"""Barca, by Al Sweigart al@inventwithpython.com
A chess-variant where each player's mice, lions, and elephants try to
occupy the watering holes near the center of the board.

Barca was invented by Andrew Caldwell http://playbarca.com
More info at https://en.wikipedia.org/wiki/Barca_(board_game)
"""

import sys

# Set up the constants:
SQUARE_PLAYER = 'Square Player'
ROUND_PLAYER = 'Round Player'
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# The strings to display on the board:
SQUARE_MOUSE = '[Mo]'
SQUARE_LION = '[Li]'
SQUARE_ELEPHANT = '[El]'
ROUND_MOUSE = '(Mo)'
ROUND_LION = '(Li)'
ROUND_ELEPHANT = '(El)'

LAND = ' __ '
WATER = ' ~~ '

# PLAYER_PIECES[x] is a tuple of the x player's pieces:
PLAYER_PIECES = {
    SQUARE_PLAYER: (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT),
    ROUND_PLAYER: (ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT),
}
# FEARED_PIECE[x] is the piece that x is afraid of:
FEARED_PIECE = {SQUARE_MOUSE: ROUND_LION,
                SQUARE_LION: ROUND_ELEPHANT,
                SQUARE_ELEPHANT: ROUND_MOUSE,
                ROUND_MOUSE: SQUARE_LION,
                ROUND_LION: SQUARE_ELEPHANT,
                ROUND_ELEPHANT: SQUARE_MOUSE}

# Changes to x and y for moving in different directions:
UPLEFT    = (-1, -1)
UP        = (0, -1)
UPRIGHT   = (1, -1)
LEFT      = (-1, 0)
RIGHT     = (1, 0)
DOWNLEFT  = (-1, 1)
DOWN      = (0, 1)
DOWNRIGHT = (1, 1)
CARDINAL_DIRECTIONS = (UP, LEFT, RIGHT, DOWN)
DIAGONAL_DIRECTIONS = (UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT)
ALL_DIRECTIONS = CARDINAL_DIRECTIONS + DIAGONAL_DIRECTIONS

# ANIMAL_DIRECTIONS[x] is a tuple of directions that x can move:
ANIMAL_DIRECTIONS = {SQUARE_MOUSE: CARDINAL_DIRECTIONS,
                     SQUARE_LION: DIAGONAL_DIRECTIONS,
                     SQUARE_ELEPHANT: ALL_DIRECTIONS,
                     ROUND_MOUSE: CARDINAL_DIRECTIONS,
                     ROUND_LION: DIAGONAL_DIRECTIONS,
                     ROUND_ELEPHANT: ALL_DIRECTIONS}
# FEARED_ANIMAL_DIRECTIONS[x] is a tuple of directions that the piece
# that x is afraid of can move:
FEARED_ANIMAL_DIRECTIONS = {SQUARE_MOUSE: DIAGONAL_DIRECTIONS,
                            SQUARE_LION: ALL_DIRECTIONS,
                            SQUARE_ELEPHANT: CARDINAL_DIRECTIONS,
                            ROUND_MOUSE: DIAGONAL_DIRECTIONS,
                            ROUND_LION: ALL_DIRECTIONS,
                            ROUND_ELEPHANT: CARDINAL_DIRECTIONS}

EMPTY_SPACE = 'empty'
WATERING_HOLES = ((3, 3), (6, 3), (3, 6), (6, 6))


def main():
    print("""Barca, by Al Sweigart al@inventwithpython.com
Barca is a chess variant where each player has two mice (which move like
chess rooks), lions (bishops), and elephants (queens). The object of the
game is to occupy three of the four "watering hole" spaces near the
middle of the board.

Mice are afraid of lions, lions are afraid of elephants, and elephants
are afraid of mice. Afraid animals are in "check", and must move away
before other animals can move.

Barca was invented by Andrew Caldwell http://playbarca.com
""")
    input('Press Enter to begin...')

    turn = ROUND_PLAYER
    gameBoard = getNewBoard()
    while True:  # Main game loop.
        displayBoard(gameBoard)

        doPlayerMove(turn, gameBoard)
        if isWinner(turn, gameBoard):
            print(turn, 'has won!')
            sys.exit()

        # Switch turns to the next player.
        if turn == SQUARE_PLAYER:
            turn = ROUND_PLAYER
        elif turn == ROUND_PLAYER:
            turn = SQUARE_PLAYER


