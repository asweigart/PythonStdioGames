"""Sonar Treasure Hunt, by Al Sweigart al@inventwithpython.com
Try to locate treasure chests hidden under the waves.
This and other games are available at https://nostarch.com/XX
Tags: large, game"""
__version__ = 0
# A version of this game is featured in the book, "Invent Your Own
# Computer Games with Python" https://nostarch.com/inventwithpython

import random
import sys
import math

# Set up the constants:
BOARD_WIDTH = 60
BOARD_HEIGHT = 15

def getNewBoard():
    """Returns a dictionary representing the board. The keys are (x, y)
    tuples and the values are '~' and '.' strings to represent waves."""
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            # Add wave characters to the board:
            if random.randint(0, 1) == 0:
                board[(x, y)] = '~'
            else:
                board[(x, y)] = '.'
    return board

def displayBoard(board):
    """Displays the board on the screen."""
    tensDigitsLine = '    ' # Indentation for the number labels.
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows.
    for row in range(BOARD_HEIGHT):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # Create the string for this row on the board.
        boardRow = ''
        for column in range(BOARD_WIDTH):
            boardRow += board[(column, row)]

        print('{}{} {} {}'.format(extraSpace, row, boardRow, row))

    # Print the numbers across the bottom of the board.
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    """Return a list of (x, y) integer tuples that represent treasure
    chest locations."""
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, BOARD_WIDTH - 1),
                    random.randint(0, BOARD_HEIGHT - 1)]
        # Make sure a chest is not already there:
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    """Returns True if (x, y) is on the board, otherwise False."""
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    """Change the board data structure with a sonar device character.
    Remove treasure chests from the chests list as they are found.
    Return False if this is an invalid move. Otherwise, return the
    string of the result of this move."""
    smallestDistance = 100  # Any chest will be closer than 100.
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distance < smallestDistance:  # Use the closest chest.
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[(x, y)] = str(smallestDistance)
            return 'Treasure detected at a distance of {} from the sonar device.'.format(smallestDistance)
        else:
            board[(x, y)] = 'X'
            return 'Sonar did not detect anything. All treasure chests out of range.'

def getPlayerMove(previousMoves):
    """Returns an (x, y) tuple of the player's move."""
    print('Where do you want to drop the next sonar device?')
    print('(0-59 0-14 or enter QUIT)')
    while True:
        move = input('> ')
        if move.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdecimal() and move[1].isdecimal() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('You already moved there.')
                continue
            return (int(move[0]), int(move[1]))

        print('Enter a number from 0 to 59, a space, then a number')
        print('from 0 to 14.')

def showInstructions():
    """Display the game instructions."""
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current
mission is to use sonar devices to find 3 sunken treasure chests at the
bottom of the ocean. But your sonar only finds distance, not direction.

Enter the coordinates to drop a sonar device. The ocean map will be
marked with how far away the nearest chest is, or an X if it is beyond
the sonar device's range. For example, the C marks are where chests are.
The sonar device shows a 3 because the closest chest is 3 spaces away.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~.~...~.~..~~~..~.~~..~~~..~.~ 0
        1 ~.~.~..~~.~...~~~...~~.~.~~~.~~~~ 1
        2 .~.C..3.~~~~.C.~~~~.....~~..~~~.. 2
        3 ........~~~.....~~~.~.....~.~..~. 3
        4 ~.~~~~.~~.~~.C.~..~~.~~~.~...~..~ 4

          012345678901234567890123456789012
                    1         2         3
(In the real game, the chests are not visible in the ocean.)

Press Enter to continue...''')
    input()

    print('''When you drop a sonar device directly on a chest, you
retrieve it. The other sonar devices update to show the distance to the
next nearest chest. The chests are beyond the range of the sonar device
on the left, so it shows an X.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~.~...~.~..~~~..~.~~..~~~..~.~ 0
        1 ~.~.~..~~.~...~~~...~~.~.~~~.~~~~ 1
        2 .~.X..7.~~~~.C.~~~~.....~~..~~~.. 2
        3 ........~~~.....~~~.~.....~.~..~. 3
        4 ~.~~~~.~~.~~.C.~..~~.~~~.~...~..~ 4

          012345678901234567890123456789012
                    1         2         3

The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9 spaces. Try to collect all 3 chests before
running out of sonar devices. Good luck!

Press enter to continue...''')
    input()


print('Sonar, by Al Sweigart al@inventwithpython.com')
print()
print('Would you like to view the instructions? (yes/no)')
if input('> ').lower().startswith('y'):
    showInstructions()

while True:
    # Game setup
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    displayBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # Show sonar device and chest statuses.
        print('You have {} sonar device(s) left. {} treasure chest(s) remaining.'.format(sonarDevices, len(theChests)))

        x, y = getPlayerMove(previousMoves)
        # We must track all moves so that sonar devices can be updated:
        previousMoves.append([x, y])

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You have found a sunken treasure chest!':
                # Update all the sonar devices currently on the map.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            displayBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('We\'ve run out of sonar devices! Now we have to head')
        print('home with treasure chests still out there! Game over.')
        print('    The remaining chests were here:')
        for x, y in theChests:
            print('    {}, {}'.format(x, y))

    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
        sys.exit()