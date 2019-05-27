# Coin Flip Simulator by Al Sweigart, al@inventwithpython.com

import random

print('Coin Flip Simulator')
print('Simulates coin flips and records the length of streaks.')

# Ask the user how many flips to make:
print('How many coin flips to make?')
while True:
    numberOfFlips = input()
    if numberOfFlips.isdecimal():
        numberOfFlips = int(numberOfFlips)
        break

print('Flipping a coin %s times...' % (numberOfFlips))
print('Press Enter to begin...')
input()

streakStats = {} # Keys are streak lengths, values are frequency.
currentStreakLength = 0
currentStreakSide = ''

for i in range(numberOfFlips):
    # Simulate one coin flip:
    if random.randint(0, 1) == 0:
        flip = 'h' # heads
    else:
        flip = 't' # tails
    print(flip, end='')

    # Check if we need to reset the streak:
    if flip != currentStreakSide:
        if currentStreakLength != 0:
            # Record the streak stats:
            streakStats.setdefault(currentStreakLength, 0)
            streakStats[currentStreakLength] += 1
        currentStreakLength = 1
        currentStreakSide = flip
    else:
        currentStreakLength += 1

# Record the final streak:
streakStats.setdefault(currentStreakLength, 0)
streakStats[currentStreakLength] += 1

print()
print('Simulation finished.')
streakLengths = list(streakStats.keys())
streakLengths.sort()

# Display results:
print('Streak   Number of')
print('Length - Occurences')
for streakLength in streakLengths:
    print(str(streakLength).rjust(6) + ' - ' + str(streakStats[streakLength]))
