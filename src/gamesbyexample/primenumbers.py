"""Prime Numbers, by Al Sweigart al@inventwithpython.com
Calculates prime numbers, which are numbers that are only evenly
divisible by one and themselves. They are used in a variety of practical
applications.
More info at: https://en.wikipedia.org/wiki/Prime_number
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, math, scrolling"""

import math, sys

def main():
    print('Prime Numbers, by Al Sweigart al@inventwithpython.com')
    print('Prime numbers are numbers that are only evenly divisible by')
    print('one and themselves. They are used in a variety of practical')
    print('applications, but cannot be predicted. They must be')
    print('calculated one at a time.')
    print()
    while True:
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break

    input('Press Ctrl-C at any time to quit. Press Enter to begin...')

    while True:
        # Print out any prime numbers:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
        num = num + 1  # Go to the next number.


def isPrime(number):
    """Returns True if number is prime, otherwise returns False."""
    # Handle special cases:
    if number < 2:
        return False
    elif number == 2:
        return True

    # Try to evenly divide number by all numbers from 2 up to number's
    # square root.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
