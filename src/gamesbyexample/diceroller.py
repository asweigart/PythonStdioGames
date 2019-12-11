# Dice Roller, by Al Sweigart al@inventwithpython.com
# Simulates dice rolls using the Dungeons & Dragons notation.
__version__ = 1

import random, sys

print('''DICE ROLLER
By Al Sweigart al@inventwithpython.com

Example input:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided dice, and adds 2
  2d17-1 rolls two 17-sided dice, and subtracts 1
  QUIT quits the program
''')

while True: # Main program loop:
    try:
        diceStr = input('> ') # The prompt to enter the dice string.
        if diceStr.upper() == 'QUIT':
            sys.exit()

        # Clean up the dice string by removing spaces, converting to lowercase:
        diceStr = diceStr.lower().replace(' ', '')

        # Find the number of dice to roll:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Get the number of dice:
        numberOfDice = diceStr[:dIndex] # The `3` in `3d6+1`.
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Find if there is a plus or minus sign:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Find the number of sides:
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1:] # The `6` in `3d6+1`.
            if not numberOfSides.isdecimal():
                raise Exception('Missing the number of sides.')
            numberOfSides = int(numberOfSides)

            modAmount = 0
        else:
            numberOfSides = diceStr[dIndex + 1:modIndex]
            if not numberOfSides.isdecimal():
                raise Exception('Missing the number of sides.')
            numberOfSides = int(numberOfSides)

            # Find the modifier amount:
            modAmount = int(diceStr[modIndex + 1:]) # The `1` in `3d6+1`.
            if diceStr[modIndex] == '+':
                pass # Do nothing if it's +.
            elif diceStr[modIndex] == '-':
                # Change the modification amount to negative:
                modAmount = -modAmount

        # Simulate the dice rolls:
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
            print(', {}{}'.format(diceStr[modIndex], abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # Catch any raised exceptions and display the message to the user:
        print('Invalid input. Enter something like `3d6` or `1d10+1`')
        print('Input was invalid because: ' + str(exc))
        continue # Go back to the dice string prompt.
    # At this point, go back to the start of the main program loop.