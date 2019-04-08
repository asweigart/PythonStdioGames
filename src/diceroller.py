# Dice Roller, by Al Sweigart al@inventwithpython.com

"""
Be able to type 1d6+1 and have it respond.

> 3d6
7 (2, 2, 3)
> 4d10+3
12 (1, 2, 3, 3, +3)
"""

import random

print('DICE ROLLER')
print('(Enter text like `3d6` to roll three 6-sided dice, or 1d10+2 to')
print('roll one 10-sided dice and add 2. Enter `quit` to quit.)')
print()

while True: # Main program loop:
    diceStr = input('> ') # The prompt to enter the dice string.
    diceStr = diceStr.lower().replace(' ', '') # Clean up the dice string.

    try:
        # Find the number of dice to roll:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            # There is no 'd' in the dice string:
            print('Invalid input. Enter something like `3d6` or `1d10+1`')
            continue # Go back to the dice string prompt.

        numberOfDice = int(diceStr[:dIndex]) # The `3` in `3d6+1`.

        # Find if there is a plus or minus sign:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Find the number of sides:
        if modIndex == -1:
            numberOfSides = int(diceStr[dIndex + 1:]) # The `6` in `3d6+1`.
            modAmount = 0
        else:
            numberOfSides = int(diceStr[dIndex + 1:modIndex])

            # Find the modifier amount:
            modAmount = int(diceStr[modIndex + 1:]) # The `1` in `3d6+1`.
            if diceStr[modIndex] == '+':
                pass # Do nothing if it's +.
            elif diceStr[modIndex] == '-':
                modAmount = -modAmount # Change the modifier to negative.

        # Calculate the total of the dice rolls:
        rolls = []
        for i in range(numberOfDice):
            rolls.append(random.randint(1, numberOfSides))

        # Display the total:
        print(sum(rolls) + modAmount, '(', end='')

        # Display the individual rolls:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Display the modifier amount:
        if modAmount != 0:
            print(', %s%s' % (diceStr[modIndex], abs(modAmount)), end='')
        print(')')

    except:
        print('Invalid input. Enter something like `3d6` or `1d10+1`')
        continue # Go back to the dice string prompt.
