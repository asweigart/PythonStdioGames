/*
Deep Cave, by Al Sweigart al@inventwithpython.com
An animation of a deep cave that goes forever into the earth.
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}


// Set up the constants:
const WIDTH = 70;  // (!) Try changing this to 10 or 30.
const PAUSE_AMOUNT = 0.05;  // (!) Try changing this to 0 or 1.0.

async function main() {
    console.log('Deep Cave, by Al Sweigart al@inventwithpython.com');
    console.log('Press Ctrl-C to stop.');
    await sleep(2);

    let leftWidth = 20;
    let gapWidth = 10;

    while (true) {
        // Display the tunnel segment:
        let rightWidth = WIDTH - gapWidth - leftWidth;
        process.stdout.write('#'.repeat(leftWidth));
        process.stdout.write(' '.repeat(gapWidth));
        process.stdout.write('#'.repeat(rightWidth));
        process.stdout.write('\n');  // Print a newline.

        await sleep(PAUSE_AMOUNT);

        // Adjust the left side width:
        let diceRoll = Math.floor(Math.random() * 6) + 1;
        if (diceRoll === 1 && leftWidth > 1) {
            leftWidth = leftWidth - 1  // Decrease left side width.
        } else if (diceRoll === 2 && leftWidth + gapWidth < WIDTH - 1) {
            leftWidth = leftWidth + 1  // Increase left side width.
        }

        // Adjust the gap width:
        // (!) Try uncommenting out all of the following code:
        diceRoll = Math.floor(Math.random() * 6) + 1;
        if (diceRoll === 1 && gapWidth > 1) {
            gapWidth = gapWidth - 1;  // Decrease gap width.
        } else if (diceRoll === 2 && leftWidth + gapWidth < WIDTH - 1) {
            gapWidth = gapWidth + 1;  // Increase gap width.
        }
    }
}

main();