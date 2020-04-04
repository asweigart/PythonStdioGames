"""Shell Game, by Al Sweigart al@inventwithpython.com
A random gambling game.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, game"""
__version__ = 0
import random, time, sys

print('Shell Game, by Al Sweigart al@inventwithpython.com')
print()
print('I will hide a diamond in one of three cups.')
print('Try to find the diamond!')
input('Press Enter to begin...')

# This list has the contents of the cups:
CUPS = ['diamond', 'a peanut', 'nothing']

while True:  # Main game loop.
    print()
    print('Shuffling the cups...')
    random.shuffle(CUPS)  # This changes the order of the items in CUPS.

    # We add fake pauses to make it seem more interesting:
    time.sleep(0.5)
    print('  shuffle...')
    time.sleep(0.5)
    print('    shuffle...')
    time.sleep(0.5)
    print('      shuffle...')
    time.sleep(0.5)
    print('        shuffle...')
    time.sleep(0.5)
    print('          shuffle...')
    time.sleep(0.5)
    print()
    while True:  # Keep asking until the player enters a cup number.
        print('Okay! Pick a cup 1, 2, or 3')
        pickedCup = input('> ')
        if pickedCup.isdecimal() and 1 <= int(pickedCup) <= 3:
            break
        print('Type a number between 1 and 3.')
        print()

    if CUPS[int(pickedCup) - 1] == 'diamond':
        print('You found the cup with the diamond!')
    else:
        print('Nope! You picked a cup that had {} in it.'.format(CUPS[int(pickedCup) - 1]))


    print('Would you like to play again? Y/N')
    response = input('> ').upper()
    if not response.startswith('Y'):
        print('Thanks for playing!')
        sys.exit()
