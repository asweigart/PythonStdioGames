# Peg Solitaire, by Al Sweigart al@inventwithpython.com
# A single-player, peg-jumping game to eliminate all the pegs.
# More info at https://en.wikipedia.org/wiki/Peg_solitaire

import sys

EMPTY = '.'
PEG = 'O'
NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
ALL_SPACES = 'C1 D1 E1 C2 D2 E2 A3 B3 C3 D3 E3 F3 G3 A4 B4 C4 D4 E4 F4 G4 A5 B5 C5 D5 E5 F5 G5 C6 D6 E6 C7 D7 E7'.split()

def getNewBoard():
    board = {}
    # Set every space on the board to a peg:
    for space in ALL_SPACES:
        board[space] = PEG

    # Set the center space to be empty:
    board['D4'] = EMPTY

    return board


def displayBoard(board):
    spaces = []
    for space in ALL_SPACES:
        spaces.append(board[space])

    print('''
  ABCDEFG
1   {}{}{}
2   {}{}{}
3 {}{}{}{}{}{}{}  N
4 {}{}{}{}{}{}{} W+E
5 {}{}{}{}{}{}{}  S
6   {}{}{}
7   {}{}{}
'''.format(*spaces))


def getNeighboringSpaces(space, direction):
    x, y = space # Split up `space` into the x and y coordinates.

    if direction == NORTH:
        neighborSpace = x + str(int(y) - 1) # E.g. convert y of 3 to '2'
        secondNeighborSpace = x + str(int(y) - 2) # E.g. convert y of 3 to '1'
    elif direction == SOUTH:
        neighborSpace = x + str(int(y) + 1) # E.g. convert y of 3 to '4'
        secondNeighborSpace = x + str(int(y) + 2) # E.g. convert y of 3 to '5'
    elif direction == WEST:
        neighborSpace = chr(ord(x) - 1) + y # E.g. convert 'C' to 'B'
        secondNeighborSpace = chr(ord(x) - 2) + y # E.g. convert 'C' to 'A'
    elif direction == EAST:
        neighborSpace = chr(ord(x) + 1) + y # E.g. convert 'C' to 'D'
        secondNeighborSpace = chr(ord(x) + 2) + y # E.g. convert 'C' to 'E'

    return neighborSpace, secondNeighborSpace


def canMoveInDirection(board, space, direction):
    neighborSpace, secondNeighborSpace = getNeighboringSpaces(space, direction)

    # Check if the neighboring space exists:
    if neighborSpace in ALL_SPACES:
        # Check if there is a peg in the neighboring space:
        if board[neighborSpace] == PEG:
            # Check if the neighbor's neighboring space exists:
            if secondNeighborSpace in ALL_SPACES:
                # Check if there is an empty space there:
                if board[secondNeighborSpace] == EMPTY:
                    return True
    return False


def getMoveablePegs(board):
    moveablePegs = [] # Contain a list of spaces whose peg can jump.
    for space in ALL_SPACES:
        if board[space] == EMPTY:
            continue # There's no peg here, so it's not a valid move.

        # Determine if the peg at this space can move:
        if canMoveInDirection(board, space, NORTH) or \
           canMoveInDirection(board, space, SOUTH) or \
           canMoveInDirection(board, space, WEST) or \
           canMoveInDirection(board, space, EAST):
            moveablePegs.append(space)
            continue

    return moveablePegs


def getPlayerMove(board):
    while True:
        # Ask the player to select a peg to move:
        moveablePegs = getMoveablePegs(board)

        if len(moveablePegs) == 0:
            # No pegs left to move, which means game over.
            print('You have run out of pegs to move! Game over.')
            sys.exit()

        # Let the player select which peg they want to move:
        print('Enter the peg you want to move: ' + ' '.join(moveablePegs) + ' QUIT')
        space = input().upper()

        if space == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if space in moveablePegs:
            break # If the space has a moveable peg, break out of the loop.

    # Get the possible directions that the selected peg can jump:
    possibleDirections = []
    for direction in [NORTH, SOUTH, EAST, WEST]:
        if canMoveInDirection(board, space, direction):
            possibleDirections.append(direction)

    if len(possibleDirections) == 1:
        # There is only one possible direction to jump, so select it:
        jumpDirection = possibleDirections[0]
    else:
        while True:
            # Ask the player which direction to jump:
            print('Enter the direction to jump: ' + ' '.join(possibleDirections))
            jumpDirection = input().upper()

            if jumpDirection in possibleDirections:
                break # If the jump direction is a valid move, break out of the loop.

    return (space, jumpDirection)


def makeMove(board, space, direction):
    neighborSpace, secondNeighborSpace = getNeighboringSpaces(space, direction)

    board[space] = EMPTY # Moving the peg in the space to a different space.
    board[neighborSpace] = EMPTY # Removing the jumped-over peg.
    board[secondNeighborSpace] = PEG # The moved peg lands here.


def checkIfPlayerHasWon(board):
    pegCount = 0
    for space in ALL_SPACES:
        if board[space] == PEG:
            pegCount += 1
    return pegCount == 1


print('PEG SOLITAIRE')
print('By Al Sweigart al@inventwithpython.com')
print()

theBoard = getNewBoard()

while True:
    displayBoard(theBoard)
    space, jumpDirection = getPlayerMove(theBoard)
    makeMove(theBoard, space, jumpDirection)
    if checkIfPlayerHasWon(theBoard):
        displayBoard(theBoard)
        print('You have solved the puzzle! Thanks for playing!')
        sys.exit()
