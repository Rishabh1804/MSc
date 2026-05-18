// v1.2.1 mobile-viewport verification — captures the four fixed regions at
// 360x740 (typical Android narrow viewport) to confirm the mobile fixes
// render correctly. This is the workspace's first mobile-viewport capture;
// future polish PRs should follow the same pattern.

const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const OUT = (name) => path.join(__dirname, name);

const SAMPLE_CSV = `destination_master_id,canonical_name,country,macro_region,state_or_area,district_or_area,destination_scale,location_type,vibe_1,vibe_2,vibe_3,trip_style_tags,context_tags,caution_tags,verification_status,promotion_status,planner_use_status,source_layer,source_id
DST2-001,Manali,India,South Asia,Himachal Pradesh,Kullu,hill_town,hill_town,mountains,relaxation,nature,family;couples,winter,landslide_risk,seed_unverified,candidate,needs_verification,seed,SEED-001
DST2-002,Bali Beach,Indonesia,Southeast Asia,Bali,Denpasar,beach_city,beach_city,beach,relaxation,party,couples;solo,monsoon,,seed_unverified,candidate,needs_verification,seed,SEED-002
DST2-003,Reykjavik,Iceland,Northern Europe,Capital Region,Reykjavik,capital_city,capital_city,city,nature,museums,couples;solo,winter,,candidate,candidate,needs_verification,normalized_candidate,CAND-001
DST2-004,Disputed Place,Country X,Region X,State X,District X,city,city,city,,,solo,,,blocked,rejected,blocked,normalized_candidate,CAND-002
DST2-009,Leh,India,South Asia,Ladakh,Leh,mountain_town,mountain_town,mountains,nature,culture,family;solo,winter,altitude_risk,seed_unverified,candidate,needs_verification,seed,SEED-005`;

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  // Mobile-viewport context: ~Android narrow phone (360x740)
  const ctx = await browser.newContext({
    viewport: { width: 360, height: 740 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    userAgent: 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
  });
  const page = await ctx.newPage();

  await page.route('**/destinations_master_v2.csv', r =>
    r.fulfill({ status: 200, contentType: 'text/csv', body: SAMPLE_CSV }));

  const fileUrl = 'file://' + path.resolve(__dirname, '../../../../../docs/destination-master-browser.html');
  await page.goto(fileUrl);
  await page.waitForSelector('table.records tbody tr, .cards .card');

  // F-MOB-1 fix verification — sortable column headers in table view
  await page.locator('#viewTable').click();
  await page.waitForTimeout(150);
  // Scroll past the toolbar so the table header is in view
  await page.evaluate(() => document.querySelector('table.records thead').scrollIntoView({ block: 'start' }));
  await page.waitForTimeout(150);
  await page.screenshot({ path: OUT('mobile-table-headers.png'), fullPage: false });

  // F-MOB-4 fix verification — card with caution chips (Manali has landslide_risk; Leh has altitude_risk)
  await page.locator('#viewCards').click();
  await page.waitForTimeout(150);
  await page.evaluate(() => document.querySelector('.cards').scrollIntoView({ block: 'start' }));
  await page.waitForTimeout(150);
  await page.screenshot({ path: OUT('mobile-cards-caution.png'), fullPage: false });

  // F-MOB-3 fix verification — drawer Workflow Verification row should now show the pill
  // Open Manali card
  await page.locator('.cards .card').first().click();
  await page.waitForTimeout(250);
  // Drawer should open; scroll to Workflow section
  await page.evaluate(() => {
    const sections = document.querySelectorAll('.drawer-section');
    for (const s of sections) {
      if (s.textContent.includes('WORKFLOW') || s.textContent.includes('Workflow') || s.textContent.includes('workflow')) {
        s.scrollIntoView({ block: 'start' });
        break;
      }
    }
  });
  await page.waitForTimeout(150);
  await page.screenshot({ path: OUT('mobile-drawer-workflow.png'), fullPage: false });

  await browser.close();
  console.log('Captured 3 mobile-viewport screenshots in', __dirname);
})();
