"""Checkers, by Al Sweigart al@inventwithpython.com

The classic checkers board game.
In this version, capturing is not mandatory.
Tags: extra-large, board game, game, two-player"""
__version__ = 0
import copy, sys

# Set up the constants:
ALL_COLUMNS = 'ABCDEFGH'
# The columns where odd/even rows can have checkers on them.
ODD_CHECKER_COLUMNS = 'BDFH'
EVEN_CHECKER_COLUMNS = 'ACEG'
EMPTY = ' '  # The character to use for an empty space on the board.


def main():
    """Run a single game of Checkers."""
    print('''CHECKERS
    By Al Sweigart al@inventwithpython.com''')
    gameBoard = getNewBoard() # Create a new checker board.
    turn = 'O' # O goes first.
    while True: # Main game loop.
        displayBoard(gameBoard)

        # Get the player's move and carry it out:
        srcMove, dstMove = getPlayerMove(gameBoard, turn)
        if (srcMove, dstMove) == (None, None):
            break  # If no moves can be made, end this player's turn.
        gameBoard = makeMove(gameBoard, srcMove, dstMove)

        if hasLost(gameBoard, otherCheckers(turn)[1]):
            displayBoard(gameBoard)
            print(turn + ' is the winner!')
            sys.exit()
        if (srcMove, dstMove) == (None, None):
            displayBoard(gameBoard)
            print(otherCheckers(turn)[1] + ' is the winner!')
            sys.exit()
        turn = otherCheckers(turn)[1]  # Switch turns.
        # At this point, go back to the start of the main game loop.


def getNewBoard():
    """Set up a board data structure with empty spaces."""

    # Keys are spaces (like 'B1'), values are the checker or EMPTY:
    board = {}

    # Set every space to be empty:
    for row in range(1, 9):
        if row % 2 == 0:  # Set the spaces on even rows:
            for column in EVEN_CHECKER_COLUMNS:
                board[column + str(row)] = EMPTY
        elif row % 2 == 1:  # Set the spaces on odd rows:
            for column in ODD_CHECKER_COLUMNS:
                board[column + str(row)] = EMPTY

    # Place the starting pieces for player X at the top:
    for space in 'B1 D1 F1 H1 A2 C2 E2 G2 B3 D3 F3 H3'.split():
        board[space] = 'x'

    # Place the starting pieces for player O at the bottom:
    for space in 'A6 C6 E6 G6 B7 D7 F7 H7 A8 C8 E8 G8'.split():
        board[space] = 'o'

    return board


def displayBoard(board):
    """Display the board data structure on the screen."""
    spaces = []  # Contains all the characters to display at each space.
    for row in range(1, 9):
        if row % 2 == 0:
            for column in EVEN_CHECKER_COLUMNS:
                spaces.append(board[column + str(row)])
        else:
            for column in ODD_CHECKER_COLUMNS:
                spaces.append(board[column + str(row)])

    print("""
      A   B   C   D   E   F   G   H
    +---+---+---+---+---+---+---+---+
  1 |   | {} |   | {} |   | {} |   | {} | 1
    +---+---+---+---+---+---+---+---+
  2 | {} |   | {} |   | {} |   | {} |   | 2
    +---+---+---+---+---+---+---+---+
  3 |   | {} |   | {} |   | {} |   | {} | 3
    +---+---+---+---+---+---+---+---+
  4 | {} |   | {} |   | {} |   | {} |   | 4
    +---+---+---+---+---+---+---+---+
  5 |   | {} |   | {} |   | {} |   | {} | 5
    +---+---+---+---+---+---+---+---+
  6 | {} |   | {} |   | {} |   | {} |   | 6
    +---+---+---+---+---+---+---+---+
  7 |   | {} |   | {} |   | {} |   | {} | 7
    +---+---+---+---+---+---+---+---+
  8 | {} |   | {} |   | {} |   | {} |   | 8
    +---+---+---+---+---+---+---+---+
      A   B   C   D   E   F   G   H""".format(*spaces))


def prevCol(column):
    """Return the column letter that comes before column.

    Returns '' if column 'A'."""
    return {'': '', 'A': '', 'B': 'A', 'C': 'B', 'D': 'C',
            'E': 'D', 'F': 'E', 'G': 'F', 'H': 'G', '': ''}[column]


def nextCol(column):
    """Return the column letter that comes after column.

    Returns '' if column 'H'."""
    return {'': '', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E',
            'E': 'F', 'F': 'G', 'G': 'H', 'H': '', '': ''}[column]


def otherCheckers(checker):
    """Return a string of the opponent's checkers."""
    return {'x': ('o', 'O'), 'X': ('o', 'O'),
            'o': ('x', 'X'), 'O': ('x', 'X')}[checker]


