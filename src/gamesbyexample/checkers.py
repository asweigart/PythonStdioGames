# Checkers, by Al Sweigart al@inventwithpython.com
# The classic checkers board game.
# In this version, capturing is not mandatory.

import copy, sys

ALL_COLUMNS = 'ABCDEFGH'
# The columns where odd/even rows can have checkers on them.
ODD_CHECKER_COLUMNS = 'BDFH'
EVEN_CHECKER_COLUMNS = 'ACEG'
EMPTY = ' ' # The character to use for an empty space on the board.

def getNewBoard():
    # Set up the board data structure with empty spaces.
    board = {} # Keys of spaces like 'B1', and values of the checker or EMPTY.

    # Set every space to be empty:
    for row in range(1, 9):
        if row % 2 == 0: # Set the spaces on even rows:
            for column in EVEN_CHECKER_COLUMNS:
                board[column + str(row)] = EMPTY
        elif row % 2 == 1: # Set the spaces on odd rows:
            for column in ODD_CHECKER_COLUMNS:
                board[column + str(row)] = EMPTY

    # Place the starting pieces for player X at the top:
    for space in 'B1 D1 F1 H1 A2 C2 E2 G2 B3 D3 F3 H3'.split():
        board[space] = 'x'

    # Place the starting pieces for player O at the bottom:
    for space in 'A6 C6 E6 G6 B7 D7 F7 H7 A8 C8 E8 G8'.split():
        board[space] = 'o'

    return board

def drawBoard(board):
    spaces = [] # This contains all the characters to print at each space.
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
    # Return the column letter that comes before `column`, or '' if it's 'A'.
    return {'': '', 'A': '', 'B': 'A', 'C': 'B', 'D': 'C',
            'E': 'D', 'F': 'E', 'G': 'F', 'H': 'G', '': ''}[column]

def nextCol(column):
    # Return the column letter that comes after `column`, or '' if it's 'H'.
    return {'': '', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E',
            'E': 'F', 'F': 'G', 'G': 'H', 'H': '', '': ''}[column]

def otherCheckers(checker):
    # Return a string of the opponent's checkers.
    return {'x': ('o', 'O'), 'X': ('o', 'O'),
            'o': ('x', 'X'), 'O': ('x', 'X')}[checker]

def getPossibleDstMoves(board, srcSpace):
    # Return a list of possible destination moves from `srcSpace`.
    if board.get(srcSpace) not in ('x', 'o', 'X', 'O'):
        return [] # There are no checkers at `srcSpace`.

    checker = board[srcSpace] # The checker at `srcSpace`
    possibleDstMoves = []     # Possible places the checker can move to.
    possibleDstCaptures = []  # Possible places to move to after capturing.

    # Setup variables for various spaces adjacent/near `srcSpace`.
    column = srcSpace[0]   # Columns are letters.
    row = int(srcSpace[1]) # E.g. convert string '1' to int 1.
    downLeftSpace    = prevCol(column) + str(row + 1)
    downRightSpace   = nextCol(column) + str(row + 1)
    upLeftSpace      = prevCol(column) + str(row - 1)
    upRightSpace     = nextCol(column) + str(row - 1)
    down2Left2Space  = prevCol(prevCol(column)) + str(row + 2)
    down2Right2Space = nextCol(nextCol(column)) + str(row + 2)
    up2Left2Space    = prevCol(prevCol(column)) + str(row - 2)
    up2Right2Space   = nextCol(nextCol(column)) + str(row - 2)

    # See where the checker at this space can move:
    if checker in ('x', 'X', 'O'):
        # Check the two spaces below this x:
        if board.get(downLeftSpace) == EMPTY:
            possibleDstMoves.append(downLeftSpace)
        if board.get(downRightSpace) == EMPTY:
            possibleDstMoves.append(downRightSpace)

        # Check the two spaces below this x if you can capture an o:
        if board.get(downLeftSpace) in otherCheckers(checker) and board.get(down2Left2Space) == EMPTY:
            possibleDstCaptures.append(down2Left2Space)
        if board.get(downRightSpace) in otherCheckers(checker) and board.get(down2Right2Space) == EMPTY:
            possibleDstCaptures.append(down2Right2Space)

    if checker in ('o', 'X', 'O'):
        # Check the two spaces above this o:
        if board.get(upLeftSpace) == EMPTY:
            possibleDstMoves.append(upLeftSpace)
        if board.get(upRightSpace) == EMPTY:
            possibleDstMoves.append(upRightSpace)

        # Check the two spaces below this o if you can capture an x:
        if board.get(upLeftSpace) in otherCheckers(checker) and board.get(up2Left2Space) == EMPTY:
            possibleDstCaptures.append(up2Left2Space)
        if board.get(upRightSpace) in otherCheckers(checker) and board.get(up2Right2Space) == EMPTY:
            possibleDstCaptures.append(up2Right2Space)

    return (possibleDstMoves, possibleDstCaptures)

