/*
Numeral System Counters, by Al Sweigart al@inventwithpython.com
Shows equivalent numbers in decimal, hexadecimal, and binary.
*/

'use strict';

const readlineSync = require('readline-sync');

console.log(`Numeral System Counters, by Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)
`);

while (true) {
    var response = readlineSync.question('Enter the starting number (e.g. 0) > ');
    if (response === '') {
        response = '0';  // Start at 0 by default.
        break;
    }
    if (response.isdecimal()) {
        break;
    }
    console.log('Please enter a number.');
}
var start = Number(response);

while (true) {
    response = readlineSync.question('Enter how many numbers to display (e.g. 1000) > ');
    if (response === '') {
        var response = '1000';  // Display 1000 numbers by default.
        break;
    }
    if (response.isdecimal()) {
        break;
    }
    console.log('Please enter a number greater than or equal to 0.');
}
var amount = Number(response);

for (var number = start; number < start + amount; number++) {  // Main program loop.
    // Convert to hexadecimal/binary and remove the prefix:
    var hexNumber = number.toString(16).toUpperCase();
    var binNumber = number.toString(2);

    console.log('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber);
}
