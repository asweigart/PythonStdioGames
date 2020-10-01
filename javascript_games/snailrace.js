/*
Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
*/

var readlineSync = require('readline-sync');

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// Set up the constants:
const MAX_NUM_SNAILS = 8;
const MAX_NAME_LENGTH = 20;
const FINISH_LINE = 40;  // (!) Try modifying this number.


async function main() {
    console.log('Snail Race, by Al Sweigart al@inventwithpython.com\n\n    @v <-- snail\n\n');

    // Ask how many snails to race:
    while (true) {
        console.log('How many snails will race? Max:', MAX_NUM_SNAILS);
        response = readlineSync.question('> ');
        if (!isNaN(response)) {
            var numSnailsRacing = Number(response);
            if (1 < numSnailsRacing <= MAX_NUM_SNAILS) {
                break;
            }
        }
        console.log('Enter a number between 2 and', MAX_NUM_SNAILS);
    }

    // Enter the names of each snail:
    var snailNames = [];  // Array of the string snail names.
    for (var i = 1; i <= numSnailsRacing; i++) {
        while (true) {  // Keep asking until the player enters a valid name.
            console.log('Enter snail #' + i.toString() + "'s name:");
            var name = readlineSync.question('> ');
            if (name.length === 0) {
                console.log('Please enter a name.');
            }
            else if (snailNames.includes(name)) {
                console.log('Choose a name that has not already been used.');
            }
            else {
                break;  // The entered name is acceptable.
            }
        }
        snailNames.push(name);
    }

    // Display each snail at the start line.
    console.log('\n'.repeat(40));
    console.log('START' + ' '.repeat(FINISH_LINE - 'START'.length) + 'FINISH');
    console.log('|' + (' '.repeat(FINISH_LINE - '|'.length)) + '|');
    var snailProgress = {};
    for (var i = 0; i < snailNames.length; i++) {
        var snailName = snailNames[i];
        console.log(snailName.substr(0, MAX_NAME_LENGTH));
        console.log('@v');
        snailProgress[snailName] = 0;
    }

    await sleep(1.5);  // The pause right before the race starts.

    while (true) {  // Main program loop.
        // Pick random snails to move forward:
        var numSnailsToMove = Math.floor(Math.random() * Math.floor(numSnailsRacing / 2)) + 1;
        for (var i = 0; i < numSnailsToMove; i++) {
            var randomSnailName = snailNames[Math.floor(Math.random() * snailNames.length)];
            snailProgress[randomSnailName] += 1;

            // Check if a snail has reached the finish line:
            if (snailProgress[randomSnailName] == FINISH_LINE) {
                console.log(randomSnailName, 'has won!');
                return;
            }
        }

        // (!) Add a cheat here that increases a snail's progress
        // if it has your name.

        await sleep(0.5);  // (!) Try changing this value.

        // (!) What happens if you comment this line out?
        console.log('\n'.repeat(40));

        // Display the start and finish lines:
        console.log('START' + ' '.repeat(FINISH_LINE - 'START'.length) + 'FINISH');
        console.log('|' + (' '.repeat(FINISH_LINE - '|'.length)) + '|');

        // Display the snails (with name tags):
        for (var i = 0; i < snailNames.length; i++) {
            var snailName = snailNames[i];
            var spaces = snailProgress[snailName];
            console.log(' '.repeat(spaces) + snailName.substr(0, MAX_NAME_LENGTH));
            console.log('.'.repeat(snailProgress[snailName]) + '@v');
        }
    }
}

main();
