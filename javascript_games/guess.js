/*
Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
*/

'use strict';

const readlineSync = require('readline-sync');

function askForGuess() {
    while (true) {
        let guess = readlineSync.question('> ');  // Enter the guess.

        if (!isNaN(guess)) {
            return Number(guess);  // Convert string guess to an integer.
        }
        console.log('Please enter a number between 1 and 100.');
    }
}

console.log('Guess the Number, by Al Sweigart al@inventwithpython.com');
console.log();
let secretNumber = Math.floor(Math.random() * 100) + 1;  // Select a random number.
console.log('I am thinking of a number between 1 and 100.');

for (let i = 0; i < 10; i++) {  // Give the player 10 guesses.
    console.log('You have', ( 10 - i), 'guesses left. Take a guess.');

    var guess = askForGuess();
    if (guess == secretNumber) {
        break;  // Break out of the for loop if the guess is correct.
    }

    // Offer a hint:
    if (guess < secretNumber) {
        console.log('Your guess is too low.');
    }
    if (guess > secretNumber) {
        console.log('Your guess is too high.');
    }
}

// Reveal the results:
if (guess == secretNumber) {
    console.log('Yay! You guessed my number!');
} else {
    console.log('Game over. The number I was thinking of was', secretNumber);
}
