# Multiplicative Persistence, by Al Sweigart al@inventwithpython.com
# For more information about this topic, see https://youtu.be/Wim9WJeDTHQ

import time, sys

while True:
    print('Try to get the longest multiplicative persistence chain possible!')
    print('(Try 277777788888899, which has the longest known chain length.')
    print('Enter a number (or "quit" to quit):')
    while True:
        try:
            number = input()
            if number.lower().startswith('q'):
                sys.exit()
        except ValueError:
            continue # If the user entered a non-integer, ask again.
        break

    originalNumber = number
    chainLength = 0
    while len(str(number)) > 1:
        chainLength += 1
        print(number, end='', flush=True)
        time.sleep(0.2)
        print(' -> ', end='', flush=True)
        time.sleep(0.2)
        print('*'.join(list(str(number))), end='', flush=True)
        time.sleep(0.2)
        print(' =')
        time.sleep(0.6)

        # Calculate the next number in the multiplicative persistence chain by
        # multiplying all of the digits in the number.
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product

    print(number)
    print('Length of', originalNumber, 'chain:', chainLength)
    print()


