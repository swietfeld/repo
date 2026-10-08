const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const vp of [{ width: 1440, height: 900 }, { width: 390, height: 844 }]) {
    const ctx = await b.newContext({ viewport: vp, permissions: ['clipboard-read', 'clipboard-write'] });
    const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + __dirname + '/../local.html'); await p.waitForTimeout(600);
    const el = await p.$('.contact'); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(600);
    await el.screenshot({ path: __dirname + `/../shots/kontakt_${vp.width}.png` });
    if (vp.width === 1440) {
      await p.click('[data-copy="cMail"]'); await p.waitForTimeout(200);
      console.log('clipboard mail:', await p.evaluate(() => navigator.clipboard.readText()).catch(e => 'n/a ' + e.message));
      await p.click('[data-copy="cTel"]'); await p.waitForTimeout(200);
      console.log('clipboard tel:', await p.evaluate(() => navigator.clipboard.readText()).catch(e => 'n/a ' + e.message));
      console.log(await p.evaluate(() => [...document.querySelectorAll('.crow2 a')].map(a => a.href).join(' ')));
    }
    await ctx.close();
  }
  console.log('errs', JSON.stringify(errs)); await b.close();
})();
