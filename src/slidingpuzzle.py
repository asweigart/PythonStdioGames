# Sliding Puzzle, by Al Sweigart al@inventwithpython.com

import logging
LOG_FILE = 'slidingpuzzle_log.txt' # Set to None to display logs on the screen instead.
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL) # Uncomment this line out to disable logs.
logging.debug('Start of program.')

import random, sys

BLANK = '  '


def getNewBoard():
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'], ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]


def drawBoard(board):
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],
              board[0][1], board[1][1], board[2][1], board[3][1],
              board[0][2], board[1][2], board[2][2], board[3][2],
              board[0][3], board[1][3], board[2][3], board[3][3]]
    boardToDraw = """
+----+----+----+----+
|    |    |    |    |
| {} | {} | {} | {} |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
| {} | {} | {} | {} |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
| {} | {} | {} | {} |
|    |    |    |    |
+----+----+----+----+
|    |    |    |    |
| {} | {} | {} | {} |
|    |    |    |    |
+----+----+----+----+
""".format(*labels)
    logging.debug('Drawing board:\n' + boardToDraw)
    print(boardToDraw)


def findBlankSpace(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def getPlayerMove(board):
    blankx, blanky = findBlankSpace(board)

    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                                 (%s)' % w)
        print('Enter your move (or "quit"): (%s) (%s) (%s)' % (a, s, d))

        move = input().upper()
        if move == 'QUIT':
            sys.exit()
        if move in (w + a + s + d).replace(' ', ''):
            return move


def makeMove(board, move):
    # Note: This function assumes that the move is valid.
    blankx, blanky = findBlankSpace(board)

    if move == 'W':
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == 'A':
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == 'S':
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == 'D':
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def makeRandomMove(board):
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 3:
        validMoves.append('W')
    if blankx != 3:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))


def getNewPuzzle(moves=200):
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board


def runGame():
    print('Sliding Puzzle')
    print('Use the WASD keys to move the tiles')
    print('back into their original order:')
    print('       1  2  3  4')
    print('       5  6  7  8')
    print('       9 10 11 12')
    print('      13 14 15   ')
    print()

    gameBoard = getNewPuzzle()

    while True:
        drawBoard(gameBoard)
        playerMove = getPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')


if __name__ == '__main__':
    runGame()
