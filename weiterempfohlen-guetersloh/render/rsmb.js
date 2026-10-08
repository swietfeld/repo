const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const head = fs.readFileSync(__dirname + '/head.html', 'utf8');
  for (const n of process.argv.slice(2)) {
    const html = head + fs.readFileSync(__dirname + '/../markenbuch/project/slides/' + n + '.html', 'utf8') + '</body></html>';
    fs.writeFileSync(__dirname + '/tmp_' + n + '.html', html);
    await p.goto('file://' + __dirname + '/tmp_' + n + '.html'); await p.waitForTimeout(400);
    const over = await p.evaluate(() => { const s = document.querySelector('section'); return [...s.querySelectorAll('*')].filter(e => { const r = e.getBoundingClientRect(); return r.bottom > 1080 - 120 && !e.closest('[style*="bottom:64px"]') && r.height > 0 && getComputedStyle(e).position !== 'absolute'; }).map(e => e.tagName + ':' + Math.round(e.getBoundingClientRect().bottom)).slice(0, 5); });
    console.log(n, JSON.stringify(over));
    await p.screenshot({ path: __dirname + '/mb-' + n + '.png', clip: { x: 0, y: 0, width: 1920, height: 1080 } });
  }
  await b.close();
})();
