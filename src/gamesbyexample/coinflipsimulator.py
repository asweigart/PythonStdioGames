# Coin Flip Simulator, by Al Sweigart al@inventwithpython.com
# Simulate a large number of coin flips.
__version__ = 1

import random

print('COIN FLIP SIMULATOR')
print('By Al Sweigart al@inventwithpython.com')

# Ask the user how many flips to make:
print('How many coin flips to make?')
while True:
    response = input()
    if response.isdecimal():
        numberOfFlips = int(response)
        break
    # At this point, go back to the start of the loop.

streakStats = {} # Keys are streak lengths, values are frequency.
for i in range(numberOfFlips):
    isFirstFlip = i == 0

    # Simulate one coin flip:
    if random.randint(0, 1) == 0:
        flip = 'heads'
    else:
        flip = 'tails'
    print(flip[0], end='') # Print out "h" or "t".

    if isFirstFlip:
        currentStreakLength = 0
        currentStreakSide = flip

    # Check if we need to reset the streak:
    if flip != currentStreakSide:
        # Record the streak stats:
        streakKey = (currentStreakLength, currentStreakSide)
        streakStats.setdefault(streakKey, 0)
        streakStats[streakKey] += 1

        # Reset the streak length for this new streak:
        currentStreakLength = 1
        currentStreakSide = flip
    else:
        currentStreakLength += 1

# Record the streak stats for the final flip:
streakKey = (currentStreakLength, currentStreakSide)
streakStats.setdefault(streakKey, 0)
streakStats[streakKey] += 1

print()
print('Simulation finished.')
streakLengths = list(streakStats.keys())
streakLengths.sort()

# Display the results:
for streakLength in streakLengths:
    label = str(streakLength[0]) + ' ' + streakLength[1] + ' in a row'
    print(label.rjust(21) + ' - ' + str(streakStats[streakLength]))
