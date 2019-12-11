# Hangman with Random Letters, by Al Sweigart al@inventwithpython.com
# A completely unfair word-guessing game. (This is a joke program.)
__version__ = 1

import random

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]
CATEGORY = 'Random'


def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # Show the previously guessed letters:
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # Show the secret word with spaces in between each letter:
    for letter in blanks:
        print(letter, end=' ')

    print()


def getPlayerGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure the
    player entered a single letter they haven't guessed before."""
    while True: # Keep asking until the player enters a valid letter.
        print('Guess a letter.')
        guess = input()
        guess = guess.upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Please enter a LETTER.')
        else:
            return guess


print('''HANGMAN WITH RANDOM LETTERS
By Al Sweigart al@inventwithpython.com
''')

# Setup variables for a new game:
missedLetters = []
correctLetters = []

secretWord = ''
for i in range(random.randint(4, 9)): # The secret word has 4 to 9 letters.
    secretWord += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


while True: # Main game loop.
    drawHangman(missedLetters, correctLetters, secretWord)

    # Let the player enter their letter guess:
    guess = getPlayerGuess(missedLetters + correctLetters)

    if guess in secretWord:
        # The player has guessed correctly:
        correctLetters.append(guess)

        # Check if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            break
    else:
        # The player has guessed incorrectly:
        missedLetters.append(guess)

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            drawHangman(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!')
            print('The word was "{}"'.format(secretWord))
            break
    # At this point, go back to the start of the main game loop.
