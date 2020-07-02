"""Ultimate Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
Instead of a board with 9 spaces, this game has 9 boards with 81 spaces,
the winner of each board placing their X or O on the big board!
More info at: https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe
This and other games are available at https://nostarch.com/XX
Tags: large, board game, game, two-player"""
__version__ = 0
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
    print('''Ultimate Tic-Tac-Toe, by Al Sweigart al@inventwithpython.com
Instead of tic-tac-toe with 9 spaces, this game has a "big" board
made up of 9 "small" tic-tac-toe boards. Moving on a small board causes
the next player to move on that relative board. Winning on a small board
lets that player put their mark on the big board. The winner must get
three in a row on the big board.
''')

    turn = X_PLAYER  # X will go first.
    gameBoard = getNewBoard()

    # focusX and focusY determine which small board the player moves on.
    # If they are both None, the player can choose a small board.
    focusX, focusY = None, None
    while True:  # Main game loop.
        displayBoard(gameBoard)
        focusX, focusY = askForPlayerMove(turn, gameBoard, focusX, focusY)

        # Check for a big board winner:
        bigBoard = makeBoardFromSmallBoards(gameBoard)
        bigWinner = getWinner(bigBoard)
        if bigWinner == TIED:
            displayBoard(gameBoard)
            print('The game is a tie!')
            print('Thanks for playing!')
            sys.exit()
        elif bigWinner != None:
            displayBoard(gameBoard)
            print(bigWinner, 'has won!')
            print('Thanks for playing!')
            sys.exit()

        # Switch to the other player's turn:
        if turn == X_PLAYER:
            turn = O_PLAYER
        elif turn == O_PLAYER:
            turn = X_PLAYER


def getNewBoard():
    """Returns a dictionary that represents the big tic-tac-toe board.
    Keys are (x, y) int tuples that span from 0 to 2, the values are
    dictonaries that represent small tic-tac-toe boards. These
    dictionaries have (x, y) int tuples as well, and their values are
    either X_PLAYER, O_PLAYER, or EMPTY_SPACE."""
    board = {}
    # Loop over each small board:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = {}
            # Loop over each space on the small board:
            for smallX in range(BOARD_WIDTH):
                for smallY in range(BOARD_HEIGHT):
                    board[(x, y)][(smallX, smallY)] = EMPTY_SPACE
    return board


def displayBoard(board):
    """Displays the big tic-tac-toe board on the screen."""
    # The canvas is a dictionary that has keys of (x, y) tuples, and
    # the values are the character to print at that place on the screen.
    canvas = {}
    # First, put blank spaces on the entire canvas:
    for x in range(CANVAS_WIDTH):
        for y in range(CANVAS_HEIGHT):
            canvas[(x, y)] = ' '

    # Second, fill in the big board Xs and Os on the canvas:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            winner = getWinner(board[(x, y)])
            if winner == X_PLAYER:
                # Draw a large X for each small board X won:
                canvas[(x * 5 + 1, y * 3 + 0)] = '\\'
                canvas[(x * 5 + 3, y * 3 + 0)] = '/'
                canvas[(x * 5 + 2, y * 3 + 1)] = 'X'
                canvas[(x * 5 + 1, y * 3 + 2)] = '/'
                canvas[(x * 5 + 3, y * 3 + 2)] = '\\'
            elif winner == O_PLAYER:
                # Draw a large O for each small board O won:
                canvas[(x * 5 + 2, y * 3 + 0)] = '_'
                canvas[(x * 5 + 1, y * 3 + 1)] = '/'
                canvas[(x * 5 + 3, y * 3 + 1)] = '\\'
                canvas[(x * 5 + 1, y * 3 + 2)] = '\\'
                canvas[(x * 5 + 2, y * 3 + 2)] = '_'
                canvas[(x * 5 + 3, y * 3 + 2)] = '/'
            elif winner == TIED:
                # Draw a large ### block for tied small boards:
                for scx in range(SUBCANVAS_WIDTH):
                    for scy in range(SUBCANVAS_HEIGHT):
                        canvas[(x * 5 + scx, y * 3 + scy)] = '#'

    # Third, fill in the Xs and Os of the small boards on the canvas:
    for ix, smallTopLeftX in enumerate([0, 5, 10]):
        for iy, smallTopLeftY in enumerate([0, 3, 6]):
            if getWinner(board[(ix, iy)]) != None:
                continue

            for x in range(3):
                for y in range(3):
                    canvasx = smallTopLeftX + (x * 2)
                    canvasy = smallTopLeftY + y
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
    """Return X_PLAYER, O_PLAYER, or TIED depending on who won. Return
    None if there is no winner and the board isn't full yet."""

    # Create short-named variables for the spaces on this board.
    topL, topM, topR = board[(0, 0)], board[(1, 0)], board[(2, 0)]
    midL, midM, midR = board[(0, 1)], board[(1, 1)], board[(2, 1)]
    botL, botM, botR = board[(0, 2)], board[(1, 2)], board[(2, 2)]

    for player in (X_PLAYER, O_PLAYER):
        if ((topL == topM == topR == player) or  # Top row
            (midL == midM == midR == player) or  # Middle row
            (botL == botM == botR == player) or  # Bottom row
            (topL == midL == botL == player) or  # Left column
            (topM == midM == botM == player) or  # Middle column
            (topR == midR == botR == player) or  # Right column
            (topL == midM == botR == player) or  # \ diagonal
            (topR == midM == botL == player)):   # / diagonal
            return player

    # Check for a tie:
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] == EMPTY_SPACE:
                return None  # Return None since there is no winner yet.
    return TIED


