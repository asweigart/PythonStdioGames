# Shell Game, by Al Sweigart al@inventwithpython.com

import random, time, sys

print('SHELL GAME')
print('By Al Sweigart al@inventwithpython.com')
print()
print('Try to find the diamond!')
print('Press Enter to continue...')
input()

CUPS = ['diamond', 'pocket lint', 'nothing']

while True:
    print()
    print('Shuffling the cups', end='')
    random.shuffle(CUPS) # This happens instantly.

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
        print(f'Okay! Pick a cup 1-{len(CUPS)}')
        pickedCup = input()
        if pickedCup.isdecimal() and 1 <= int(pickedCup) <= len(CUPS):
            break
        print(f'Type a number between 1 and {len(CUPS)}.')
        print()

    if CUPS[int(pickedCup) - 1] == 'diamond':
        print('You found the cup with the diamond!')
    else:
        print(f'Nope! You picked the cup that had {CUPS[int(pickedCup) - 1]} in it.')


    print('Would you like to play again? Y/N')
    response = input().upper()
    if not response.startswith('Y'):
        print('Thanks for playing!')
        sys.exit()
