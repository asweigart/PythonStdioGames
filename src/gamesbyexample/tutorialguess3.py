"""Tutorial: Guess the Number, by Al Sweigart al@inventwithpython.com

Part 3 of a tutorial to make a "Guess the Number" game, bit by bit."""

# Try copying the code in this program on your own and running the
# program before moving on to part 4. (You don't have to copy the
# comments.)


import random

secretNumber = random.randint(1, 20)


print('Hello! What is your name?')
playerName = input()
print('It is good to meet you, ' + playerName)

print('I am thinking of a number from 1 to 20.')
print('Take a guess.')
guess = input()

print('My secret number was', secretNumber)

if guess == str(secretNumber):
    print('You guessed my number!')
else:
    print('You did not guess my number. Better luck next time.')
