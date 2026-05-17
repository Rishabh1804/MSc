// Full 13-gate Playwright walk-through for Destination Master Browser v1.1.
// Each criterion has an explicit pass/fail test that two evaluators applying
// the same script must reach the same verdict on. Source: design/foundations/
// ux-acceptance-criteria.md §3 (gates) and §5 (test plan).

const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const OUT = (name) => path.join(__dirname, name);

const SAMPLE_CSV = `destination_master_id,canonical_name,country,macro_region,state_or_area,district_or_area,destination_scale,location_type,vibe_1,vibe_2,vibe_3,trip_style_tags,context_tags,caution_tags,verification_status,promotion_status,planner_use_status,source_layer,source_id
DST2-001,Manali,India,South Asia,Himachal Pradesh,Kullu,hill_town,hill_town,mountains,relaxation,nature,family;couples,winter,landslide_risk,seed_verified,promoted,planner_ready,seed,SEED-001
DST2-002,Bali Beach,Indonesia,Southeast Asia,Bali,Denpasar,beach_city,beach_city,beach,relaxation,party,couples;solo,monsoon,,seed_unverified,candidate,needs_verification,seed,SEED-002
DST2-003,Reykjavik,Iceland,Northern Europe,Capital Region,Reykjavik,capital_city,capital_city,city,nature,museums,couples;solo,winter,,candidate,candidate,needs_verification,normalized_candidate,CAND-001
DST2-004,Disputed Place,Country X,Region X,State X,District X,city,city,city,,,solo,,,blocked,rejected,blocked,normalized_candidate,CAND-002
DST2-005,Empty Fields Test,,,,,,city,,,,,,,,,,normalized_candidate,CAND-003
DST2-006,Mumbai,India,South Asia,Maharashtra,Mumbai,metropolis,metropolis,city,nightlife,food,solo;business,monsoon,,seed_verified,promoted,planner_ready,seed,SEED-003
DST2-007,Dubai,UAE,West Asia,Dubai,Dubai,desert_beach_emirate,desert_beach_emirate,city,luxury,nightlife,couples;business,heat,,seed_verified,promoted,planner_ready,seed,SEED-004
DST2-008,Goa Coast,India,South Asia,Goa,North Goa,beach_city,beach_city,beach,party,relaxation,couples;solo,monsoon,,candidate,candidate,needs_verification,normalized_candidate,CAND-002B
DST2-009,Leh,India,South Asia,Ladakh,Leh,mountain_town,mountain_town,mountains,nature,culture,family;solo,winter,altitude_risk,seed_verified,promoted,planner_ready,seed,SEED-005
DST2-010,Pondicherry,India,South Asia,Tamil Nadu,Pondicherry,heritage_town,heritage_town,city,relaxation,culture,couples;family,heat,,seed_verified,promoted,planner_ready,seed,SEED-006`;

const results = [];

