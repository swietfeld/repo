const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; const out = [];
  for (const vp of [{ width: 1440, height: 900 }, { width: 820, height: 1000 }, { width: 390, height: 844 }]) {
    const p = await b.newPage({ viewport: vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + __dirname + '/../local.html'); await p.waitForTimeout(600);
    await p.evaluate(() => document.querySelectorAll('[data-reveal]').forEach(e => e.classList.add('in', 'is-in', 'shown')));
    const el = await p.$('#paket'); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(900);
    await el.screenshot({ path: __dirname + `/../shots/pkg_${vp.width}.png` });
    const plan = await p.$('.plan.main'); await plan.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
    await (await p.$('.offer')).screenshot({ path: __dirname + `/../shots/offer_${vp.width}.png` });
    out.push(vp.width + ' overflow: ' + await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
    out.push(vp.width + ' calc: ' + await p.evaluate(() => [document.getElementById('cPerEp').textContent, document.getElementById('cValue').textContent].join(' | ')));
    await p.close();
  }
  console.log(out.join('\n')); console.log('errs', JSON.stringify(errs)); await b.close();
})();