def getNewBoard():
    """Return a dictionary that represent the board. The keys are (x, y)
    integer tuples for positions and the values are one of the animal
    piece constants e.g. SQUARE_ELEPHANT or ROUND_LION"""
    # First, set the board to be completely empty:
    board = {}  # Keys are (x, y) int tuples, values are player pieces.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Next, place the pieces in their starting positions:
    board[(4, 0)] = board[(5, 0)] = SQUARE_ELEPHANT
    board[(3, 1)] = board[(6, 1)] = SQUARE_LION
    board[(4, 1)] = board[(5, 1)] = SQUARE_MOUSE
    board[(4, 9)] = board[(5, 9)] = ROUND_ELEPHANT
    board[(3, 8)] = board[(6, 8)] = ROUND_LION
    board[(4, 8)] = board[(5, 8)] = ROUND_MOUSE

    return board


def displayBoard(board):
    """Display the board on the screen."""
    # A list of arguments to pass to format() to fill in the board
    # template string's {}.
    spaces = []
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] == EMPTY_SPACE:
                # This space is an empty land or waterhole.
                if (x, y) in WATERING_HOLES:
                    spaces.append(WATER)
                else:
                    spaces.append(LAND)
            else:
                # This space has an animal piece on it.
                spaces.append(getAnimalStr(board, x, y))

    print("""
 +--A---B---C---D---E---F---G---H---I---J-+
 |                                        |
 1{}{}{}{}{}{}{}{}{}{}1
 |                                        |
 2{}{}{}{}{}{}{}{}{}{}2
 |                                        |
 3{}{}{}{}{}{}{}{}{}{}3
 |                                        |
 4{}{}{}{}{}{}{}{}{}{}4
 |                                        |
 5{}{}{}{}{}{}{}{}{}{}5
 |                                        |
 6{}{}{}{}{}{}{}{}{}{}6
 |                                        |
 7{}{}{}{}{}{}{}{}{}{}7
 |                                        |
 8{}{}{}{}{}{}{}{}{}{}8
 |                                        |
 9{}{}{}{}{}{}{}{}{}{}9
 |                                        |
10{}{}{}{}{}{}{}{}{}{}10
 +--A---B---C---D---E---F---G---H---I---J-+""".format(*spaces))


def getAnimalStr(board, x, y):
    """Returns the 4-character string of the animal for the piece at
    (x, y) on the board. This string will end with a ! if the piece
    is afraid of another animal on the board."""
    piece = board[(x, y)]

    for offsetX, offsetY in FEARED_ANIMAL_DIRECTIONS[piece]:
        # Check the directions of the animal this piece is afraid of:
        checkX, checkY = x, y  # Start at the piece's location.
        while True:
            # The space check moves further in the current direction:
            checkX += offsetX
            checkY += offsetY
            if not isOnBoard(checkX, checkY):
                break  # This space is off-board, so stop checking.
            if board[(checkX, checkY)] == FEARED_PIECE[piece]:
                return piece[0:-1] + '!'  # This piece is afraid.
            elif board[(checkX, checkY)] != EMPTY_SPACE:
                break  # Another animal is blocking any feared animals.
            elif board[(checkX, checkY)] == EMPTY_SPACE:
                continue  # This space is empty, so keep checking.
    return piece  # This piece is not afraid.


def isOnBoard(x, y):
    """Returns True if (x, y) is a position on the board, otherwise
    returns False."""
    return (0 <= x < BOARD_WIDTH) and (0 <= y < BOARD_HEIGHT)


def doPlayerMove(player, board):
    """Ask the player for their move, and if it is valid, carry it out
    on the board."""
    validMoves = getPieceMovements(player, board)
    assert len(validMoves) > 0

    validMovesInA1 = []
    for x, y in validMoves.keys():
        validMovesInA1.append(xyToA1(x, y))
    print(player + ', select piece to move (or QUIT):', ', '.join(validMovesInA1))
    while True:
        # Keep asking the player until they select a valid piece:
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response in validMovesInA1:
            moveFrom = A1ToXy(response)
            break  # Player has selected a valid piece.
        print('Please select one of the given pieces.')

    moveToInA1 = []
    for x, y in validMoves[moveFrom]:
        moveToInA1.append(xyToA1(x, y))
    moveFromStr = getAnimalStr(board, moveFrom[0], moveFrom[1])
    print('Select where to move this {}: {}'.format(moveFromStr, ', '.join(moveToInA1)))
    while True:
        # Keep asking the player until they select a valid move:
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response in moveToInA1:
            moveTo = A1ToXy(response)
            break  # Player has selected a valid space to move to.
        print('Please select one of the given spaces.')

    # Carry out the player's move:
    movePiece(moveFrom, moveTo, board)


