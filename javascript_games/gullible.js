/*
Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hours. (This is a joke program.)
*/

'use strict';

const readlineSync = require('readline-sync');

console.log('Gullible, by Al Sweigart al@inventwithpython.com');

while (true) {  // Main program loop.
    console.log('Do you want to know how to keep a gullible person busy for hours?');
    let response = readlineSync.question('> ');  // Get the user's response.
    if (response.toLowerCase() === 'no' || response.toLowerCase() === 'n') {
        break;  // If "no", break out of this loop.
    }
    if (response.toLowerCase() === 'yes' || response.toLowerCase() === 'y') {
        continue;  // If "yes", continue to the start of this loop.
    }
    process.stdout.write('"');
    process.stdout.write(response);
    process.stdout.write('" is not a valid yes/no response.\n');
}

console.log('Thank you. Have a nice day!');
