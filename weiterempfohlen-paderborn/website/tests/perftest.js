const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const vp of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const p = await b.newPage({ viewport: vp }); p.on('pageerror', e => errs.push(e.message));
    const reqs = []; p.on('request', r => reqs.push(r.url().split('/').pop()));
    await p.goto('file://' + __dirname + '/../local.html', { waitUntil: 'load' }); await p.waitForTimeout(1200);
    const fonts = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight).join(', '));
    console.log(vp.width, 'nach Laden:', reqs.filter(r => /\.(webp|jpg|woff2)$/.test(r)).join(' '), '| Schriften:', fonts);
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } });
    await p.waitForTimeout(800);
    console.log(vp.width, 'nach Scrollen:', reqs.filter(r => /\.(webp|jpg)$/.test(r)).length, 'Bilder;', await p.evaluate(() => [...document.querySelectorAll('[data-photo]')].filter(e => !e.classList.contains('has-photo')).map(e => e.dataset.photo).join(' ') || 'alle Fotos sichtbar'));
    const bts = await p.$('.bts'); await bts.scrollIntoViewIfNeeded(); await p.waitForTimeout(500); await bts.screenshot({ path: __dirname + `/../shots/bts_new_${vp.width}.png` });
    await p.close();
  }
  console.log('errs', JSON.stringify(errs)); await b.close();
})();
