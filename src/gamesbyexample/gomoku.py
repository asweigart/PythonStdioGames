"""Gomoku, by Al Sweigart al@inventwithpython.com
Gomoku is a Japanese board game where two players take turns placing
down tiles. The first player to place five tiles in a row horizontally,
vertically, or diagonally wins.
More info at: https://en.wikipedia.org/wiki/Gomoku
This and other games are available at https://nostarch.com/XX
Tags: large, game, board game, two-player"""

import sys

# Set up the constants:
X_PLAYER = 'x'  # (!) Try changing this to another letter.
O_PLAYER = 'o'  # (!) Try changing this to another letter.
EMPTY_SPACE = '.'  # (!) Try changing this to another letter.
BOARD_WIDTH = 15  # (!) Try changing this to another integer.
BOARD_HEIGHT = 15  # (!) Try changing this to another integer.

# Let's make sure the board isn't too large to fit on the screen:
assert BOARD_WIDTH < 100
assert BOARD_HEIGHT < 100


def main():
    print('''Gomoku, by Al Sweigart al@inventwithpython.com

Gomoku is a Japanese board game where two players take turns placing
down tiles. The first player to place five tiles in a row horizontally,
vertically, or diagonally wins.''')

    turn = O_PLAYER  # O will go first.
    gameBoard = getNewBoard()
    while True:
        displayBoard(gameBoard)
        playerMoveX, playerMoveY = getPlayerMove(turn, gameBoard)

        if (playerMoveX, playerMoveY) != (None, None):
            # Add this new tile to the board:
            gameBoard[(playerMoveX, playerMoveY)] = turn

            # Check for winner after this new tile has been added:
            if isWinner(turn, gameBoard):
                displayBoard(gameBoard)
                print(turn.upper(), 'has won!')
                print('Thanks for playing!')
                sys.exit()

            # Check for a tie after this new tile has been added:
            if isBoardFull(gameBoard):
                displayBoard(gameBoard)
                print('The board is full and the game is a tie.')
                print('Thanks for playing!')
                sys.exit()

        # Switch to the other player's turn:
        if turn == O_PLAYER:
            turn = X_PLAYER
        elif turn == X_PLAYER:
            turn = O_PLAYER


def getNewBoard():
    """Returns a new dictionary that represents the board. The keys are
    (x, y) tuples of integers starting at 0 and going up to, but not
    including, BOARD_WIDTH and BOARD_HEIGHT."""
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE
    return board


def displayLetterLabels():
    """Display a row of letter labels, based on the BOARD_WIDTH."""
    print('   ', end='')  # Print the indentation.
    for x in range(BOARD_WIDTH):
        print(chr(65 + x) + ' ', end='')  # Print the letter.
    print()  # Print a newline.


def displayBoard(board):
    """Display the board data structure on the screen."""
    displayLetterLabels()  # Display the letter labels at the top.

    # Display each board row:
    for y in range(BOARD_HEIGHT):
        # Display the leftside number label:
        print(str(y + 1).rjust(2) + ' ', end='')
        for x in range(BOARD_WIDTH):
            # Display each tile in this row, followed by a space:
            print(board[(x, y)] + ' ', end='')
        # Display the rightside number label:
        print(y + 1)

    displayLetterLabels()  # Display the letter labels at the bottom.


def getPlayerMove(player, board):
    """Asks the player for a move and returns a (x, y) tuple of integer
    indexes for the place they want to put their tile. Also returns
    (None, None) if they want to pass on their turn."""
    print('It is ' + player.upper() + '\'s turn.')
    while True:  # Keep looping until the player enters a valid move:
        print('Enter a move (such as B3) or PASS or QUIT:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response == 'PASS':
            return (None, None)  # No move should be made.

        # Make sure the player entered a valid move like 'B3' or 'D14'.
        # The response[0] character will always be a letter, and the
        # next one or more characters must be a number.
        if len(response) >= 2 and response[1:].isdecimal():
            # Make sure the letter they entered is on the board:
            if 'A' <= response[0] < chr(65 + BOARD_WIDTH):
                # Make sure the number they entered is on the board:
                if 1 <= int(response[1:]) <= BOARD_HEIGHT:
                    # Get the integer indexes for their move:
                    moveX = ord(response[0]) - 65
                    moveY = int(response[1:]) - 1

                    if board[(moveX, moveY)] != EMPTY_SPACE:
                        print('There is already a piece there.')
                        continue
                    break  # Player has entered a valid move.

        # If any of the previous checks failed, make the player enter
        # their move again:
        print('That is not a valid space on this board.')
    return (moveX, moveY)


def isWinner(player, board):
    """Returns True if player has four tiles in a row on board,
    otherwise returns False."""

    # Go through the entire board, checking for five-in-a-row:
    for columnIndex in range(BOARD_WIDTH - 4):
        for rowIndex in range(BOARD_HEIGHT):
            # Check for five-in-a-row going across to the right:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            tile5 = board[(columnIndex + 4, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == tile5 == player:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 4):
            # Check for five-in-a-row going down:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            tile5 = board[(columnIndex, rowIndex + 4)]
            if tile1 == tile2 == tile3 == tile4 == tile5 == player:
                return True

    for columnIndex in range(BOARD_WIDTH - 4):
        for rowIndex in range(BOARD_HEIGHT - 4):
            # Check for five-in-a-row going right-down diagonal:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            tile5 = board[(columnIndex + 4, rowIndex + 4)]
            if tile1 == tile2 == tile3 == tile4 == tile5 == player:
                return True

            # Check for five-in-a-row going left-down diagonal:
            tile1 = board[(columnIndex + 4, rowIndex)]
            tile2 = board[(columnIndex + 3, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 1, rowIndex + 3)]
            tile5 = board[(columnIndex, rowIndex + 4)]
            if tile1 == tile2 == tile3 == tile4 == tile5 == player:
                return True
    return False


def isBoardFull(board):
    """Returns True if the board is full of tiles, otherwise, returns
    False if there is at least one empty space somewhere on the board."""
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] == EMPTY_SPACE:
                # An empty space means the board is not full.
                return False
    return True  # None of the spaces were empty, so the board is full.


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
