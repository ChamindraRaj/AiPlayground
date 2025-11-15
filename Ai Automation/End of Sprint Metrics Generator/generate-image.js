const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1240, height: 670 });
  const filePath = path.resolve(__dirname, 'index.html');
  await page.goto(`file://${filePath}`);
  
  await page.waitForSelector('#capture');
  const element = await page.$('#capture');
  await element.screenshot({ path: 'Program Metrics.png' });

  await browser.close();
})();
