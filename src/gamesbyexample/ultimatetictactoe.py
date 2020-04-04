"""Ultimate Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
This and other games are available at https://nostarch.com/XX
Tags: large, game, board game, two-player"""
__version__ = 0
# TODO - Comments need updating.

import sys

# Set up the constants:
O_PLAYER = 'O'
X_PLAYER = 'X'
TIED = 'tied'
EMPTY_SPACE = '.'
BOARD_WIDTH = 3
BOARD_HEIGHT = 3
CANVAS_WIDTH = 15
CANVAS_HEIGHT = 9
SUBCANVAS_WIDTH = 5
SUBCANVAS_HEIGHT = 3

def main():
    # todo intro stuff

    turn = X_PLAYER
    gameBoard = getNewBoard()
    focusX, focusY = None, None  # The player moves on the center local board first.
    while True:  # Main game loop.
        displayBoard(gameBoard)
        focusX, focusY = getPlayerMove(turn, gameBoard, focusX, focusY)

        # Check for a global winner:
        globalBoard = makeBoardFromLocalBoards(gameBoard)
        globalWinner = getWinner(globalBoard)
        if globalWinner == TIED:
            displayBoard(gameBoard)
            print('The game is a tie!')
            print('Thanks for playing!')
            sys.exit()
        elif globalWinner != None:
            displayBoard(gameBoard)
            print(globalWinner, 'has won!')
            print('Thanks for playing!')
            sys.exit()

        # Switch to the other player's turn:
        if turn == X_PLAYER:
            turn = O_PLAYER
        elif turn == O_PLAYER:
            turn = X_PLAYER

def getNewBoard():
    board = {}  # Keys are (x, y) int tuples, values are: Dictionaries with keys of (x, y) tuples, values of X/O/Empty tiles
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = {}
            for localX in range(BOARD_WIDTH):
                for localY in range(BOARD_HEIGHT):
                    board[(x, y)][(localX, localY)] = EMPTY_SPACE
    return board


def displayBoard(board):
    canvas = {}  # Keys are (x, y) tuples, values are the character to print there.
    # First, put blank spaces on the entire canvas:
    for x in range(CANVAS_WIDTH):
        for y in range(CANVAS_HEIGHT):
            canvas[(x, y)] = ' '

    # Second, fill in the global board Xs and Os on the canvas:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            winner = getWinner(board[(x, y)])
            if winner == X_PLAYER:
                # Draw a large X on the canvas:
                canvas[(x * 5 + 1, y * 3 + 0)] = '\\'
                canvas[(x * 5 + 3, y * 3 + 0)] = '/'
                canvas[(x * 5 + 2, y * 3 + 1)] = 'X'
                canvas[(x * 5 + 1, y * 3 + 2)] = '/'
                canvas[(x * 5 + 3, y * 3 + 2)] = '\\'
            elif winner == O_PLAYER:
                # Draw a large O on the canvas:
                canvas[(x * 5 + 2, y * 3 + 0)] = '_'
                canvas[(x * 5 + 1, y * 3 + 1)] = '/'
                canvas[(x * 5 + 3, y * 3 + 1)] = '\\'
                canvas[(x * 5 + 1, y * 3 + 2)] = '\\'
                canvas[(x * 5 + 2, y * 3 + 2)] = '_'
                canvas[(x * 5 + 3, y * 3 + 2)] = '/'
            elif winner == TIED:
                # Draw a solid # block on the canvas:
                for scx in range(SUBCANVAS_WIDTH):
                    for scy in range(SUBCANVAS_HEIGHT):
                        canvas[(x * 5 + scx, y * 3 + scy)] = '#'

    # Third, fill in the Xs and Os of the local boards on the canvas:
    for ix, localTopLeftX in enumerate([0, 5, 10]):
        for iy, localTopLeftY in enumerate([0, 3, 6]):
            if getWinner(board[(ix, iy)]) != None:
                continue

            for x in range(3):
                for y in range(3):
                    canvasx = localTopLeftX + (x * 2)
                    canvasy = localTopLeftY + y
                    canvas[(canvasx, canvasy)] = board[(ix, iy)][(x, y)]

    # Print out the tic tac toe board:
    for y in range(9):
        for x in range(15):
            print(canvas[(x, y)], end='')
            if x == 4 or x == 9:
                print('|', end='')
        print()  # Print a newline.

        if y == 2 or y == 5:
            print('-----+-----+-----')