def askForPlayerMove(player, board, focusX, focusY):
    """Asks the player which space on which small board to move on.
    The focusX and focusY values determine which small board the player
    can move on, but if they are both None the player can freely choose
    a small board. Returns the (x, y) of the small board the next player
    plays on.
    """
    # Check if the player can freely select any small board:
    if focusX == None and focusY == None:
        # Let the player pick which board they want to move on:
        print(player + ': Enter the BOARD you want to move on.')
        validBoardsToSelect = []
        for xyTuple, smallBoard in board.items():
            if getWinner(smallBoard) == None:
                validBoardsToSelect.append(xyTuple)
        selectedBoard = enter1Through9(validBoardsToSelect)
        focusX = selectedBoard % 3
        focusY = selectedBoard // 3

    # Select the space on the focused small board:
    smallXDesc = ['left', 'middle', 'right'][focusX]
    smallYDesc = ['top', 'middle', 'bottom'][focusY]
    print(player, 'moves on the', smallYDesc, smallXDesc, 'board.')
    validSpacesToSelect = []
    for xyTuple, tile in board[(focusX, focusY)].items():
        if tile == EMPTY_SPACE:
            validSpacesToSelect.append(xyTuple)
    selectedSpace = enter1Through9(validSpacesToSelect)
    x = selectedSpace % 3
    y = selectedSpace // 3

    board[(focusX, focusY)][(x, y)] = player

    # Figure out the small board that the next player must move on:
    if getWinner(board[(x, y)]) == None:
        return (x, y)
    else:
        # If the small board has a winner or is tied, the next player
        # can move on any small board:
        return (None, None)


def enter1Through9(validMoves):
    """Presents a "minimap" of a tic-tac-toe board's spaces, labeled
    with numbers 1 through 9. Returns the numeric space they chose.
    Valid moves is a list of (x, y) tuples representing the spaces
    the player can pick, e.g. [(0, 0), (0, 2)] means the player can
    only pick the top two corner spaces."""
    for i, move in enumerate(validMoves):
        # Convert the (x, y) tuple values to an integer 1 through 9:
        validMoves[i] = str((move[1] * 3 + move[0]) + 1)
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
            # Return a int that is 0-8, not a string that is 1-9.
            return int(response) - 1
        print('You cannot select that space.')


def makeBoardFromSmallBoards(smallBoards):
    bigBoard = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            winner = getWinner(smallBoards[(x, y)])
            if winner == None:
                bigBoard[(x, y)] = EMPTY_SPACE
            elif winner == TIED:
                bigBoard[(x, y)] = TIED
            elif winner in (X_PLAYER, O_PLAYER):
                bigBoard[(x, y)] = winner
    return bigBoard


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
