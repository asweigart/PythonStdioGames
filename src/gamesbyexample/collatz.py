# Collatz Sequence, by Al Sweigart al@inventwithpython.com
# Generates numbers for the Collatz sequence, given a starting number.

# More info at: https://en.wikipedia.org/wiki/Collatz_conjecture

import sys, time
PAUSE = 0.1 # Length of pauses in between printing sequence numbers.

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

while True: # Main program loop.
    while True: # Ask for a starting number.
        print('Enter a starting number (greater than 0) or QUIT:')
        response = input()
        if response.upper().startswith('Q'):
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) > 0:
            break
        print('You must enter an integer greater than 0.')

    n = int(response)
    length = 1
    print(n, end='')
    while n != 1:
        if n % 2 == 0:  # If n is even...
            n = n // 2
        else: # Otherwise, n is odd...
            n = 3 * n + 1

        print(', ' + str(n), end='')
        length += 1
        time.sleep(PAUSE)

    print()
    print('It seems that the starting number', response, ' produces a')
    print('Collatz sequence that terminates after', length, 'numbers.')
    print()
