# Guess the Number, by Al Sweigart al@inventwithpython.com
# While given hints, try to guess the secret number.

# A version of this game is featured in the book, "Invent Your Own
# Computer Games with Python. https://nostarch.com/inventwithpython

import random

print('GUESS THE NUMBER')
print('By Al Sweigart al@inventwithpython.com')
print()

secretNumber = random.randint(1, 100) # Select a random number.
print('I am thinking of a number between 1 and 100.')

for i in range(10): # Give the player 10 guesses.
    print('You have ' + str(10 - i) + ' guesses left. Take a guess.')
    while True:
        try:
            guess = int(input()) # Enter the guess.
            break # Break out of the while loop.
        except:
            print('Please enter a number.')

    if guess == secretNumber:
        break # Break out of the for loop if the guess is correct.

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
