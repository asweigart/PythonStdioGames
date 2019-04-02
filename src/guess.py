# A guess-the-number game, by Al Sweigart al@inventwithpython.com

import random

secretNumber = random.randint(1, 100) # Select a random number.
print('I am thinking of a number between 1 and 100.')

for i in range(10):
    print('You have ' + str(10 - i) + ' guesses left. Take a guess.')
    guess = input() # Enter the guess.
    guess = int(guess) # Convert the guess to an integer.

    if guess == secretNumber:
        break # Exit the loop if the guess is correct.

    # Offer a hint:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# Reveal the results:
if guess == secretNumber:
    print('Yay! You guessed my number!')
if guess != secretNumber:
    secretNumber = str(secretNumber) # Convert the number to a string.
    print('Game over. The number I was thinking of was ' + secretNumber)
