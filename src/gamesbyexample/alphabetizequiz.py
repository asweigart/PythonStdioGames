# Alphabetize Quiz, by Al Sweigart al@inventwithpython.com
# A time-based quiz game to see how fast you can alphabetize letters.

# EXPERIMENT! Try changing the QUESTION_SIZE and QUIZ_DURATION constants.

import random, time

# Set up the constants:
QUESTION_SIZE = 5 # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30 # The quiz lasts 30 seconds.
assert QUESTION_SIZE <= 26
assert QUIZ_DURATION > 0

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = ''.join(sorted(ALPHABET, reverse=True))


def slowPrint(text, pauseAmount):
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='') # end='' means no newline.
        time.sleep(pauseAmount) # Pause in between each letter.
    print() # Print a newline.


# Fancy animation for the title:
slowPrint(ALPHABET, 0.05)
slowPrint('    ALPHABETIZE QUIZ', 0.05)
slowPrint(REVERSE_ALPHABET, 0.05)
time.sleep(0.75)

print('''
By Al Sweigart al@inventwithpython.com

To play, enter the alphabetical order of the letters shown as fast as
possible. Try to get as many as possible in {} seconds!

Example:
    P M O T Q
    > mopqt

Press enter to start!
'''.format(QUIZ_DURATION))
input() # Let the player press Enter to start the game.

startTime = time.time() # Get the current time for the start time.
numCorrect = 0 # Number of questions answered correctly.
while True: # Main game loop.
    # Come up with QUESTION_SIZE letters for the question:
    questionLetters = random.sample(ALPHABET, QUESTION_SIZE)
    print(' '.join(questionLetters))
    print()
    response = input('> ').upper()

    # Check if the quiz's time is up:
    if time.time() - 30 > startTime:
        print("TIME'S UP!")
        break

    # Check if the response is correct:
    if list(response) == sorted(questionLetters):
        print('    Correct!\n')
        numCorrect += 1 # Increase the score by 1.
    else:
        print('    Ack. :(\n')

# After the loop exits, the quiz is over. Show the final score:
print('In {} seconds you got {} correct!'.format(QUIZ_DURATION, numCorrect))
print('Thanks for playing!')

