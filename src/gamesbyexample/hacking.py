"""Hacking Minigame, by Al Sweigart al@inventwithpython.com
The hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.
This and other games are available at https://nostarch.com/XX
Tags: large, game, artistic, puzzle game"""
__version__ = 0
# NOTE: This program requires the sevenletterwords.txt file, you can
# download it from https://inventwithpython.com/sevenletterwords.txt

import random, sys

# Set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # The "computer memory" is just cosmetic, but it looks cool:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Start at 4 tries remaining, going down:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))


def getWords():
    """Return a list of 12 words that could possibly be the password.

    The secret password will be the first word in the list.
    To make the game fair, we want to only have at most 2 words that
    have 0 letters in common with the secret password."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two more words; these have zero matching letters.
    # We use "< 3" because the secret password is already in words.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break  # Found 5 words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)

    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
            break  # Found 7 or more words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)

    # Add any random words needed to get 12 words total.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


def getOneWordExcept(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def numMatchingLetters(word1, word2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def getComputerMemoryString(words):
    """Return a string representing the "computer memory"."""

    # Pick one line per word to contain a word. There are 16 lines, but
    # they are split into two halves.
    linesWithWords = random.sample(range(16 * 2), len(words))
    # The starting memory address (this is also cosmetic).
    memoryAddress = 16 * random.randint(0, 4000)

    # Create the "computer memory" string.
    computerMemory = []  # Will contain 16 strings, one for each line.
    nextWord = 0  # The index in words of the word to put into a line.
    for lineNum in range(16):  # The "computer memory" has 16 lines.
        # Create a half line of garbage characters:
        leftHalf = ''
        rightHalf = ''
        for j in range(16):  # Each half line has 16 characters.
            leftHalf += random.choice(GARBAGE_CHARS)
            rightHalf += random.choice(GARBAGE_CHARS)

        # Fill in the password from words:
        if lineNum in linesWithWords:
            # Find a random place in the half line to insert the word:
            insertionIndex = random.randint(0, 9)
            # Insert the word:
            leftHalf = (leftHalf[:insertionIndex] + words[nextWord]
                + leftHalf[insertionIndex + 7:])
            nextWord += 1  # Update the word to put in the half line.
        if lineNum + 16 in linesWithWords:
            # Find a random place in the half line to insert the word:
            insertionIndex = random.randint(0, 9)
            # Insert the word:
            rightHalf = (rightHalf[:insertionIndex] + words[nextWord]
                + rightHalf[insertionIndex + 7:])
            nextWord += 1  # Update the word to put in the half line.

        computerMemory.append('0x' + hex(memoryAddress)[2:].zfill(4)
                     + '  ' + leftHalf + '    '
                     + '0x' + hex(memoryAddress + (16*16))[2:].zfill(4)
                     + '  ' + rightHalf)

        memoryAddress += 16  # Jump from, say, 0xe680 to 0xe690.

    # Each string in the computerMemory list is joined into one large
    # string to return:
    return '\n'.join(computerMemory)


def askForPlayerGuess(words, tries):
    """Let the player enter a password guess."""
    while True:
        print('Enter password: ({} tries remaining)'.format(tries))
        guess = input('> ').upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
