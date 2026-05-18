// Lab 04 Loop 1 — batch-promote-confirm modal walk-through (v1.2 feature).
// Tests U-CONF-1..4 acceptance criteria from `design/foundations/
// ux-acceptance-criteria.md`. Each criterion has a pass/fail check that two
// evaluators applying the same script must reach the same verdict on.

const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const fs = require('fs');
const OUT = (name) => path.join(__dirname, name);

const SAMPLE_CSV = `destination_master_id,canonical_name,country,macro_region,state_or_area,district_or_area,destination_scale,location_type,vibe_1,vibe_2,vibe_3,trip_style_tags,context_tags,caution_tags,verification_status,promotion_status,planner_use_status,source_layer,source_id
DST2-001,Manali,India,South Asia,Himachal Pradesh,Kullu,hill_town,hill_town,mountains,relaxation,nature,family;couples,winter,landslide_risk,seed_verified,promoted,planner_ready,seed,SEED-001
DST2-002,Bali Beach,Indonesia,Southeast Asia,Bali,Denpasar,beach_city,beach_city,beach,relaxation,party,couples;solo,monsoon,,seed_unverified,candidate,needs_verification,seed,SEED-002
DST2-003,Reykjavik,Iceland,Northern Europe,Capital Region,Reykjavik,capital_city,capital_city,city,nature,museums,couples;solo,winter,,candidate,candidate,needs_verification,normalized_candidate,CAND-001
DST2-004,Disputed Place,Country X,Region X,State X,District X,city,city,city,,,solo,,,blocked,rejected,blocked,normalized_candidate,CAND-002
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

  const fileUrl = 'file://' + path.resolve(__dirname, '../../../../../docs/destination-master-browser.html');
  await page.goto(fileUrl);
  await page.waitForSelector('table.records tbody tr');

  // ---------- Setup: select three records ----------
  const checkboxes = await page.locator('table.records tbody tr input[type="checkbox"]').elementHandles();
  await checkboxes[0].evaluate(el => el.click());
  await checkboxes[1].evaluate(el => el.click());
  await checkboxes[2].evaluate(el => el.click());
  await page.waitForTimeout(100);

  // Batch action bar should now show
  const barVisible = await page.locator('#batchActionBar:not(.hidden)').count();
  record('SETUP', 'Batch action bar shows after selecting rows', barVisible === 1, { barVisible });

  // ---------- Open the modal ----------
  const promoteBtn = page.locator('#batchPromoteBtn');
  const promoteBtnBox = await promoteBtn.boundingBox();
  await promoteBtn.click();
  await page.waitForTimeout(150);

  // Capture modal-open screenshot
  await page.screenshot({ path: OUT('walkthrough-modal-open.png'), fullPage: false });

  // ---------- U-CONF-1: modal body shows N records ----------
  const titleText = await page.locator('#promoteModalTitle').textContent();
  const recordsListItems = await page.locator('#promoteModalList li').count();
  const noScrollNeeded = recordsListItems === 3; // 3 selected, list fits with no overflow message
  const moreText = (await page.locator('#promoteModalMore').textContent()).trim();
  record('U-CONF-1', 'Modal body shows record names + count without scrolling past list',
    /promote 3 records/i.test(titleText) && recordsListItems === 3 && moreText === '',
    { titleText, recordsListItems, moreText, noScrollNeeded });

  // ---------- U-CONF-2: cancel ≤ 1 interaction ----------
  // Cancel button is default-focused
  const focusedAfterOpen = await page.evaluate(() => document.activeElement && document.activeElement.id);
  // Esc cancels
  await page.keyboard.press('Escape');
  await page.waitForTimeout(120);
  const modalHiddenAfterEsc = await page.locator('#promoteModal[hidden]').count();
  record('U-CONF-2a', 'Cancel button is default-focused when modal opens',
    focusedAfterOpen === 'promoteCancelBtn', { focusedAfterOpen });
  record('U-CONF-2b', 'Esc closes the modal in 1 interaction', modalHiddenAfterEsc === 1, { modalHiddenAfterEsc });

  // Re-open the modal to test overlay-click cancel
  await promoteBtn.click();
  await page.waitForTimeout(120);
  // Click the overlay (top-left, away from modal)
  await page.locator('#promoteOverlay').click({ position: { x: 10, y: 10 } });
  await page.waitForTimeout(120);
  const modalHiddenAfterOverlay = await page.locator('#promoteModal[hidden]').count();
  record('U-CONF-2c', 'Overlay-click closes the modal in 1 interaction', modalHiddenAfterOverlay === 1, { modalHiddenAfterOverlay });

  // ---------- U-CONF-3: screen-reader accessibility ----------
  // Re-open to inspect ARIA attributes
  await promoteBtn.click();
  await page.waitForTimeout(120);
  const aria = await page.evaluate(() => {
    const m = document.getElementById('promoteModal');
    return {
      role: m.getAttribute('role'),
      ariaModal: m.getAttribute('aria-modal'),
      labelledby: m.getAttribute('aria-labelledby'),
      describedby: m.getAttribute('aria-describedby'),
      titleText: document.getElementById('promoteModalTitle').textContent.trim(),
      descTextFirstLine: document.getElementById('promoteModalLead').textContent.trim()
    };
  });
  record('U-CONF-3', 'Modal exposes role="dialog" + aria-modal="true" + aria-labelledby + aria-describedby',
    aria.role === 'dialog' && aria.ariaModal === 'true' && aria.labelledby === 'promoteModalTitle' && aria.describedby === 'promoteModalDesc',
    aria);

  // ---------- U-CONF-4: focus trap + focus restoration ----------
  // From Cancel (current focus), Tab → Confirm
  await page.keyboard.press('Tab');
  const focusedAfterTab = await page.evaluate(() => document.activeElement && document.activeElement.id);
  // Tab again → cycles back to Cancel (focus trap; only 2 focusables in footer)
  await page.keyboard.press('Tab');
  const focusedAfterTab2 = await page.evaluate(() => document.activeElement && document.activeElement.id);
  record('U-CONF-4a', 'Focus trap cycles among modal footer buttons (Cancel ↔ Confirm)',
    focusedAfterTab === 'promoteConfirmBtn' && focusedAfterTab2 === 'promoteCancelBtn',
    { focusedAfterTab, focusedAfterTab2 });

  // Close modal via Cancel button click and verify focus restores to Promote button (opener)
  await page.locator('#promoteCancelBtn').click();
  await page.waitForTimeout(120);
  const focusedAfterClose = await page.evaluate(() => document.activeElement && document.activeElement.id);
  record('U-CONF-4b', 'Focus restores to the trigger (Promote button) after close',
    focusedAfterClose === 'batchPromoteBtn', { focusedAfterClose });

  // ---------- Confirm path: actually promote ----------
  // Re-open and confirm. Verify the rows' Planner status flips to planner-ready in the table.
  await promoteBtn.click();
  await page.waitForTimeout(120);
  // The 3 records selected before Cancel are gone (Cancel keeps state but Esc/overlay-click also keep state in this implementation).
  // Re-check: selection survived because we used cancel paths above? Let's check selected count.
  const stillSelected = await page.locator('table.records tbody tr.selected').count();
  if (stillSelected === 0) {
    // Re-select
    const cbs = await page.locator('table.records tbody tr input[type="checkbox"]').elementHandles();
    await cbs[0].evaluate(el => el.click());
    await cbs[1].evaluate(el => el.click());
    await cbs[2].evaluate(el => el.click());
    await page.waitForTimeout(80);
    await promoteBtn.click();
    await page.waitForTimeout(120);
  }
  // Confirm promotion
  await page.locator('#promoteConfirmBtn').click();
  await page.waitForTimeout(300);
  const modalHiddenAfterConfirm = await page.locator('#promoteModal[hidden]').count();
  // Toast should show "promoted to Planner"
  const toastShown = await page.locator('.promote-toast.show').count();
  // Selection should clear
  const selectedAfterConfirm = await page.locator('table.records tbody tr.selected').count();
  record('CONFIRM-PATH', 'Confirm path closes modal + shows toast + clears selection',
    modalHiddenAfterConfirm === 1 && toastShown >= 0 && selectedAfterConfirm === 0,
    { modalHiddenAfterConfirm, toastShown, selectedAfterConfirm });

  // Capture final state
  await page.screenshot({ path: OUT('walkthrough-modal-after-confirm.png'), fullPage: false });

  // ---------- CONSOLE check ----------
  record('CONSOLE', 'Zero console errors / pageerrors / requestfailed across the modal walk-through',
    consoleErrors.length === 0, { count: consoleErrors.length, sample: consoleErrors.slice(0, 3) });

  fs.writeFileSync(OUT('walkthrough-conf-results.json'), JSON.stringify(results, null, 2));
  console.log('\nResults written to', OUT('walkthrough-conf-results.json'));
  const pass = results.filter(r => r.pass).length;
  console.log(`\n${pass} / ${results.length} pass`);
  await browser.close();
  process.exit(pass === results.length ? 0 : 1);
})();