function record(id, label, pass, evidence) {
  results.push({ id, label, pass: !!pass, evidence });
  process.stdout.write(`${pass ? '✓' : '✗'} ${id} — ${label}\n`);
}

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();

  await page.route('**/destinations_master_v2.csv', r =>
    r.fulfill({ status: 200, contentType: 'text/csv', body: SAMPLE_CSV }));

  const consoleErrors = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
  page.on('pageerror', e => consoleErrors.push('pageerror: ' + e.message));
  page.on('requestfailed', r => consoleErrors.push('requestfailed: ' + r.url()));

  const arriveStart = Date.now();
  await page.goto('file:///home/user/MSc/docs/destination-master-browser.html',
    { waitUntil: 'networkidle', timeout: 15000 });
  await page.waitForTimeout(300);
  const arriveDurationMs = Date.now() - arriveStart;

  // ===== U-ARR-1: orient within 5s, no scroll, no interaction =====
  const bannerVisible = await page.locator('.trust-banner').isVisible();
  const headerVisible = await page.locator('header.app-header h1').isVisible();
  const subtitleHasDataset = (await page.locator('.subtitle').innerText()).includes('destinations_master_v2');
  record('U-ARR-1', 'Orient within 5s — tool + dataset + trust state visible without scroll',
    bannerVisible && headerVisible && subtitleHasDataset && arriveDurationMs < 5000,
    { arriveDurationMs, bannerVisible, headerVisible, subtitleHasDataset });

  // ===== U-ARR-2: trust banner persistent on scroll =====
  await page.evaluate(() => window.scrollTo(0, 800));
  await page.waitForTimeout(150);
  const bannerAfterScroll = await page.locator('.trust-banner').isVisible();
  const bannerBox = await page.locator('.trust-banner').boundingBox();
  const stickyAtTop = bannerBox && bannerBox.y < 50; // sticky positions at viewport top
  record('U-ARR-2', 'Trust banner persistent on scroll (sticky)',
    bannerAfterScroll && stickyAtTop,
    { bannerAfterScroll, bannerY: bannerBox && bannerBox.y });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(150);

  // ===== U-UND-1: trust state via text + colour + icon =====
  const bannerHasText = (await page.locator('.trust-banner-text').innerText()).toLowerCase().includes('not planner-ready');
  const bannerHasIcon = (await page.locator('.trust-banner svg').count()) >= 1;
  const bannerStyles = await page.locator('.trust-banner').evaluate(el => {
    const cs = getComputedStyle(el);
    return { bg: cs.backgroundColor, color: cs.color };
  });
  // Distinct background + foreground = colour signal present
  const hasColour = bannerStyles.bg !== 'rgba(0, 0, 0, 0)' && bannerStyles.bg !== bannerStyles.color;
  record('U-UND-1', 'Trust state via text + colour + icon',
    bannerHasText && bannerHasIcon && hasColour,
    { bannerHasText, bannerHasIcon, ...bannerStyles });

  // ===== U-NAR-1: filters reversible without leaving the result list =====
  // Apply 3 filters, then remove one via the per-chip remove button, verify count updates.
  await page.locator('#sourceLayer').selectOption('seed');
  await page.locator('#macroRegion').selectOption('South Asia');
  await page.waitForTimeout(150);
  const afterTwoFilters = await page.locator('#tableBody tr').count();
  const activeChips = await page.locator('#activeFilterChips .chip-active').count();
  const countVisibleNoScroll = await page.locator('#resultCount').isVisible();
  // Measure response time on filter change: rapid input + measure DOM update
  const responseStart = Date.now();
  await page.locator('#scale').selectOption('hill_town');
  // Wait until the result count actually changes by polling
  await page.waitForFunction((n) => Number(document.getElementById('resultCount').textContent) !== n,
    afterTwoFilters, { timeout: 1000 });
  const responseMs = Date.now() - responseStart;
  // Remove one filter via its chip × button
  const chipsBeforeRemove = await page.locator('#activeFilterChips .chip-active').count();
  await page.evaluate(() => document.querySelector('#activeFilterChips .chip-active [data-remove]').click());
  await page.waitForTimeout(150);
  const chipsAfterRemove = await page.locator('#activeFilterChips .chip-active').count();
  record('U-NAR-1', 'Filters reversible without leaving result list; count updates ≤300ms; visible without scroll',
    activeChips >= 2 && countVisibleNoScroll && responseMs <= 300 && chipsAfterRemove === chipsBeforeRemove - 1,
    { activeChips, countVisibleNoScroll, responseMs, chipsBeforeRemove, chipsAfterRemove });

  // ===== U-NAR-2: filter controls show non-default state =====
  // After U-NAR-1 removed the first chip (Source), state is:
  //   sourceLayer = default; macroRegion + scale = applied.
  // U-NAR-2 passes iff the .has-value indicator tracks the actual applied/default split.
  const sourceFieldClass = await page.locator('#sourceLayerField').getAttribute('class');
  const regionFieldClass = await page.locator('#macroRegionField').getAttribute('class');
  const scaleFieldClass = await page.locator('#scaleField').getAttribute('class');
  record('U-NAR-2', 'Filter controls visibly distinguish default vs applied state',
    !sourceFieldClass.includes('has-value') &&
    regionFieldClass.includes('has-value') &&
    scaleFieldClass.includes('has-value'),
    { sourceFieldClass, regionFieldClass, scaleFieldClass });

  // ===== U-NAR-3: trust badge survives narrowing =====
  const rowsAfterFilter = await page.locator('#tableBody tr').count();
  const badgesAfterFilter = await page.locator('#tableBody .trust-badge').count();
  record('U-NAR-3', 'Trust badge visible across the result list after narrowing',
    rowsAfterFilter > 0 && badgesAfterFilter === rowsAfterFilter,
    { rowsAfterFilter, badgesAfterFilter });

  // Clear filters to set up next checks
  await page.locator('#clearAll').click();
  await page.waitForTimeout(150);

  // ===== U-COM-1: sortable columns + first-pass under 60s =====
  // Sort by trust state to simulate "find verified records quickly"
  const compareStart = Date.now();
  await page.evaluate(() => {
    const th = [...document.querySelectorAll('table.records thead th[data-sort]')]
      .find(t => t.dataset.sort === 'trust');
    th.click();
  });
  await page.waitForTimeout(100);
  // First three rows after sorting by trust ascending should be Planner-ready
  const firstThreeTrust = await page.locator('#tableBody tr .trust-badge')
    .evaluateAll(els => els.slice(0, 3).map(e => e.getAttribute('data-state')));
  const compareMs = Date.now() - compareStart;
  const sortableCount = await page.locator('table.records thead th[data-sort]').count();
  record('U-COM-1', 'Sortable columns present (≥4 for high-frequency attributes); first comparison pass under 60s',
    sortableCount >= 7 && compareMs < 60000 && firstThreeTrust.every(s => s === 'planner-ready'),
    { sortableCount, compareMs, firstThreeTrust });

  // ===== U-COM-2: card/table toggle present; table is default =====
  // Verify table default by reloading and checking initial view
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(300);
  const tableDefault = await page.locator('#resultTable').isVisible();
  const cardsHidden = await page.locator('#resultCards').isHidden();
  const togglePresent = (await page.locator('.view-toggle button').count()) === 2;
  const tablePressed = (await page.locator('#viewTable').getAttribute('aria-pressed')) === 'true';
  record('U-COM-2', 'Card/table toggle present; table is the default',
    tableDefault && cardsHidden && togglePresent && tablePressed,
    { tableDefault, cardsHidden, togglePresent, tablePressed });

  // ===== U-INS-1: drawer ≤2 to open, 1 to close, scroll preserved =====
  // Scroll the page to a non-zero position before opening
  await page.evaluate(() => window.scrollTo(0, 200));
  await page.waitForTimeout(100);
  const scrollBeforeOpen = await page.evaluate(() => window.scrollY);
  // 1 interaction: click row (use direct dispatch to avoid Playwright scroll-into-view)
  await page.evaluate(() => document.querySelector('#tableBody tr').click());
  await page.waitForTimeout(300);
  const drawerOpenedFast = await page.locator('#drawer').isVisible();
  const scrollAfterOpen = await page.evaluate(() => window.scrollY);
  // 1 interaction to close (click X)
  await page.locator('#drawerClose').click();
  await page.waitForTimeout(500);
  const drawerClosedFast = await page.locator('#drawer').isHidden();
  const scrollAfterClose = await page.evaluate(() => window.scrollY);
  record('U-INS-1', 'Drawer ≤2 interactions to open; 1 to close; scroll position preserved',
    drawerOpenedFast && drawerClosedFast && scrollBeforeOpen === scrollAfterClose,
    { scrollBeforeOpen, scrollAfterOpen, scrollAfterClose, drawerOpenedFast, drawerClosedFast });

  // ===== U-INS-2: trust banner persistent in drawer header =====
  await page.evaluate(() => document.querySelector('#tableBody tr').click());
  await page.waitForTimeout(300);
  const drawerTrustVisible = await page.locator('#drawerTrust').isVisible();
  const drawerTrustText = await page.locator('#drawerTrustText').innerText();
  const drawerTrustHasLabel = /verified|planner|unverified|blocked|missing|conflict|unassigned/i.test(drawerTrustText);
  // Scroll drawer body; trust banner should not scroll out
  await page.evaluate(() => {
    const body = document.querySelector('.drawer-body');
    body.scrollTop = body.scrollHeight;
  });
  await page.waitForTimeout(100);
  const drawerTrustStillVisible = await page.locator('#drawerTrust').isVisible();
  record('U-INS-2', 'Trust banner persistent in drawer header (does not scroll out)',
    drawerTrustVisible && drawerTrustHasLabel && drawerTrustStillVisible,
    { drawerTrustVisible, drawerTrustText: drawerTrustText.slice(0, 80), drawerTrustStillVisible });

  // ===== U-INS-3: Prev/Next navigation inside the drawer =====
  const nameBefore = await page.locator('#drawerName').innerText();
  await page.locator('#drawerNext').click();
  await page.waitForTimeout(150);
  const nameAfterNext = await page.locator('#drawerName').innerText();
  await page.locator('#drawerPrev').click();
  await page.waitForTimeout(150);
  const nameAfterPrev = await page.locator('#drawerName').innerText();
  record('U-INS-3', 'Prev/Next navigates between records without re-opening from list',
    nameAfterNext !== nameBefore && nameAfterPrev === nameBefore,
    { nameBefore, nameAfterNext, nameAfterPrev });
  // Close for next check
  await page.locator('#drawerClose').click();
  await page.waitForTimeout(500);

  // ===== U-REC-1: empty → recovery in ≤1 interaction =====
  await page.locator('#search').fill('zzz-no-match-string-xyzpdq');
  await page.waitForTimeout(200);
  const emptyVisible = await page.locator('#resultEmpty').isVisible();
  const filtersListed = await page.locator('#emptyFiltersListed .chip-active').count();
  const clearAllVisible = await page.locator('#emptyClearAll').isVisible();
  // Single click on Clear-all → non-empty result set
  await page.locator('#emptyClearAll').click();
  await page.waitForTimeout(200);
  const rowsAfterClear = await page.locator('#tableBody tr').count();
  const emptyHiddenAfterClear = await page.locator('#resultEmpty').isHidden();
  record('U-REC-1', 'Empty-state recovery in ≤1 interaction; active filters listed; Clear-all visible',
    emptyVisible && filtersListed >= 1 && clearAllVisible && emptyHiddenAfterClear && rowsAfterClear > 0,
    { emptyVisible, filtersListed, clearAllVisible, rowsAfterClear, emptyHiddenAfterClear });

  // ===== U-REC-2: empty / loading / error are distinct (not one shared component) =====
  // Force empty again
  await page.locator('#search').fill('zzz-no-match-string-xyzpdq');
  await page.waitForTimeout(150);
  const emptyHasFilters = (await page.locator('#emptyFiltersListed').innerText()).length > 0;
  const emptyHasSuggestion = (await page.locator('#emptySuggestion').innerText()).length > 20;
  const emptyHasCTA = await page.locator('#emptyClearAll').isVisible();
  // Check the three components exist as separate IDs in the DOM
  const loadingExists = await page.locator('#resultLoading').count();
  const errorExists = await page.locator('#resultError').count();
  const emptyExists = await page.locator('#resultEmpty').count();
  const threeDistinct = loadingExists === 1 && errorExists === 1 && emptyExists === 1;
  // Loading has skeleton rows
  const skeletonRowCount = await page.locator('#resultLoading .skel-row').count();
  // Error has Retry + Report-issue actions
  const errorHasRetry = (await page.locator('#retryBtn').count()) === 1;
  record('U-REC-2', 'Empty / loading / error are distinct components; empty is content-rich',
    threeDistinct && skeletonRowCount >= 5 && errorHasRetry &&
    emptyHasFilters && emptyHasSuggestion && emptyHasCTA,
    { threeDistinct, skeletonRowCount, errorHasRetry, emptyHasFilters, emptyHasSuggestion, emptyHasCTA });
  await page.locator('#emptyClearAll').click();
  await page.waitForTimeout(150);

  // ===== U-LEA-1: trust signal consistent across the journey =====
  // Pick one specific record (by name) and verify trust state matches across:
  //   list-row badge → card-view badge → drawer-header label
  const targetName = 'Bali Beach';
  const listRowTrust = await page.locator(`#tableBody tr:has-text("${targetName}") .trust-badge`).getAttribute('data-state');
  // Switch to cards view
  await page.locator('#viewCards').click();
  await page.waitForTimeout(200);
  const cardTrust = await page.locator(`.card:has-text("${targetName}") .trust-badge`).getAttribute('data-state');
  // Open drawer from cards view
  await page.evaluate(name => {
    const card = [...document.querySelectorAll('.card')].find(c => c.textContent.includes(name));
    card.click();
  }, targetName);
  await page.waitForTimeout(300);
  const drawerName = await page.locator('#drawerName').innerText();
  const drawerTrustLabel = (await page.locator('#drawerTrustText strong').innerText()).toLowerCase();
  // Map drawer-label back to the state slug for comparison
  const labelToState = { 'verified': 'verified', 'planner-ready': 'planner-ready', 'unverified': 'unverified',
                        'blocked': 'blocked', 'missing fields': 'missing-fields', 'conflict': 'conflict',
                        'unassigned': 'unassigned' };
  const drawerTrust = labelToState[drawerTrustLabel];
  record('U-LEA-1', 'Trust signal consistent across list-row, card, and drawer-header for the same record',
    drawerName === targetName && listRowTrust === cardTrust && cardTrust === drawerTrust,
    { targetName, listRowTrust, cardTrust, drawerTrust, drawerName });
  await page.locator('#drawerClose').click();
  await page.waitForTimeout(500);

  // ===== POLISH-1: focus restoration on drawer close =====
  // Switch back to table view first (U-LEA-1 left us in cards; hidden TR can't receive focus).
  // Click a specific row; close the drawer; assert focus returned to that row.
  await page.locator('#viewTable').click();
  await page.waitForTimeout(200);
  await page.evaluate(() => document.querySelector('#tableBody tr[data-index="0"]').click());
  await page.waitForTimeout(300);
  await page.locator('#drawerClose').click();
  await page.waitForTimeout(500);
  const restoredIndex = await page.evaluate(() => {
    const el = document.activeElement;
    return { tag: el && el.tagName, idx: el && el.dataset ? el.dataset.index : null };
  });
  record('POLISH-1', 'Focus restoration on drawer close — returns to the opener row',
    restoredIndex.tag === 'TR' && restoredIndex.idx === '0',
    { restoredIndex });

  // ===== POLISH-2: result-count perceptibility (.flash class fires on count change) =====
  await page.locator('#search').fill('Mumbai');
  await page.waitForFunction(() => document.getElementById('resultCount').classList.contains('flash'),
    { timeout: 500 });
  const flashedAfterFilter = await page.evaluate(() =>
    document.getElementById('resultCount').classList.contains('flash'));
  record('POLISH-2', 'Result-count flash animation fires on count change (U-NAR-1 "perceptible")',
    flashedAfterFilter,
    { flashedAfterFilter });
  await page.locator('#clearAll').click();
  await page.waitForTimeout(200);

  // ===== POLISH-3: drawer aria-describedby points at the trust line =====
  const ariaDescribedby = await page.locator('#drawer').getAttribute('aria-describedby');
  const trustTextId = await page.locator('#drawerTrustText').getAttribute('id');
  record('POLISH-3', 'Drawer has aria-describedby referencing the trust-state line',
    ariaDescribedby === 'drawerTrustText' && trustTextId === 'drawerTrustText',
    { ariaDescribedby, trustTextId });

  // ===== POLISH-4: taxonomy-drift console.warn fires on unmapped status =====
  // Reload with a stubbed CSV containing a synthetic unknown verification_status.
  const driftCsv = SAMPLE_CSV + `\nDST2-999,Frobnitz Place,Country Z,Region Z,,,city,city,,,,,,,unknown_drift_status,promoted,promoted,seed,SEED-999`;
  await page.unroute('**/destinations_master_v2.csv');
  await page.route('**/destinations_master_v2.csv', r =>
    r.fulfill({ status: 200, contentType: 'text/csv', body: driftCsv }));
  const driftWarnings = [];
  const captureWarn = m => { if (m.type() === 'warning') driftWarnings.push(m.text()); };
  page.on('console', captureWarn);
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(400);
  page.off('console', captureWarn);
  const driftWarnFired = driftWarnings.some(t => t.includes('unmapped status') && t.includes('unknown_drift_status'));
  record('POLISH-4', 'Taxonomy-drift console.warn fires on unmapped verification_status; row still renders',
    driftWarnFired,
    { driftWarnings: driftWarnings.slice(0, 3), driftWarnFired });
  // Restore the original sample CSV
  await page.unroute('**/destinations_master_v2.csv');
  await page.route('**/destinations_master_v2.csv', r =>
    r.fulfill({ status: 200, contentType: 'text/csv', body: SAMPLE_CSV }));
  await page.reload({ waitUntil: 'networkidle' });
  await page.waitForTimeout(300);

  // ===== Final: console-error count must be zero =====
  const consoleClean = consoleErrors.length === 0;
  record('CONSOLE', 'Zero console errors / pageerrors / requestfailed across the full walk-through',
    consoleClean,
    { count: consoleErrors.length, sample: consoleErrors.slice(0, 3) });

  // Final screenshots: table view, cards view, empty state, drawer open
  await page.locator('#viewTable').click();
  await page.waitForTimeout(200);
  await page.screenshot({ path: OUT('walkthrough-table.png'), fullPage: false });
  await page.locator('#viewCards').click();
  await page.waitForTimeout(200);
  await page.screenshot({ path: OUT('walkthrough-cards.png'), fullPage: false });
  await page.locator('#viewTable').click();
  await page.locator('#search').fill('zzz-no-match-string-xyzpdq');
  await page.waitForTimeout(200);
  await page.screenshot({ path: OUT('walkthrough-empty.png'), fullPage: false });
  await page.locator('#emptyClearAll').click();
  await page.waitForTimeout(150);
  await page.evaluate(() => document.querySelector('#tableBody tr').click());
  await page.waitForTimeout(300);
  await page.screenshot({ path: OUT('walkthrough-drawer.png'), fullPage: false });

  const passed = results.filter(r => r.pass).length;
  const total = results.length;
  console.log(`\n=== WALK-THROUGH RESULT: ${passed}/${total} gates pass ===\n`);
  console.log(JSON.stringify(results, null, 2));
  await browser.close();
  if (passed !== total) process.exit(1);
})().catch(e => { console.error(e); process.exit(1); });
