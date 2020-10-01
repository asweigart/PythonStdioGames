/*
Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
A simulation of one million dice rolls.
*/

'use strict';

const readlineSync = require('readline-sync');

console.log(`Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com

Enter how many six-sided dice you want to roll:`);
var numberOfDice = Number(readlineSync.question('> '));

// Set up a dictionary to store the results of each dice roll:
var results = {};
for (var i = numberOfDice; i <= (numberOfDice * 6); i++) {
    results[i] = 0;
}

// Simulate dice rolls:
console.log('Simulating 1,000,000 rolls of', numberOfDice, 'dice...');
var lastPrintTime = Date.now();
for (var i = 0; i < 1_000_000; i++) {
    if (Date.now() > lastPrintTime + 1000) {
        console.log((Math.round(i / 1_000) / 10) + '% done...');
        lastPrintTime = Date.now();
    }

    var total = 0;
    for (var j = 0; j < numberOfDice; j++) {
        total = total + (Math.floor(Math.random() * 6) + 1);
    }
    results[total] = results[total] + 1;
}

// Display results:
console.log('TOTAL - ROLLS - PERCENTAGE');
for (var i = numberOfDice; i <= (numberOfDice * 6); i++) {
    var roll = results[i];
    var percentage = Math.round(results[i] / 1_000) / 10;
    console.log('  ' + i + ' - ' + roll + ' rolls - ' + percentage + '%');
}
