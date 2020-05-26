"""Guess the Number, by Al Sweigart al@inventwithpython.com
Try to guess the secret number based on hints.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, game"""
__version__ = 0
import random


def askForGuess():
    while True:
        guess = input('> ')  # Enter the guess.

        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer.
        print('Please enter a number.')


print('Guess the Number, by Al Sweigart al@inventwithpython.com')
print()
secretNumber = random.randint(1, 100)  # Select a random number.
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # Give the player 10 guesses.
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = askForGuess()
    if guess == secretNumber:
        break  # Break out of the for loop if the guess is correct.

    # Offer a hint:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# Reveal the results:
if guess == secretNumber:
    print('Yay! You guessed my number!')
if guess != secretNumber:
    print('Game over. The number I was thinking of was', secretNumber)
