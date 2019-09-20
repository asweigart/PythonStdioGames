# Alphabetize Quiz, by Al Sweigart al@inventwithpython.com

import random, time

# Setup the constants:
QUESTION_SIZE = 5 # Each question shows 5 letters to alphabetize.
QUIZ_DURATION = 30 # The quiz lasts 30 seconds.
assert QUESTION_SIZE <= 26
assert QUIZ_DURATION > 0

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'


def slowPrint(text, pauseAmount):
    for character in text:
        print(character, flush=True, end='')
        time.sleep(pauseAmount)
    print() # Print a newline.


# Fancy animation for the title:
slowPrint(ALPHABET, 0.05)
slowPrint('Alphabetize Quiz', 0.05)
slowPrint(REVERSE_ALPHABET, 0.05)

print('''
By Al Sweigart al@inventwithpython.com

To play, enter the alphabetical order of the letters shown as fast as
possible. Try to get as many as possible in 30 seconds!

Example:
    P M O T Q

    > mopqt

Press enter to start!
''')
input() # Let the player press Enter to start the game.


startTime = time.time() # Get the current time for the start time.
numCorrect = 0 # Number of questions answered correctly.
while True: # Main game loop.
    # Come up with QUESTION_SIZE letters to display:
    questionLetters = random.sample(ALPHABET, QUESTION_SIZE)
    print(' '.join(questionLetters))
    print()
    response = input('> ').upper()

    # Check if the quiz's time is up.
    if time.time() - 30 > startTime:
        print("TIME'S UP!")
        break

    # Check if the response is correct:
    if sorted(response) == sorted(questionLetters):
        print('    Correct!\n')
        numCorrect += 1
    else:
        print('    Ack. :(\n')

# After the loop exits, the quiz is over. Show the final score:
print(f'In {QUIZ_DURATION} you got {numCorrect} correct!')
print('Thanks for playing!')

