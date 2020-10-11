/*
Fast Draw, by Al Sweigart al@inventwithpython.com
Test your reflexes to see if you're the fastest draw in the west.
*/

'use strict';

const readlineSync = require('readline-sync');

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}


async function main() {
    console.log('Fast Draw, by Al Sweigart al@inventwithpython.com');
    console.log();
    console.log('Time to test your reflexes and see if you are the fastest');
    console.log('draw in the west!');
    console.log('When you see "DRAW", you have 0.3 seconds to press Enter.');
    console.log('But you lose if you press Enter before "DRAW" appears.');
    console.log();
    readlineSync.question('Press Enter to begin...');

    while (true) {
        console.log();
        console.log('It is high noon...');
        await sleep(Math.random() * 3 + 2);
        console.log('DRAW!');
        let drawTime = Date.now();
        readlineSync.question();  // This function call doesn't return until Enter is pressed.
        let timeElapsed = (Date.now() - drawTime) / 1000;

        if (timeElapsed < 0.01) {
            // If the player pressed Enter before DRAW! appeared, the input()
            // call returns almost instantly.
            console.log('You drew before "DRAW" appeared! You lose.');
        } else if (timeElapsed > 0.3) {
            timeElapsed = Math.trunc(timeElapsed * 10000) / 10000;
            console.log('You took', timeElapsed, 'seconds to draw. Too slow!');
        } else {
            timeElapsed = Math.trunc(timeElapsed * 10000) / 10000;
            console.log('You took', timeElapsed, 'seconds to draw.');
            console.log('You are the fastest draw in the west! You win!');
        }

        console.log('Enter QUIT to stop, or press Enter to play again.');
        let response = readlineSync.question('> ').toUpperCase();
        if (response === 'QUIT') {
            console.log('Thanks for playing!');
            return;
        }
    }
}

main();
