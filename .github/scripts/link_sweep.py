#!/usr/bin/env python3
"""Batch-9 internal link sweep.

Rewrites markdown link targets that reference moved files by their old
bare names. The migration moved 13 charter docs to `charter/`, 16
operations docs to `operations/`, and four root directories under
`capabilities/`, `curriculum/`, and `charter/orientation/`. Links
written against the pre-migration root layout no longer resolve.

For each `.md` file in the repo (excluding the migration registers
themselves, which intentionally cite pre-migration paths as historical
record), this script:

  1. Finds every Markdown link target `(<target>)` and reference-style
     definition `[id]: <target>`.
  2. If `<target>` is a bare filename matching a moved doc, or a
     `<dir>/...` path whose `<dir>` is a moved root directory, it is
     rewritten to a path relative to the file containing the link
     (using `os.path.relpath`).
  3. Anchors (`#section`) and query strings are preserved.

The script is idempotent — running it on an already-swept tree is a
no-op. Files whose bare references happen to be self-referential
(e.g. `charter/BUDGET.md` linking to `BUDGET.md`) get no rewrite,
because `os.path.relpath` returns `BUDGET.md` unchanged.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Pre-migration root-level docs that moved during the migration, with
# their post-migration paths. Built from the directory listings of
# charter/ and operations/.
MOVED_FILES: dict[str, str] = {
    # charter/
    "BUDGET.md": "charter/BUDGET.md",
    "CODEMIKE.md": "charter/CODEMIKE.md",
    "DATA_POLICY.md": "charter/DATA_POLICY.md",
    "DOCTRINES.md": "charter/DOCTRINES.md",
    "DOMAIN_MAP.md": "charter/DOMAIN_MAP.md",
    "GITHUB_WORKFLOW.md": "charter/GITHUB_WORKFLOW.md",
    "HARD_RULES.md": "charter/HARD_RULES.md",
    "HTML_ARTIFACTS.md": "charter/HTML_ARTIFACTS.md",
    "PRODUCTISATION.md": "charter/PRODUCTISATION.md",
    "QA_CHECKLIST.md": "charter/QA_CHECKLIST.md",
    "REPO_STRUCTURE.md": "charter/REPO_STRUCTURE.md",
    "RESPONSIBLE_AI.md": "charter/RESPONSIBLE_AI.md",
    "STUDENT_LIFE.md": "charter/STUDENT_LIFE.md",
    "SUPERVISION.md": "charter/SUPERVISION.md",
    "TOOLING.md": "charter/TOOLING.md",
    # operations/
    "ARTIFACT_INDEX.md": "operations/ARTIFACT_INDEX.md",
    "CAPABILITIES.md": "operations/CAPABILITIES.md",
    "DATASETS.md": "operations/DATASETS.md",
    "DECISIONS.md": "operations/DECISIONS.md",
    "EVIDENCE.md": "operations/EVIDENCE.md",
    "EXPERIMENTS.md": "operations/EXPERIMENTS.md",
    "FAILURE_LOG.md": "operations/FAILURE_LOG.md",
    "LIBRARY.md": "operations/LIBRARY.md",
    "NEXT_ACTIONS.md": "operations/NEXT_ACTIONS.md",
    "PORTFOLIO.md": "operations/PORTFOLIO.md",
    "PROJECT_LOG.md": "operations/PROJECT_LOG.md",
    "RISK_REGISTER.md": "operations/RISK_REGISTER.md",
    "ROADMAP.md": "operations/ROADMAP.md",
    "SKILL_MAP.md": "operations/SKILL_MAP.md",
    "TRANSFER_LOG.md": "operations/TRANSFER_LOG.md",
    "VIVA.md": "operations/VIVA.md",
}

# Pre-migration root-level directories that moved. Maps a path prefix
# to its new location.
MOVED_DIRS: dict[str, str] = {
    "anti-patterns": "capabilities/anti-patterns",
    "artifacts": "operations/artifacts",
    "assignments": "curriculum/assignments",
    "benchmarks": "operations/benchmarks",
    "case-studies": "capabilities/case-studies",
    "courses": "curriculum/courses",
    "decision-science": "capabilities/decision-science",
    "modules": "curriculum/modules",
    "orientation": "charter/orientation",
    "patterns": "capabilities/patterns",
    "synthetic-data": "datasets/synthetic",
    "thesis": "curriculum/thesis",
    "trackers": "operations/trackers",
}

# Files whose old citations are intentional historical record.
SKIP_FILES = {
    "operations/MIGRATION_LOG.md",
    "operations/MIGRATION_PLAN.md",
    ".github/scripts/link_sweep.py",
}

# Match Markdown inline link: `](target)` capturing the target.
INLINE_LINK_RE = re.compile(r"(?<!\\)\]\((?P<target>[^)\s]+)(?P<title>\s+\"[^\"]*\")?\)")

# Match reference-style definition at line start: `[id]: target`.
REF_DEF_RE = re.compile(r"^(\s*\[[^\]]+\]:\s+)(?P<target>\S+)", re.MULTILINE)


def rewrite_target(target: str, source_file: Path) -> str:
    """Rewrite a link target if it points at a moved file or dir."""
    # Split anchor / query off the path portion.
    path_part = target
    suffix = ""
    for sep in ("#", "?"):
        i = path_part.find(sep)
        if i != -1:
            suffix = path_part[i:] + suffix
            path_part = path_part[:i]

    if not path_part or path_part.startswith(("http://", "https://", "mailto:", "//")):
        return target

    # Direct file-name match.
    if path_part in MOVED_FILES:
        new_abs = REPO_ROOT / MOVED_FILES[path_part]
        new_rel = os.path.relpath(new_abs, source_file.parent)
        return new_rel + suffix

    # Old-directory prefix match (e.g. `orientation/research-ethics.md`).
    for old_dir, new_dir in MOVED_DIRS.items():
        if path_part == old_dir or path_part.startswith(old_dir + "/"):
            tail = path_part[len(old_dir):]
            new_abs = REPO_ROOT / (new_dir + tail)
            new_rel = os.path.relpath(new_abs, source_file.parent)
            return new_rel + suffix

    return target


def sweep_file(md_path: Path) -> tuple[bool, int]:
    src = md_path.read_text(encoding="utf-8")
    rewrites = 0

    def inline_repl(m: re.Match) -> str:
        nonlocal rewrites
        old_target = m.group("target")
        title = m.group("title") or ""
        new_target = rewrite_target(old_target, md_path)
        if new_target != old_target:
            rewrites += 1
        return "](" + new_target + title + ")"

    def ref_repl(m: re.Match) -> str:
        nonlocal rewrites
        old_target = m.group("target")
        new_target = rewrite_target(old_target, md_path)
        if new_target != old_target:
            rewrites += 1
        return m.group(1) + new_target

    out = INLINE_LINK_RE.sub(inline_repl, src)
    out = REF_DEF_RE.sub(ref_repl, out)

    if out != src:
        md_path.write_text(out, encoding="utf-8")
        return True, rewrites
    return False, 0


def main() -> int:
    changed = 0
    total_rewrites = 0
    for md_path in sorted(REPO_ROOT.rglob("*.md")):
        rel = md_path.relative_to(REPO_ROOT).as_posix()
        if rel in SKIP_FILES:
            continue
        if "/.git/" in str(md_path):
            continue
        did_change, n = sweep_file(md_path)
        if did_change:
            changed += 1
            total_rewrites += n
            print(f"{rel}: {n} link(s) rewritten")
    print(f"\n{changed} file(s) changed, {total_rewrites} link(s) rewritten")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
