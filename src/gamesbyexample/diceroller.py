"""Dice Roller, by Al Sweigart al@inventwithpython.com
Simulates dice rolls using the Dungeons & Dragons dice roll notation.
This and other games are available at https://nostarch.com/XX
Tags: short, simulation"""
__version__ = 0
import random, sys

print('''Dice Roller, by Al Sweigart al@inventwithpython.com

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
  3d6 rolls three 6-sided dice
  1d10+2 rolls one 10-sided die, and adds 2
  2d38-1 rolls two 38-sided die, and subtracts 1
  QUIT quits the program
''')

while True:  # Main program loop:
    try:
        diceStr = input('> ')  # The prompt to enter the dice string.
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Clean up the dice string:
        diceStr = diceStr.lower().replace(' ', '')

        # Find the "d" in the dice string input:
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Get the number of dice. (The "3" in "3d6+1"):
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)

        # Find if there is a plus or minus sign for a modifier:
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Find the number of sides. (The "6" in "3d6+1"):
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        # Find the modifier amount. (The "1" in "3d6+1"):
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                # Change the modification amount to negative:
                modAmount = -modAmount

        # Simulate the dice rolls:
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Display the total:
        print(sum(rolls) + modAmount, '(', end='')

        # Display the individual rolls:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Display the modifier amount:
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        # Catch any exceptions and display the message to the user:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # Go back to the dice string prompt.
