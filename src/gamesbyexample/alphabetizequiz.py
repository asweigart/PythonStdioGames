"""Alphabetize Quiz, by Al Sweigart al@inventwithpython.com
A time-based quiz game to see how fast you can alphabetize letters.
Tags: short, game"""
__version__ = 0

import random, time

# Set up the constants:
# (!) Try changing these constants.
QUESTION_SIZE = 5  # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30  # The quiz lasts 30 seconds.
assert QUESTION_SIZE <= 26
assert QUIZ_DURATION > 0

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = ''.join(sorted(ALPHABET, reverse=True))


def main():
    # Fancy animation for the title:
    slowPrint(ALPHABET, 0.02)
    slowPrint('    Alphabetize Quiz', 0.02)
    slowPrint(REVERSE_ALPHABET, 0.02)
    time.sleep(0.5)

    print('''
By Al Sweigart al@inventwithpython.com

To play, enter the alphabetical order of the letters shown as fast
as possible. Try to get as many as possible in {} seconds!

Example:
    P M O T Q  <-- The letters.
    > mopqt    <-- Enter the correct alphabetical order.

    '''.format(QUIZ_DURATION))
    input('Press Enter to begin...')

    startTime = time.time()  # Get the current time for the start time.
    numCorrect = 0  # Number of questions answered correctly.
    while True:  # Main game loop.
        # Come up with letters for the question:
        quizLetters = random.sample(ALPHABET, QUESTION_SIZE)
        print(' '.join(quizLetters))
        print()
        response = input('> ').upper()

        # Check if the quiz's time is up:
        if time.time() - 30 > startTime:
            print("TIME'S UP!")
            break

        # Check if the response is correct:
        if list(response) == sorted(quizLetters):
            print('    Correct!\n')
            numCorrect += 1  # Increase the score by 1.
        else:
            print('    Ack. :(\n')
        # At this point, go back to the start of the main game loop.

    # After the loop exits, the quiz is over. Show the final score:
    print('In {} seconds you'.format(QUIZ_DURATION))
    print('got {} correct!'.format(numCorrect))
    print('Thanks for playing!')


def slowPrint(text, pauseAmount):
    """Slowly print out the characters in text one at a time."""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='')  # end='' means no newline.
        time.sleep(pauseAmount)  # Pause in between each letter.
    print()  # Print a newline.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
