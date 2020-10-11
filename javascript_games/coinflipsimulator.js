/*
Coin Flip Simulator, by Al Sweigart al@inventwithpython.com
Simulate a large number of coin flips.
*/

const readlineSync = require('readline-sync');

console.log('Coin Flip Simulator, by Al Sweigart al@inventwithpython.com');

// Ask the user how many flips to make:
console.log('How many coin flips to make?');
while (true) {
    let response = readlineSync.question('> ');
    if (!isNaN(response)) {
        var numberOfFlips = Number(response);
        break  // Exit the loop once they enter a valid number.
    }
}

// The streakStats dictionary keeps count of how many times a certain
// streak of heads or tails has occurred. The keys are arrays of
// [streakLength, side] and the values are integer counts.
let streakStats = {};
for (let i = 0; i < numberOfFlips; i++) {
    // Simulate one coin flip:
    if (Math.floor(Math.random() * 2) == 0) {
        var flip = 'heads';
    } else {
        var flip = 'tails';
    }
    process.stdout.write(flip[0]);  // Print out "h" or "t".

    let isFirstFlip = (i === 0);
    if (isFirstFlip) {
        var currentStreakLength = 0;
        var currentStreakSide = flip;
    }

    // Check if we need to reset the streak:
    if (flip != currentStreakSide) {
        // Record the streak stats:
        var streakKey = [currentStreakLength, currentStreakSide];
        if (streakStats[streakKey] === undefined) {
            // Set this recorded streak to 0:
            streakStats[streakKey] = 0;
        }
        streakStats[streakKey] = streakStats[streakKey] + 1;

        // Reset the streak length for this new streak:
        currentStreakLength = 1;
        currentStreakSide = flip;
    } else {
        currentStreakLength = currentStreakLength + 1;
    }

    // Record the streak stats for the final flip:
    streakKey = [currentStreakLength, currentStreakSide];
    if (streakStats[streakKey] === undefined) {
        // Set this recorded streak to 0:
        streakStats[streakKey] = 0;
    }
    streakStats[streakKey] = streakStats[streakKey] + 1;
}

console.log();
console.log('Simulation finished.');
streakLengthsAndSides = Object.keys(streakStats);
streakLengthsAndSides.sort(); // TODO fix "10 before 2" bug

// Display the results:
for (let i = 0; i < streakLengthsAndSides.length; i++) {
    let length = streakLengthsAndSides[i].split(',')[0];
    let side = streakLengthsAndSides[i].split(',')[1];
    let label = length + ' ' + side + ' in a row';
    console.log(label.padStart(21, ' ') + ' - ' + streakStats[[length, side]]);
}
