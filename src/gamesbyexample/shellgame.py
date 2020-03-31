"""Shell Game, by Al Sweigart al@inventwithpython.com

A random gambling game.
Tags: tiny, beginner, game"""
__version__ = 0
import random, time, sys

print('''SHELL GAME
By Al Sweigart al@inventwithpython.com

Try to find the diamond!
Press Enter to continue...''')
input()

CUPS = ['diamond', 'pocket lint', 'nothing']

while True:  # Main game loop.
    print()
    print('Shuffling the cups', end='')
    random.shuffle(CUPS)  # This happens instantly.

    # We add fake pauses to make it seem more interesting:
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print('.', end='')
    time.sleep(0.3)
    print()
    while True:
        print('Okay! Pick a cup 1-{}'.format(len(CUPS)))
        pickedCup = input('> ')
        if pickedCup.isdecimal() and 1 <= int(pickedCup) <= len(CUPS):
            break
        print('Type a number between 1 and {}.'.format(len(CUPS)))
        print()

    if CUPS[int(pickedCup) - 1] == 'diamond':
        print('You found the cup with the diamond!')
    else:
        print('Nope! You picked the cup that had {} in it.'.format(CUPS[int(pickedCup) - 1]))


    print('Would you like to play again? Y/N')
    response = input('> ').upper()
    if not response.startswith('Y'):
        print('Thanks for playing!')
        sys.exit()
    # At this point, go back to the start of the main game loop.