def getPossibleDstMoves(board, srcSpace):
    """Get all possible destination moves from srcSpace.

    Returns a tuple of two lists. The first is a list of spaces the
    checker at srcSpace can move to, the second is a list of spaces
    the checker at srcSpace jumps to after capturing a checker."""
    assert board.get(srcSpace) != EMPTY

    checker = board[srcSpace] # The checker at srcSpace.
    possibleDstMoves = []     # Possible places the checker can move to.
    possibleDstCaptures = []  # Possible places to move after capturing.

    # Setup variables for various spaces adjacent/near srcSpace.
    column = srcSpace[0]    # Columns are letters.
    row = int(srcSpace[1])  # E.g. convert string '1' to int 1.
    downLeftSpace    = prevCol(column) + str(row + 1)
    downRightSpace   = nextCol(column) + str(row + 1)
    upLeftSpace      = prevCol(column) + str(row - 1)
    upRightSpace     = nextCol(column) + str(row - 1)
    down2Left2Space  = prevCol(prevCol(column)) + str(row + 2)
    down2Right2Space = nextCol(nextCol(column)) + str(row + 2)
    up2Left2Space    = prevCol(prevCol(column)) + str(row - 2)
    up2Right2Space   = nextCol(nextCol(column)) + str(row - 2)

    # See where the checker at this space can move:
    if checker in ('x', 'X', 'O'):  # x, X, and O can move down.
        # Check the two spaces below this x:
        if board.get(downLeftSpace) == EMPTY:
            possibleDstMoves.append(downLeftSpace)
        if board.get(downRightSpace) == EMPTY:
            possibleDstMoves.append(downRightSpace)

        # Check the two spaces below this x if you can capture an o:
        canCapDL = board.get(downLeftSpace) in otherCheckers(checker)
        if canCapDL and board.get(down2Left2Space) == EMPTY:
            possibleDstCaptures.append(down2Left2Space)
        canCapDR = board.get(downRightSpace) in otherCheckers(checker)
        if canCapDR and board.get(down2Right2Space) == EMPTY:
            possibleDstCaptures.append(down2Right2Space)

    if checker in ('o', 'X', 'O'):  # o, X, and O can move up.
        # Check the two spaces above this o:
        if board.get(upLeftSpace) == EMPTY:
            possibleDstMoves.append(upLeftSpace)
        if board.get(upRightSpace) == EMPTY:
            possibleDstMoves.append(upRightSpace)

        # Check the two spaces below this o if you can capture an x:
        canCapUL = board.get(upLeftSpace) in otherCheckers(checker)
        if canCapUL and board.get(up2Left2Space) == EMPTY:
            possibleDstCaptures.append(up2Left2Space)
        canCapUR = board.get(upRightSpace) in otherCheckers(checker)
        if canCapUR and board.get(up2Right2Space) == EMPTY:
            possibleDstCaptures.append(up2Right2Space)

    return (possibleDstMoves, possibleDstCaptures)


def getPlayerMove(board, player):
    """Ask the player to select a move."""
    assert player in ('X', 'O')

    # Get possible "source" spaces to select:
    checkersThatCanMove = []
    for row in range(1, 9):  # Loop over all the spaces on the board.
        for column in ALL_COLUMNS:
            thisSpace = column + str(row)
            checkerAtSpace = board.get(thisSpace, '')
            cantMove = checkerAtSpace.upper() != player
            if cantMove:
                continue  # This is not a checker the player can move.

            # See where the checker at this space can move:
            dstMoves, dstCaptures = getPossibleDstMoves(board, thisSpace)
            if dstMoves != [] or dstCaptures != []:
                checkersThatCanMove.append(thisSpace)

    if checkersThatCanMove == []:
        return (None, None)  # There are no valid moves.

    while True:  # Loop until a valid "source" space is selected.
        print('Player', player, 'select the checker to move:')
        print(' '.join(checkersThatCanMove), 'QUIT')
        srcMove = input('> ').upper().strip()
        if srcMove == 'QUIT':
            sys.exit()
        if srcMove in checkersThatCanMove:
            break
        # At this point, go back to the start of the loop.

    while True:  # Loop until a valid "destination" space is selected.
        dstMoves, dstCaptures = getPossibleDstMoves(board, srcMove)
        dstMoves += dstCaptures
        print('Enter the space to move', srcMove, 'to:')
        print(' '.join(dstMoves))
        dstMove = input('> ').upper().strip()
        if dstMove in dstMoves:
            break
        # At this point, go back to the start of the loop.

    return (srcMove, dstMove)


def makeMove(board, srcMove, dstMove):
    """Carry out the move and return a new board data structure."""
    board = copy.copy(board)  # We'll modify a copy of the board object.
    srcColumn, srcRow = srcMove[0], int(srcMove[1])
    dstColumn, dstRow = dstMove[0], int(dstMove[1])

    if abs(srcRow - dstRow) >= 1:
        # The checker is making a normal or jump move:
        board[dstMove] = board[srcMove]
        board[srcMove] = EMPTY
    if abs(srcRow - dstRow) == 2:
        # Erase the checker that was captured in the jump:
        if dstColumn < srcColumn and dstRow < srcRow:
            board[prevCol(srcColumn) + str(srcRow - 1)] = EMPTY
        elif dstColumn < srcColumn and dstRow > srcRow:
            board[prevCol(srcColumn) + str(srcRow + 1)] = EMPTY
        elif dstColumn > srcColumn and dstRow < srcRow:
            board[nextCol(srcColumn) + str(srcRow - 1)] = EMPTY
        elif dstColumn > srcColumn and dstRow > srcRow:
            board[nextCol(srcColumn) + str(srcRow + 1)] = EMPTY

    # See if we need to promote this checker:
    if dstRow == 1 or dstRow == 8:
        print(board[dstMove].upper(), 'has been promoted!')
        board[dstMove] = board[dstMove].upper()  # Promote this checker.

    # See if this checker can do another jump after jumping:
    dstMoves, dstCaptures = getPossibleDstMoves(board, dstMove)
    if dstCaptures != [] and abs(srcRow - dstRow) == 2:
        displayBoard(board)
        while True:  # Keep asking until valid input is entered.
            print('Enter the double jump to make:')
            print(' '.join(dstCaptures))
            doubleJumpMove = input('> ').upper().strip()
            if doubleJumpMove in dstCaptures:
                break
            # At this point, go back to the start of the loop.
        return makeMove(board, dstMove, doubleJumpMove)
    return board


def hasLost(board, player):
    """Return True if player has no checkers, otherwise False."""
    assert player in ('X', 'O')
    for row in range(1, 9):
        for column in ALL_COLUMNS:
            if board.get(column + str(row), '').upper() == player:
                return False
    return True


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
