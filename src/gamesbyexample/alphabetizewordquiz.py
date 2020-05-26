"""Alphabetize Word Quiz, by Al Sweigart al@inventwithpython.com
A time-based quiz game to see how fast you can alphabetize words.
This and other games are available at https://nostarch.com/XX
Tags: short, game, word"""
__version__ = 0
import random, time

# Set up the constants:
# (!) Try changing these constants.
QUESTION_SIZE = 3 # Each question shows 3 words to alphabetize.
WORD_RANGE = 50 # How closely grouped the selected words are.
QUIZ_DURATION = 30 # The quiz lasts 30 seconds.
assert QUIZ_DURATION > 0

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = ''.join(sorted(ALPHABET, reverse=True))

# Read in the words from the word file.
# This file can be downloaded from:
# https://inventwithpython.com/commonenglishwords.txt
with open('commonenglishwords.txt') as wordFile:
    allWords = wordFile.read().splitlines()


def main():
    # Fancy animation for the title:
    slowPrint(ALPHABET, 0.02)
    slowPrint('  Alphabetize Word Quiz', 0.02)
    slowPrint(REVERSE_ALPHABET, 0.02)
    time.sleep(0.5)

    print('''
    By Al Sweigart al@inventwithpython.com

    To play, enter the alphabetical order of the words shown as fast as
    possible. Try to get as many as possible in {} seconds!

    Example:
        trade tracks transmit  <-- The 1st, 2nd and 3rd word.
        1     2      3         <-- Word numbers.
        > 213                  <-- Enter the alphabetical order.

    '''.format(QUIZ_DURATION))
    input('Press Enter to begin...')

    startTime = time.time() # Get the current time for the start time.
    numCorrect = 0 # Number of questions answered correctly.
    while True: # Main game loop.
        # Come up with QUESTION_SIZE words for the question:
        #questionLetters = random.sample(ALPHABET, QUESTION_SIZE)
        wordRange = random.randint(0, len(allWords) - WORD_RANGE)
        possibleWords = allWords[wordRange:wordRange + WORD_RANGE]
        quizWords = random.sample(possibleWords, QUESTION_SIZE)
        random.shuffle(quizWords) # Randomize the order of the words.

        print('   ', ' '.join(quizWords)) # Print the words.

        # Print the number labels:
        print('    ', end='')
        for i, word in enumerate(quizWords):
            print(i + 1, end='')
            print(' ' * (len(word)), end='')
        print() # Print a newline.

        response = input('> ').replace(' ', '') # Remove any spaces.

        # Check if the quiz's time is up:
        if time.time() - 30 > startTime:
            print("TIME'S UP!")
            break

        # Check if the response is correct:
        isCorrect = True
        for i, number in enumerate(response):
            if quizWords[int(number) - 1] != sorted(quizWords)[i]:
                isCorrect = False

        if isCorrect:
            print('    Correct!\n')
            numCorrect += 1 # Increase the score by 1.
        else:
            print('    Ack. :(\n')

        # After the loop exits, the quiz is over. Show the final score:
        print('In {} seconds you'.format(QUIZ_DURATION))
        print('got {} correct!'.format(numCorrect))
        print('Thanks for playing!')


def slowPrint(text, pauseAmount=0.1):
    """Slowly print out the characters in text one at a time."""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='')  # end='' means no newline.
        time.sleep(pauseAmount)  # Pause in between each character.
    print()  # Print a newline.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