def getWinner(board):
    for i in range(9): # sanity check
        assert board[(i % 3, i // 3)] in (X_PLAYER, O_PLAYER, EMPTY_SPACE, TIED)

    topLeft  = board[(0, 0)]
    topMid   = board[(1, 0)]
    topRight = board[(2, 0)]
    midLeft  = board[(0, 1)]
    midMid   = board[(1, 1)]
    midRight = board[(2, 1)]
    botLeft  = board[(0, 2)]
    botMid   = board[(1, 2)]
    botRight = board[(2, 2)]

    for player in (X_PLAYER, O_PLAYER):
        if ((topLeft == topMid == topRight == player) or     # Top row
            (midLeft == midMid == midRight == player) or     # Middle row
            (botLeft == botMid == botRight == player) or     # Bottom row
            (topLeft == midLeft == botLeft == player) or     # Left column
            (topMid == midMid == botMid == player) or        # Midle column
            (topRight == midRight == botRight == player) or  # Right column
            (topLeft == midMid == botRight == player) or     # \ diagonal
            (topRight == midMid == botLeft == player)):       # / diagonal
            return player

    # Check for a tie:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] == EMPTY_SPACE:
                # Return None because there is no winner yet:
                return None
    return TIED


def getPlayerMove(player, board, focusX, focusY):
    # Check if the player can freely select any local board:
    if focusX == None and focusY == None:
        # Let the player pick which board they want to move on:
        print(player + ': Enter the BOARD you want to move on.')
        validBoardsToSelect = []
        for xyTuple, localBoard in board.items():
            if getWinner(localBoard) == None:
                validBoardsToSelect.append(xyTuple)
        selectedBoard = enter1Through9(validBoardsToSelect)
        focusX = selectedBoard % 3
        focusY = selectedBoard // 3

    # Select the space on the focused local board:
    localXDesc = ['left', 'middle', 'right'][focusX]
    localYDesc = ['top', 'middle', 'bottom'][focusY]
    print(player + ' moves on the ' + localYDesc + ', ' + localXDesc + ' board.')
    validSpacesToSelect = []
    for xyTuple, tile in board[(focusX, focusY)].items():
        if tile == EMPTY_SPACE:
            validSpacesToSelect.append(xyTuple)
    selectedSpace = enter1Through9(validSpacesToSelect)
    x = selectedSpace % 3
    y = selectedSpace // 3

    board[(focusX, focusY)][(x, y)] = player

    # Figure out the local board that the next player must move on:
    if getWinner(board[(x, y)]) == None:
        return (x, y)
    else:
        # Otherwise if there's a winner or it's tied, the next player can move on any local board:
        return (None, None)


def enter1Through9(validMoves):
    #breakpoint()
    for i, move in enumerate(validMoves):
        # (x, y) (0-2, 0-2) => 1-9
        # 0, 0 => 1
        # 1, 0 => 2
        # 2, 0 => 3
        # 0, 1 => 4
        validMoves[i] = str((move[1] * 3 + move[0]) + 1)  # TODO - explain this later
    #breakpoint()
    print('      1 2 3')
    print('      4 5 6')
    print('      7 8 9')
    print('Enter your move (1-9) or QUIT:')
    while True:  # Keep asking the player until they enter a valid move.
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response in validMoves:
            return int(response) - 1  # Return a int that is 0-8, not a string that is 1-9
        print('You cannot select that space.')


def makeBoardFromLocalBoards(localBoards):
    globalBoard = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            winner = getWinner(localBoards[(x, y)])
            if winner == None:
                globalBoard[(x, y)] = EMPTY_SPACE
            elif winner == TIED:
                globalBoard[(x, y)] = TIED
            elif winner in (X_PLAYER, O_PLAYER):
                globalBoard[(x, y)] = winner
    return globalBoard


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
