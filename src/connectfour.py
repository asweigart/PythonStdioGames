# Connect Four, by Al Sweigart al@inventwithpython.com

import sys

EMPTY_SPACE = '.'
X_PLAYER = 'X'
O_PLAYER = 'O'

def getNewBoard():
    # Note: The board is 7x6, represented by a dictionary with keys
    # of (x, y) tuples from (0, 0) to (6, 5), and values of '.' (empty),
    # 'X' (X player), or 'O' (O player)
    board = {}
    for y in range(6):
        for x in range(7):
            board[(x, y)] = EMPTY_SPACE
    return board


def drawBoard(board):
    tileChars = []
    for y in range(6):
        for x in range(7):
            tileChars.append(board[(x, y)])

    boardToDraw = """     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars)
    print(boardToDraw)


def getPlayerMove(playerTile, board):
    # Let the player select a column to drop a tile into.
    while True:
        print(f'Player {playerTile}, enter your move (1-7) or QUIT:')
        move = input()
        if move == 'quit':
            print('Thanks for playing!')
            sys.exit()
        if move not in '1234567':
            continue # Ask again for their move.

        try:
            move = int(move) - 1 # - 1 adjust for 0-based index.
        except:
            continue # They didn't enter a number, ask again for their move.

        # Starting from the bottom, find the first not-occupied space.
        for i in range(5, -1, -1):
            if board[(move, i)] == EMPTY_SPACE:
                return (move, i)


def isFull(board):
    for y in range(6):
        for x in range(7):
            if board[(x, y)] != EMPTY_SPACE:
                return False # Found an empty space, so return False.
    return True # All spaces are full.


def isWinner(playerTile, board):
    b = board # Using a shorter name instead of `board`.

    # Go through the entire board, checking for four-in-a-row:
    for y in range(6):
        for x in range(4):
            # Check for four-in-a-row going across:
            if b[(x, y)] == b[(x + 1, y)] == b[(x + 2, y)] == b[(x + 3, y)] == playerTile:
                return True

    for y in range(3):
        for x in range(7):
            # Check for four-in-a-row going down:
            if b[(x, y)] == b[(x, y + 1)] == b[(x, y + 2)] == b[(x, y + 3)] == playerTile:
                return True

    for y in range(3):
        for x in range(4):
            # Check for four-in-a-row going right-down diagonal:
            if b[(x, y)] == b[(x + 1, y + 1)] == b[(x + 2, y + 2)] == b[(x + 3, y + 3)] == playerTile:
                return True

            # Check for four-in-a-row going left-down diagonal:
            if b[(x + 3, y)] == b[(x + 2, y + 1)] == b[(x + 1, y + 2)] == b[(x, y + 3)] == playerTile:
                return True
    return False


def main():
    print('''CONNECT FOUR
By Al Sweigart al@inventwithpython.com
''')

    # Set up a new game:
    gameBoard = getNewBoard()
    playerTurn = X_PLAYER

    while True:
        # Draw board and get player's move:
        drawBoard(gameBoard)

        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Check for a win or tie:
        if isWinner(playerTurn, gameBoard):
            drawBoard(gameBoard)
            print(f'Player {playerTurn} has won!')
            break
        elif isFull(gameBoard):
            drawBoard(gameBoard)
            print('There is a tie!')
            break

        # Switch turn to other player:
        if playerTurn == X_PLAYER:
            playerTurn = O_PLAYER
        elif playerTurn == O_PLAYER:
            playerTurn = X_PLAYER


if __name__ == '__main__':
    main()