def movePiece(moveFrom, moveTo, board):
    """Move the piece at moveFrom on the board to moveTo. These are
    (x, y) integer tuples."""
    board[moveTo] = board[moveFrom]  # Place a piece at "move to".
    board[moveFrom] = EMPTY_SPACE  # Blank the original location.


def getPieceMovements(player, board):
    """Return a list of (x, y) tuples representing spaces that hold
    pieces that the player can move according to Barca rules. """

    # Figure out which pieces can move (afraid ones must move first).
    afraidPiecePositions = []  # List of (x, y) tuples of pieces.
    unafraidPiecePositions = []  # List of (x, y) tuples of pieces.
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] in PLAYER_PIECES[player]:
                # Check if the animal is afraid or not:
                if getAnimalStr(board, x, y).endswith('!'):
                    afraidPiecePositions.append((x, y))
                else:
                    unafraidPiecePositions.append((x, y))

    if len(afraidPiecePositions) != 0:
        # Unafraid pieces can't move if there are afraid pieces.
        unafraidPiecePositions = []

    # Go through all of the pieces and get their valid moves:

    # The keys are (x, y) tuples, values are list of (x, y) tuples of
    # where they can move:
    validMoves = {}
    for piecePosition in afraidPiecePositions + unafraidPiecePositions:
        x, y = piecePosition
        piece = board[(x, y)]
        # This list will contain this piece's valid move locations:
        validMoves[(x, y)] = []
        # Check the cardinal directions to see where this mouse can move:
        for offsetX, offsetY in ANIMAL_DIRECTIONS[piece]:
            checkX, checkY = x, y  # Start at the piece's location.
            while True:
                # The space check moves further in the current direction:
                checkX += offsetX
                checkY += offsetY
                if not isOnBoard(checkX, checkY) or board[(checkX, checkY)] != EMPTY_SPACE:
                    # This space is off-board or blocked by another
                    # animal, so stop checking.
                    break
                elif board[(checkX, checkY)] == EMPTY_SPACE:
                    validMoves[(x, y)].append((checkX, checkY))

    # Remove the possible moves that would end up putting the piece into
    # a feared position:
    for piecePosition, possibleMoves in validMoves.items():
        x, y = piecePosition
        piece = board[(x, y)]

        # List of (x, y) tuples where this piece doesn't want to move:
        fearedPositions = []
        for moveToX, moveToY in possibleMoves:
            # Simulate what would happen if we move the piece to
            # moveToX, moveToY:
            movePiece(piecePosition, (moveToX, moveToY), board)
            if getAnimalStr(board, moveToX, moveToY).endswith('!'):
                # Moving here would make the piece afraid, so don't let
                # it move here:
                fearedPositions.append((moveToX, moveToY))
            # Move the piece back to the original space:
            movePiece((moveToX, moveToY), piecePosition, board)
        if len(possibleMoves) != len(fearedPositions):
            # Some of the moves will make this piece afraid, so remove
            # those from the possible moves. (If all of the moves were
            # feared, then the piece isn't restricted at all.)
            for fearedX, fearedY in fearedPositions:
                validMoves[piecePosition].remove((fearedX, fearedY))
    return validMoves


def xyToA1(x, y):
    """Convert (x, y) coordinates (like 0,0 or 1,4) to user-friendly
    coordinates (like A1 or B5)."""
    return chr(x + 65) + str(y + 1)  # The ASCII value of 'A' is 65.


def A1ToXy(space):
    """Convert user-friendly coordinates (like A1 or B5) to (x, y)
    coordinates (like 0,0 or 1,4)."""
    column = space[0]
    row = space[1:]
      # The ASCII value of 'A' is 65:
    return (ord(column) - 65, int(row) - 1)


def isWinner(player, board):
    """Return True if the player occupies three of the four watering
    holes on this board."""
    squareClaims = 0
    roundClaims = 0
    for space in WATERING_HOLES:
        if board[space] in (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT):
            squareClaims += 1
        elif board[space] in (ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT):
            roundClaims += 1

    if player == SQUARE_PLAYER and squareClaims >= 3:
        return True
    elif player == ROUND_PLAYER and roundClaims >= 3:
        return True
    else:
        return False


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