def getMove(board, turn):
    # Present the player with valid moves and ask them to choose one:
    assert turn in ('X', 'O')

    # Get possible "source" spaces to select:
    checkersThatCanMove = []
    for row in range(1, 9): # Loop over all the spaces on the board.
        for column in ALL_COLUMNS:
            thisSpace = column + str(row)
            isNotAnAvailableMove = board.get(thisSpace, '').upper() != turn
            if isNotAnAvailableMove:
                continue # This is not a checker the player can move.

            # See where the checker at this space can move:
            dstMoves, dstCaptures = getPossibleDstMoves(board, thisSpace)
            if dstMoves != [] or dstCaptures != []:
                checkersThatCanMove.append(thisSpace)

    if checkersThatCanMove == []:
        return (None, None) # There are no valid moves.

    while True: # Loop until a valid "source" space is selected.
        print('Player', turn, 'select the checker to move:')
        print(' '.join(checkersThatCanMove), 'QUIT')
        srcMove = input().upper()
        if srcMove == 'QUIT':
            sys.exit()
        if srcMove in checkersThatCanMove:
            break

    while True: # Loop until a valid "destination" space is selected.
        dstMoves, dstCaptures = getPossibleDstMoves(board, srcMove)
        dstMoves += dstCaptures
        print('Enter the space to move', srcMove, 'to:')
        print(' '.join(dstMoves))

        dstMove = input().upper()
        if dstMove in dstMoves:
            break

    return (srcMove, dstMove)

def makeMove(board, srcMove, dstMove):
    # Carry out the move and return a new board data structure.
    board = copy.copy(board) # We'll modify a copy of the board object.
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
        board[dstMove] = board[dstMove].upper() # Promote this checker.

    # See if this checker can do another jump after jumping:
    dstMoves, dstCaptures = getPossibleDstMoves(board, dstMove)
    if dstCaptures != [] and abs(srcRow - dstRow) == 2:
        drawBoard(board)
        while True: # Keep asking until valid input is entered.
            print('Enter the double jump to make:')
            print(' '.join(dstCaptures))
            doubleJumpMove = input().upper()
            if doubleJumpMove in dstCaptures:
                break
        return makeMove(board, dstMove, doubleJumpMove)
    return board

def hasLost(board, player):
    # Return True if `player` has no checkers on `board`, otherwise False.
    assert turn in ('X', 'O')
    for row in range(1, 9):
        for column in ALL_COLUMNS:
            if board.get(column + str(row), '').upper() == player:
                return False
    return True


# Main game code:
print('CHECKERS')
print('By Al Sweigart al@inventwithpython.com')
theBoard = getNewBoard() # Create a new checker board data structure.
turn = 'X' # X goes first.
while True: # Main game loop.
    drawBoard(theBoard)

    # Get the player's move and carry it out:
    srcMove, dstMove = getMove(theBoard, turn)
    if (srcMove, dstMove) == (None, None): # TODO - remove this?
        break # If no moves can be made, end this player's turn.
    theBoard = makeMove(theBoard, srcMove, dstMove)

    if hasLost(theBoard, otherCheckers(turn)[1]):
        drawBoard(theBoard)
        print(turn + ' is the winner!')
        sys.exit()
    if (srcMove, dstMove) == (None, None):
        drawBoard(theBoard)
        print(otherCheckers(turn)[1] + ' is the winner!')
        sys.exit()
    turn = otherCheckers(turn)[1] # Switch turns to the other player.
