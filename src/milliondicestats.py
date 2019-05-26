# Million Dice Roll Stats, by Al Sweigart al@inventwithpython.com

import random

print('Million Dice Roll Statistics Simulator')
print()
print('Enter how many six-sided dice you want to roll:')
numberOfDice = int(input())

# Set up dictionary to store results:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls.
print('Simulating 1,000,000 dice rolls...')
for i in range(1000000):
    if i % 10000 == 0 and i != 0:
        print('{}% done...'.format(i / 10000))

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results:
print('Results:')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    print('  %s - %s rolls - %s%%' % (i, results[i], round(results[i] / 10000, 1)))
