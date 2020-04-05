"""Cho-Han, by Al Sweigart al@inventwtihpython.com
The traditional Japanese dice game of even-odd.
Tags: short, beginner, game"""
__version__ = 0

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor.
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            purse = purse - pot  # Detect the pot from player's purse.
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('the dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    if ((dice1 + dice2) % 2 == 0) and (bet == 'CHO'):
        playerWon = True
    elif ((dice1 + dice2) % 2 == 1) and (bet == 'HAN'):
        playerWon = True
    elif ((dice1 + dice2) % 2 == 0) and (bet == 'HAN'):
        playerWon = False
    elif ((dice1 + dice2) % 2 == 1) and (bet == 'CHO'):
        playerWon = False

    if playerWon:
        print('You won! You take', pot * 2, 'mon.')
        purse = purse + (pot * 2)
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)  # The house fee is 10%.
    else:
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
