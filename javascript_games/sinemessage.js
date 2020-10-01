/*
Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
*/

'use strict';

var readlineSync = require('readline-sync');

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// Get the size of the terminal window:
// (We can't print to the last column on Windows without it adding a
// newline automatically, so reduce the width by one.)
const WIDTH = process.stdout.columns - 1;

async function main() {
    console.log('Sine Message, by Al Sweigart al@inventwithpython.com')
    console.log('(Press Ctrl-C to quit.)')
    console.log()
    console.log('What message do you want to display? (Max', Math.floor(WIDTH / 2), 'chars.)')
    while (true) {
        var message = readlineSync.question('> ');
        if (1 <= message.length <= Math.floor(WIDTH / 2)) {
            break;
        }
        console.log('Message must be 1 to', Math.floor(WIDTH / 2), 'characters long.')
    }

    var step = 0.0;  // The "step" determines how far into the sine wave we are.
    // Sine goes from -1.0 to 1.0, so we need to change it by a multiplier:
    var multipler = (WIDTH - message.length) / 2;

    while (true) {  // Main program loop.
        var sinOfStep = Math.sin(step);
        var padding = ' '.repeat(Math.floor((sinOfStep + 1) * multipler));
        console.log(padding + message);
        await sleep(0.1);
        step += 0.25  // (!) Try changing this to 0.1 to 0.5.
    }
}

main();