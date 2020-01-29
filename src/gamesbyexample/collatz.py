"""Collatz Sequence, by Al Sweigart al@inventwithpython.com

Generates numbers for the Collatz sequence, given a starting number.

More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
An XKCD comic about Collatz numbers is at: https://www.xkcd.com/710/"""
__version__ = 1

import sys, time

# Setup the constants:
PAUSE = 0.1

print('''Collatz Sequence, or, the 3N+1 Problem
By Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a
starting number, following two rules:

1) If the current number N is even, the next number is N / 2.
2) If the current Number N is odd, the next number is N * 3 + 1.

The sequence terminates when N becomes 1. It is generally thought,
but so far not mathematically proven, that every starting number
eventually terminates.
''')

while True:  # Main program loop.
    while True:  # Ask for a starting number.
        print('Enter a starting number (greater than 0) or QUIT:')
        response = input()
        if response.upper().startswith('Q'):
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) > 0:
            break
        print('You must enter an integer greater than 0.')
        # At this point, go back to the start of the loop.

    n = int(response)
    length = 1
    print(n, end='', flush=True)
    while n != 1:
        if n % 2 == 0:  # If n is even...
            n = n // 2
        else:  # Otherwise, n is odd...
            n = 3 * n + 1

        print(', ' + str(n), end='', flush=True)
        length += 1
        time.sleep(PAUSE)

    print()
    print('It seems that the starting number', response, 'produces a')
    print('Collatz sequence that is', length, 'numbers long.')
    print()
    # At this point, go back to the start of the main game loop.
