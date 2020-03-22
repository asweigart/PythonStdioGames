"""Gomoku, by Al Sweigart al@inventwithpython.com

Gomoku is a Japanese board game where two players take turns placing
down tiles. The first player to place five tiles in a row horizontally,
vertically, or diagonally wins.

More info at: https://en.wikipedia.org/wiki/Gomoku
Tags: large, game, board game, two-player
"""

import sys

# TODO - polish and refactor

# Set up the constants:
X_PLAYER = 'x'
O_PLAYER = 'o'
EMPTY_SPACE = '.'
BOARD_WIDTH = 15
BOARD_HEIGHT = 15

assert BOARD_WIDTH < 100
assert BOARD_HEIGHT < 100


def main():
    print("""GOMOKU
By Al Sweigart al@inventwithpython.com

Gomoku is a Japanese board game where two players take turns placing
down tiles. The first player to place five tiles in a row horizontally,
vertically, or diagonally wins.""")

    turn = O_PLAYER
    gameBoard = getNewBoard()
    while True:
        displayBoard(gameBoard)
        makePlayerMove(turn, gameBoard)

        # Check for winner:
        if isWinner(turn, gameBoard):
            displayBoard(gameBoard)
            print(turn.upper(), 'has won!')
            print('Thanks for playing!')
            sys.exit()

        # Switch to the other player's turn:
        if turn == O_PLAYER:
            turn = X_PLAYER
        elif turn == X_PLAYER:
            turn = O_PLAYER


def getNewBoard():
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE
    return board


def displayBoard(board):
    # Display the letter labels at the top:
    print('   ', end='')  # Print the indentation.
    for x in range(BOARD_WIDTH):
        print(chr(65 + x) + ' ', end='')  # Print the letter.
    print()  # Print a newline.

    # Display each board row:
    for y in range(BOARD_HEIGHT):
        print(str(y + 1).rjust(2) + ' ', end='')  # Print the leftside number label.
        for x in range(BOARD_WIDTH):
            print(board[(x, y)] + ' ', end='')
        print(y + 1)

    # Display the letter labels at the bottom:
    print('   ', end='')  # Print the indentation.
    for x in range(BOARD_WIDTH):
        print(chr(65 + x) + ' ', end='')  # Print the letter.
    print()  # Print a newline.


def makePlayerMove(player, board):
    print('It is ' + player.upper() + '\'s turn.')
    while True:  # Keep looping until the player enters a valid move:
        print('Enter a move (such as B3) or PASS or QUIT:')
        response = input().upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response == 'PASS':
            return  # Return without making any move.

        if len(response) >= 2 and response[1:].isdecimal():
            if ('A' <= response[0] < chr(65 + BOARD_WIDTH)) and (1 <= int(response[1:]) <= BOARD_HEIGHT):
                x = ord(response[0]) - 65
                y = int(response[1:]) - 1
                if board[(x, y)] != EMPTY_SPACE:
                    print('There is already a piece there.')
                    continue
                break  # Player has entered a valid move.
        print('That is not a valid space on this board.')
    # Make the move on the board.
    board[(x, y)] = player


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


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
