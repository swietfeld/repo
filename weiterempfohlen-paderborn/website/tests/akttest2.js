const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const out = []; const errs = [];
  for (const vp of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const p = await b.newPage({ viewport: vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + __dirname + '/../local.html'); await p.waitForTimeout(800);
    const st = () => p.evaluate(() => { const t = id => document.getElementById(id).textContent; const sc = [...document.querySelectorAll('#spScen button')].filter(x => x.getAttribute('aria-pressed') === 'true').map(x => x.dataset.sc).join(); return [sc, t('cCost'), t('cPart'), t('cCity'), t('cPerEp'), document.getElementById('cPlus').hidden ? '-' : t('cPlus'), t('cAkt'), t('stackL'), ['aS','aM','aL'].map(t).join('/')].join(' | '); });
    out.push(vp.width + ' gut: ' + await st());
    await p.click('#spScen [data-sc="akt"]'); out.push(vp.width + ' akt: ' + await st());
    if (vp.width === 1440) {
      await p.click('#aktSizes [data-g="l"][data-d="-1"]'); out.push(' -L: ' + await st());
      await p.click('#aktSizes [data-g="s"][data-d="1"]'); await p.click('#aktSizes [data-g="s"][data-d="1"]'); await p.click('#aktSizes [data-g="m"][data-d="1"]'); out.push(' +2S+M: ' + await st());
      out.push(' plus disabled: ' + await p.evaluate(() => [...document.querySelectorAll('#aktSizes [data-d="1"]')].map(b => b.disabled).join()));
      await p.click('#spScen [data-sc="akt"]'); await p.click('#spSeg button[data-side="1"]'); out.push(' akt testphase: ' + await st());
      await p.click('#spSeg button[data-side="0"]');
    }
    await p.click('#spScen [data-sc="akt"]'); await p.waitForTimeout(600);
    const row = await p.$('#pkAktRow'); await row.scrollIntoViewIfNeeded(); await row.screenshot({ path: __dirname + `/../shots/akt2row_${vp.width}.png` });
    await (await p.$('.spons-sum')).screenshot({ path: __dirname + `/../shots/akt2sum_${vp.width}.png` });
    await p.close();
  }
  out.push('errs ' + JSON.stringify(errs)); console.log(out.join('\n')); await b.close();
})();
