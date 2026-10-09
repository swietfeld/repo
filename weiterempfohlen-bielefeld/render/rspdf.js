// Rendert alle Folien der Präsentation als PNG für den PDF-Anhang, mit echten Symbolen statt der Platzhalter-Kreise.
// Aufruf aus dem Ordner weiterempfohlen-bielefeld: node render/rspdf.js <folie> ...  → render/pdf-<folie>.png
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const fs = require('fs');
const P = {
  Check: '<path d="M20 6 9 17l-5-5"/>',
  Clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
  Globe: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
  GraduationCap: '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
  Home: '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
  Key: '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
  Lightning: '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
  Link: '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
  Play: '<path d="m6 3 14 9-14 9V3z"/>',
  Search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
  Star: '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
  Users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
  Verified: '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  const head = fs.readFileSync(__dirname + '/head.html', 'utf8');
  for (const n of process.argv.slice(2)) {
    let s = fs.readFileSync(__dirname + '/../praesentation/project/slides/' + n + '.html', 'utf8');
    s = s.replace(/<x-icon([^>]*)name="([A-Za-z]+)"([^>]*)><\/x-icon>/g, (m, a, name, c) => {
      const st = ((a + c).match(/style="([^"]*)"/) || [, ''])[1];
      return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;${st}">${P[name] || ''}</svg>`;
    });
    fs.writeFileSync(__dirname + '/tmp_' + n + '.html', head + s + '</body></html>');
    await p.goto('file://' + __dirname + '/tmp_' + n + '.html'); await p.waitForTimeout(400);
    await p.screenshot({ path: __dirname + '/pdf-' + n + '.png', clip: { x: 0, y: 0, width: 1920, height: 1080 } });
  }
  await b.close();
})();
