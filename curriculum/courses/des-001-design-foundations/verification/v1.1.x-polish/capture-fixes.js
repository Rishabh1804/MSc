// Lab 06 fixes — before/after screenshot capture for the audit doc.
// Captures the six fixed regions on the polished v1.1.x build so the audit's
// "no screenshot evidence" missed-opportunity (Lyra review on PR #18) closes.
//
// Output: ./fix-{1,2,3,4,5a,6}-after.png at curriculum/courses/des-001-design-foundations/verification/v1.1.x-polish/
//
// Note: "before" screenshots come from the existing PR-#12 walkthrough captures
// (walkthrough-table.png + walkthrough-cards.png) — those show v1.1 pre-polish.

const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
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

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();

  await page.route('**/destinations_master_v2.csv', r =>
    r.fulfill({ status: 200, contentType: 'text/csv', body: SAMPLE_CSV }));

  const fileUrl = 'file://' + path.resolve(__dirname, '../../../../../docs/destination-master-browser.html');
  await page.goto(fileUrl);
  await page.waitForSelector('table.records tbody tr');

  // Fix #4 — sortable column header affordance: capture table header area showing ↕ glyphs.
  // Fix #5a — search vs selects: visible separator visible in same shot.
  // Fix #2 — view-toggle separator: visible in same shot.
  // Fix #3 — active-filter summary separation: deepen tint visible without filters; capture after a filter applied.
  // Fix #1 — verification pill (table + card): visible in table view.
  // Fix #6 — caution-chip divider: cards view, captured at fix-6.
  await page.locator('.toolbar').screenshot({ path: OUT('fix-2-5a-toolbar-separators-after.png') });
  await page.locator('table.records thead').screenshot({ path: OUT('fix-3-4-table-headers-after.png') });
  await page.locator('table.records').screenshot({ path: OUT('fix-1-verif-pill-table-after.png') });

  // Apply a filter so the active-filter summary appears
  await page.locator('#scale').selectOption('hill_town');
  await page.waitForTimeout(150);
  await page.locator('.active-filters').screenshot({ path: OUT('fix-3-active-filters-after.png') });
  await page.locator('#scale').selectOption('');

  // Switch to cards view to capture verif-pill in meta-grid + caution-chip divider
  await page.locator('#viewCards').click();
  await page.waitForTimeout(150);
  // Manali has caution_tags = "landslide_risk" → first card shows the warn chip
  const firstCard = page.locator('.card').first();
  await firstCard.screenshot({ path: OUT('fix-1-6-card-after.png') });

  await browser.close();
  console.log('Captured 5 after-screenshots in', __dirname);
})();
