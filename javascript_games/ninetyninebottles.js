/*
Ninety-Nine Bottles of Milk on the Wall
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop.
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

const PAUSE = 2;  // (!) Try changing this to 0 to see the full song at once.

console.log('Ninety-Nine Bottles, by Al Sweigart al@inventwithpython.com');
console.log();
console.log('(Press Ctrl-C to quit.)');

async function main() {
    await sleep(2);

    var bottles = 99;  // This is the starting number of bottles.
    while (bottles > 1) {
        console.log(bottles, 'bottles of milk on the wall,');
        await sleep(PAUSE);  // Pause for PAUSE number of seconds.
        console.log(bottles, 'bottles of milk,');
        await sleep(PAUSE);
        console.log('Take one down, pass it around,');
        await sleep(PAUSE);
        bottles = bottles - 1;  // Decrease the number of bottles by one.
        console.log(bottles, 'bottles of milk on the wall!');
        await sleep(PAUSE);
        console.log()  // Print a newline.
    }

    // Display the last stanza:
    console.log('1 bottle of milk on the wall,');
    await sleep(PAUSE);
    console.log('1 bottle of milk,');
    await sleep(PAUSE);
    console.log('Take it down, pass it around,');
    await sleep(PAUSE);
    console.log('No more bottles of milk on the wall!');
}

main();
