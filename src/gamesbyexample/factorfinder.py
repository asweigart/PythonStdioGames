"""Factorization, by Al Sweigart al@inventwithpython.com

Finds all the factors of a number.
Tags: tiny, math"""
__version__ = 0
import math, sys

print('''FACTOR FINDER
By Al Sweigart al@inventwithpython.com''')

while True:  # Main program loop.
    print()
    print('Enter a number to factor (or "QUIT" to quit):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:  # If there's no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)

    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)

    print(', '.join(factors))
    # At this point, go back to the start of the loop.
