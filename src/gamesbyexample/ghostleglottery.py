"""Ghost Leg Lottery, by Al Sweigart al@inventwithpython.com

Follow the trail to see who wins!
More info at: https://en.wikipedia.org/wiki/Ghost_Leg
Tags: large, artistic"""
__version__ = 0

import random, time, sys

# Set up the constants:
VERTICAL_POLE  = chr(9474) # Character 9474 is '│'
HORIZONTAL_LEG = chr(9472) # Character 9472 is '─'
START_LEG      = chr(9500) # Character 9500 is '├'
END_LEG        = chr(9508) # Character 9508 is '┤'

# Random number of rows because if we only have two players, the
# results would always be the same.
NUMBER_OF_ROWS = random.randint(10, 11)
LEG_WIDTH = 10
MAX_NUMBER_OF_PLAYERS = 6

# NOTE: The vertical lines are called "poles", the horizontal lines are
# called "legs".


def main():
    """Run a single game of Ghost Leg Lottery."""
    print('''GHOST LEG LOTTERY
By Al Sweigart al@inventwithpython.com
''')
    players = getPlayerNames()
    legs = getLegs(players)

    placings = []  # Index 0 is 1st place, index 1 is 2nd place, etc.
    for i in range(len(players)):
        placings.append(None)

    displayGhostLegs(legs, players, None, 0)
    displayPlacings(placings)
    time.sleep(2)

    for i in range(len(players)):
        for j in range(NUMBER_OF_ROWS + 1):
            placement = displayGhostLegs(legs, players, i, j)
            if placement == None:
                displayPlacings(placings)
                time.sleep(0.2)

        playerName = players[i]
        placings[placement] = playerName
        displayPlacings(placings)
        time.sleep(1)

    print()  # Print a newline.
    print(placings[0], 'is the winner!', placings[-1], 'came in last.')


def getPlayerNames():
    """Ask how many players there are."""
    while True:  # Keep asking until the player enters a number.
        print('How many players are there? Max:', MAX_NUMBER_OF_PLAYERS)
        response = input()
        if response.isdecimal():
            numPlayers = int(response)
            if 1 < numPlayers <= MAX_NUMBER_OF_PLAYERS:
                break
        print('Enter a number between 2 and', MAX_NUMBER_OF_PLAYERS)
        # At this point, go back to the start of the loop.

    # Enter the names of each player:
    playerNames = []  # List of the string player names.
    for i in range(1, numPlayers + 1):
        while True:  # Keep asking until the player enters a valid name.
            print('Enter player #' + str(i) + "'s name:")
            name = input()
            if len(name) == 0:
                print('Please enter a name.')
            elif name in playerNames:
                print('Choose a name that has not already been used.')
            else:
                break  # The entered name is acceptable.
            # At this point, go back to the start of the loop.

        playerNames.append(name)
    return playerNames


def getLegs(players):
    """Returns a list of which poles contain legs."""
    # Seed with every pole so that each pole has at least one swap:
    legs = list(range(len(players) - 1))
    for i in range(NUMBER_OF_ROWS - len(legs)):
        while True:
            # Decide where the row between two legs goes:
            # (Make sure that two legs don't appear one after another on
            # the same pole.)
            randomLeg = random.randint(0, len(players) - 2)

            # If there are no previous legs, go with this random leg.
            if legs == []:
                break

            # If there are only two players, ignore the "can't have two
            # of the same poles in a row" rule:
            if legs == [] or (randomLeg != legs[-1] or len(players) == 2):
                break
        legs.append(randomLeg)
    random.shuffle(legs)  # Shuffle the order of the legs.
    return legs


def displayPlacings(placings):
    """Display who has come in what place."""
    for i, playerName in enumerate(placings):
        if playerName == None:
            print('    ', i + 1, '-')
        else:
            print('    ', i + 1, '-', playerName)


def displayGhostLegs(legs, playerNames, pathPole, drawPathToRow):
    """Display all of the legs and any current paths on them."""
    # Clear the screen by printing several newlines:
    print('\n' * 30)

    # Display the player names across the top:
    for name in playerNames:
        name = name[:LEG_WIDTH]
        print(name.ljust(LEG_WIDTH + 1), end='')
    print()  # Print a newline.

    # Display the top layer of poles, which will have no legs:
    displayLeglessRow(playerNames, pathPole)

    # Display the poles and legs:
    for currentRow in range(len(legs)):
        poleWithLegOnCurrentRow = legs[currentRow]

        if drawPathToRow == currentRow:
            pathPole = None  # Stop drawing the path, just draw poles/legs.

        for currentPole in range(len(playerNames)):
            poleToTheLeftOfCurrentPole = currentPole - 1
            poleToTheRightOfCurrentPole = currentPole + 1

            if (currentPole == poleWithLegOnCurrentRow) and (currentPole == pathPole):
                # Print path on the current pole and on the leg:
                # 'V>>>>>>>>>>'
                print('V', end='')
                print('>' * LEG_WIDTH, end='')
            elif (currentPole == poleWithLegOnCurrentRow) and (poleToTheRightOfCurrentPole == pathPole):
                # 'V<<<<<<<<<<'
                print('V', end='')
                print('<' * LEG_WIDTH, end='')
            elif currentPole == poleWithLegOnCurrentRow:
                # Print a HORIZONTAL_LEG leg coming from the path:
                # '├──────────''
                print(START_LEG, end='')
                print(HORIZONTAL_LEG * LEG_WIDTH, end='')
            elif (poleToTheLeftOfCurrentPole == poleWithLegOnCurrentRow) and (currentPole == pathPole or poleToTheLeftOfCurrentPole == pathPole):
                # Print path on the current pole, and no leg:
                # 'V          '
                print('V', end='')
                print(' ' * LEG_WIDTH, end='')
            elif poleToTheLeftOfCurrentPole == poleWithLegOnCurrentRow:
                # Print the right end of a HORIZONTAL_LEG leg:
                # '┤          '
                print(END_LEG, end='')
                print(' ' * LEG_WIDTH, end='')
            elif currentPole == pathPole:
                # 'V          '
                print('V', end='')
                print(' ' * LEG_WIDTH, end='')
            else:
                # Print an empty space:
                # '│          '
                print(VERTICAL_POLE, end='')
                print(' ' * LEG_WIDTH, end='')

        # Swap path.
        if pathPole != None:
            if poleWithLegOnCurrentRow == pathPole:
                pathPole += 1
            elif poleWithLegOnCurrentRow == pathPole - 1:
                pathPole -= 1

        print()  # Print a newline.

    # Display the bottom layer of poles, which will have no legs:
    displayLeglessRow(playerNames, pathPole)

    # Display the places at the bottom:
    for i in range(1, len(playerNames) + 1):
        print(str(i) + (' ' * LEG_WIDTH), end='')
    print()  # Print a newline.

    print()  # Print a newline.
    return pathPole


def displayLeglessRow(playerNames, pathPole):
    """Display a row that contains just the poles and no legs."""
    for currentPole in range(len(playerNames)):
        if currentPole == pathPole:
            print('V', end='')
        else:
            print(VERTICAL_POLE, end='')
        print(' ' * LEG_WIDTH, end='')
    print()  # Print a newline.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
