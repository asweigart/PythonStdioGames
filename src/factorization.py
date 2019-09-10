# Factorization, by Al Sweigart al@inventwithpython.com

# TODO - polish this source code

import math, sys

print('Factorization')
print('by Al Sweigart al@inventwithpython.com')
print()

while True:
    print()
    print('Enter a number larger than zero to factor (or "quit" to quit):')
    response = input()
    if response.lower() == 'quit':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of `number`:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0: # If there's no remainder, it is a factor.
            factors.append(i)
            factors.append(number // i)

    factors = list(set(factors))
    factors.sort()

    # Display the results:
    for i, factor in enumerate(factors):
        factors[i] = str(factor)

    print(', '.join(factors))