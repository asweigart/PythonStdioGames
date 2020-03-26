"""Multiplicative Persistence, by Al Sweigart al@inventwithpython.com

A fun math challenge.

For more information about this topic, see https://youtu.be/Wim9WJeDTHQ
Tags: tiny, math"""
__version__ = 0

import time, sys

print('''MULTIPLICATIVE PERSISTENCE
By Al Sweigart al@inventwithpython.com
''')

while True:  # Main program loop.
    print('Try to get the longest multiplicative persistence chain!')
    print('(Start with 277777788888899, which has the longest known')
    print('chain length.)')
    while True:  # Keep asking until the player enters a number.
        print('Enter a number (or "QUIT" to quit):')
        try:
            response = input('> ')
            if response.upper().startswith('Q'):
                sys.exit()
            number = int(response)
        except ValueError:
            continue  # If the user entered a non-integer, ask again.
        break

    chainLength = 0
    while number > 9:  # Loop as long as number is 2 or more digits.
        chainLength += 1
        print(number, end='', flush=True)
        time.sleep(0.2)
        print(' -> ', end='', flush=True)
        time.sleep(0.2)
        print('*'.join(list(str(number))), end='', flush=True)
        time.sleep(0.2)
        print(' = ', end='', flush=True)
        time.sleep(0.2)

        # Calculate the next number in the multiplicative persistence
        # chain by multiplying all of the digits in the number:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

        print(number, flush=True)
        time.sleep(0.6)
        # At this point, go back to the start of the loop.

    print(number)
    print('Length of', response, 'chain:', chainLength)
    print()
    # At this point, go back to the start of the main program loop.
