/*
Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
*/

'use strict';

const readlineSync = require('readline-sync');
const clipboardy = require('clipboardy');

// Every possible symbol that can be encrypted/decrypted:
// (!) You can add numbers and punctuation marks to encrypt those
// symbols as well.
const SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

console.log('Caesar Cipher, by Al Sweigart al@inventwithpython.com');
console.log('The Caesar cipher encrypts letters by shifting them over by a');
console.log('key number. For example, a key of 2 means the letter A is');
console.log('encrypted into C, the letter B encrypted into D, and so on.');
console.log();

// Let the user enter if they are encrypting or decrypting:
while (true) {  // Keep asking until the user enters e or d.
    console.log('Do you want to (e)ncrypt or (d)ecrypt?');
    var response = readlineSync.question('> ').toLowerCase();
    if (response.startsWith('e')) {
        var mode = 'encrypt';
        break;
    } else if (response.startsWith('d')) {
        var mode = 'decrypt';
        break;
    }
    console.log('Please enter the letter e or d.');
}

// Let the user enter the key to use:
while (true) {  // Keep asking until the user enters a valid key.
    const maxKey = SYMBOLS.length - 1;
    console.log('Please enter the key (0 to ' + maxKey + ') to use.');
    var response = readlineSync.question('> ').toUpperCase();
    if (isNaN(response)) {
        continue;
    }

    if (0 <= Number(response) < SYMBOLS.length) {
        var key = Number(response);
        break;
    }
}

// Let the user enter the message to encrypt/decrypt:
console.log('Enter the message to ' + mode + '.');
var message = readlineSync.question('> ');

// Caesar cipher only works on uppercase letters:
message = message.toUpperCase();

// Stores the encrypted/decrypted form of the message:
var translated = '';

// Encrypt/decrypt each symbol in the message:
for (const symbol of message) {
    if (SYMBOLS.includes(symbol)) {
        // Get the encrypted (or decrypted) number for this symbol.
        var num = SYMBOLS.indexOf(symbol)  // Get the number of the symbol.
        if (mode === 'encrypt') {
            num = num + key;
        } else if (mode === 'decrypt') {
            num = num - key;
        }

        // Handle the wrap-around if num is larger than the length of
        // SYMBOLS or less than 0:
        if (num >= SYMBOLS.length) {
            num = num - SYMBOLS.length;
        } else if (num < 0) {
            num = num + SYMBOLS.length;
        }

        // Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num];
    } else {
        // Just add the symbol without encrypting/decrypting:
        translated = translated + symbol;
    }
}

// Display the encrypted/decrypted string to the screen:
console.log(translated);

clipboardy.writeSync(translated);
console.log('Full ' + mode + 'ed text copied to clipboard.');
