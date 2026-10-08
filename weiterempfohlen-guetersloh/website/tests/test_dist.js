const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  const errs = [], reqs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) reqs.push(r.url()); });
  await p.goto('file://' + __dirname + '/../dist/index.html'); await p.waitForTimeout(1500);
  const f = await p.evaluate(async () => { await document.fonts.ready; return [...document.fonts].filter(x => x.status === 'loaded').map(x => x.family + ' ' + x.style).filter((v, i, a) => a.indexOf(v) === i); });
  console.log('errors', JSON.stringify(errs)); console.log('external requests', JSON.stringify(reqs)); console.log('fonts loaded', JSON.stringify(f));
  console.log('sticker', await p.evaluate(() => document.getElementById('doorSticker').getBoundingClientRect().width));
  await b.close();
})();
