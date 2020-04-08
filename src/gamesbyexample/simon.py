"""Simon, by Al Sweigart al@inventwithpython.com
A pattern-matching game with sounds. Try to memorize an increasingly
longer and longer pattern of letters.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, game"""
__version__ = 0
import random, sys, time

try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    sys.exit()

# Set up the constants:
BEEPS = {'A': 'sound0.wav', 'S': 'sound1.wav',
         'D': 'sound2.wav', 'F': 'sound3.wav'}

print('''Simon, by Al Sweigart al@inventwithpython.com
Try to memorize a pattern of A S D F letters (each with its own beep)
as it gets longer and longer.''')

input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)  # Clear the screen by printing many newlines.

    # Add a random letter to the pattern:
    pattern = pattern + random.choice('ASDF')

    # Display the pattern (and play their beeps):
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound(BEEPS[letter])

    time.sleep(1)  # Add a slight pause at the end.
    print('\n' * 60)  # Clear the screen by printing many newlines.

    # Let the player enter the pattern:
    print('Enter the pattern:')
    response = input('> ').upper()

    if response != pattern:
        print('Incorrect!')
        print('The pattern was', pattern)
    else:
        print('Correct!')

    for letter in pattern:
        playsound.playsound(BEEPS[letter])

    if response != pattern:
        print('You scored', len(pattern) - 1, 'points.')
        print('Thanks for playing!')
        break

    time.sleep(1)
