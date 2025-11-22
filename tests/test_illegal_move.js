const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  // Enable console logging from the page
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));

  try {
    await page.goto('http://localhost:8000/frontend/index.html');
    
    // Wait for board to load
    await page.waitForSelector('#chess-board');
    await page.waitForSelector('.square');

    // Select White Pawn at (0, 1)
    const sourceSelector = '.square[data-x="0"][data-y="1"]';
    await page.waitForSelector(sourceSelector);
    
    console.log('Clicking source square (0, 1)...');
    await page.click(sourceSelector);
    
    // Wait a bit for selection to register
    await new Promise(r => setTimeout(r, 500));

    // Attempt illegal move to (0, 4) - too far for a pawn
    const targetSelector = '.square[data-x="0"][data-y="4"]';
    await page.waitForSelector(targetSelector);
    
    console.log('Clicking target square (0, 4) - Illegal move...');
    await page.click(targetSelector);

    // Monitor the source square for the 'illegal-move' class
    // We expect it to blink twice: on -> off -> on -> off
    
    const checkClass = async () => {
      return await page.$eval(sourceSelector, el => el.classList.contains('illegal-move'));
    };

    console.log('Monitoring for blink effect...');
    
    // Wait for first blink ON
    await page.waitForFunction(
      selector => document.querySelector(selector).classList.contains('illegal-move'),
      { timeout: 2000 },
      sourceSelector
    );
    console.log('First blink ON detected');

    // Verify 'selected' class IS present during animation (this is the bug we want to confirm first, then fix)
    // We want to ensure it IS NOT present for the fix.
    // So for now, let's assert that it IS NOT present, which should FAIL if the bug exists.
    const isSelected = await page.$eval(sourceSelector, el => el.classList.contains('selected'));
    if (isSelected) {
        throw new Error('FAIL: Source square still has "selected" class (yellow blink risk)');
    }
    console.log('Verified "selected" class is removed.');

    // Wait for first blink OFF
    await page.waitForFunction(
      selector => !document.querySelector(selector).classList.contains('illegal-move'),
      { timeout: 2000 },
      sourceSelector
    );
    console.log('First blink OFF detected');

    // Wait for second blink ON
    await page.waitForFunction(
      selector => document.querySelector(selector).classList.contains('illegal-move'),
      { timeout: 2000 },
      sourceSelector
    );
    console.log('Second blink ON detected');

    // Wait for second blink OFF
    await page.waitForFunction(
      selector => !document.querySelector(selector).classList.contains('illegal-move'),
      { timeout: 2000 },
      sourceSelector
    );
    console.log('Second blink OFF detected');

    console.log('TEST PASSED: Double blink detected successfully and no yellow blink.');

  } catch (error) {
    console.error('TEST FAILED:', error);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
