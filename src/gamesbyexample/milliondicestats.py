# Million Dice Roll Stats, by Al Sweigart al@inventwithpython.com
# A simulation of one million dice rolls.

import random, time

print('''MILLION DICE ROLL STATISTICS SIMULATOR
By Al Sweigart al@inventwithpython.com

Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input())

# Set up dictionary to store results:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls.
print('Simulating 1,000,000 dice rolls...')
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print('{}% done...'.format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rolls - {}%'.format(i, roll, percentage))
