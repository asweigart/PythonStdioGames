# Bagels, a game similar to Mastermind, by Al Sweigart al@inventwithpython.com
# This game is featured in Invent Your Own Computer Games with Python from No Starch Press. https://nostarch.com/inventwithpython
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def getSecretNum(NUM_DIGITS):
    # Returns a string that is NUM_DIGITS long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)


print('BAGELS')
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:  # Main game loop.
    secretNum = getSecretNum(NUM_DIGITS)
    print('I have thought up a number. You have %s guesses to get it.' %
          (MAX_GUESSES))

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdigit():
            print('Guess #%s: ' % (numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAX_GUESSES:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    # Ask player if thye want to play again.
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
