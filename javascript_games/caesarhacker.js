/*
Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
*/

'use strict';

const readlineSync = require('readline-sync');

console.log('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com');

// Let the user specify the message to hack:
console.log('Enter the encrypted Caesar cipher message to hack.');
let message = readlineSync.question('> ');

// Every possible symbol that can be encrypted/decrypted:
// (This must match the SYMBOLS used when encrypting the message.)
const SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for (let key = 0; key < SYMBOLS.length; key++) {  // Loop through every possible key.
    let translated = '';

    // Decrypt each symbol in the message:
    for (const symbol of message) {
        if (SYMBOLS.includes(symbol)) {
            let num = SYMBOLS.indexOf(symbol);  // Get the number of the symbol.
            num = num - key;  // Decrypt the number.

            // Handle the wrap-around if num is less than 0:
            if (num < 0) {
                num = num + SYMBOLS.length;
            }

            // Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num];
        } else {
            // Just add the symbol without decrypting:
            translated = translated + symbol;
        }
    }

    // Display the key being tested, along with its decrypted text:
    console.log('Key #' + key + ': ' + translated);
}