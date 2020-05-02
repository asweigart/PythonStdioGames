"""Coin Flip Simulator, by Al Sweigart al@inventwithpython.com
Simulate a large number of coin flips.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, math, simulation"""
__version__ = 0
import random

print('Coin Flip Simulator, by Al Sweigart al@inventwithpython.com')

# Ask the user how many flips to make:
print('How many coin flips to make?')
while True:
    response = input('> ')
    if response.isdecimal():
        numberOfFlips = int(response)
        break  # Exit the loop once they enter a valid number.

# The streakStats dictionary keeps count of how many times a certain
# streak of heads or tails has occurred. The keys are tuples of
# (streakLength, side) and the values are integer counts.
streakStats = {}
for i in range(numberOfFlips):
    # Simulate one coin flip:
    if random.randint(0, 1) == 0:
        flip = 'heads'
    else:
        flip = 'tails'
    print(flip[0], end='')  # Print out "h" or "t".

    isFirstFlip = i == 0
    if isFirstFlip:
        currentStreakLength = 0
        currentStreakSide = flip

    # Check if we need to reset the streak:
    if flip != currentStreakSide:
        # Record the streak stats:
        streakKey = (currentStreakLength, currentStreakSide)
        if streakKey not in streakStats:
            # Set this new key to 0:
            streakStats[streakKey] = 0
        streakStats[streakKey] = streakStats[streakKey] + 1

        # Reset the streak length for this new streak:
        currentStreakLength = 1
        currentStreakSide = flip
    else:
        currentStreakLength = currentStreakLength + 1

# Record the streak stats for the final flip:
streakKey = (currentStreakLength, currentStreakSide)
if streakKey not in streakStats:
    streakStats[streakKey] = 0  # New streaks start at 0.
streakStats[streakKey] = streakStats[streakKey] + 1

print()
print('Simulation finished.')
streakLengthsAndSides = list(streakStats.keys())
streakLengthsAndSides.sort()

# Display the results:
for length, side in streakLengthsAndSides:
    label = str(length) + ' ' + side + ' in a row'
    print(label.rjust(21) + ' - ' + str(streakStats[(length, side)]))
