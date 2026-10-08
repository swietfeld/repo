const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const t0 = Date.now(); await p.goto('file://' + __dirname + '/../local.html', { waitUntil: 'commit' });
  const shots = [];
  for (const t of [60, 300, 1600]) { await p.waitForTimeout(Math.max(0, t - (Date.now() - t0))); const f = __dirname + `/../shots/fp_${t}.png`; await p.screenshot({ path: f, clip: { x: 0, y: 0, width: 1440, height: 900 } }); shots.push(f); }
  console.log(await p.evaluate(() => document.fonts.check("800 40px 'Bricolage Grotesque'") + ' ' + document.fonts.check("16px 'DM Sans'")));
  await b.close();
})();
