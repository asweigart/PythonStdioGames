# 2048, by Al Sweigart al@inventwithpython.com

import random


BLANK = ''

def getNewBoard():
    board = {}
    for x in range(4):
        for y in range(4):
            board[(x, y)] = BLANK

    startingNumbers = set()
    while len(startingNumbers) < 2:
        startingNumbers.add((random.randint(0, 3), random.randint(0, 3)))
    for position in startingNumbers:
        board[position] = 2

    return board



def drawBoard(board):
    labels = []
    for y in range(4):
        for x in range(4):
            labels.append(str(board[(x, y)]).center(5))

    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def squishColumn(column):
    # Note: Index 0 is the bottom of the column.

    # Drop all the numbers down into any blank spaces.
    columnNumbers = []
    for i in range(4):
        if column[i] != BLANK:
            columnNumbers.append(column[i])
            column[i] = BLANK
    for i, number in enumerate(columnNumbers):
        column[i] = number

    for startingIndex in range(3): # Skip index 3, since nothing can be on top of it.
        if column[startingIndex] == column[startingIndex + 1]:
            column[startingIndex] *= 2
            for aboveIndex in range(startingIndex + 1, 3):
                column[aboveIndex] = column[aboveIndex + 1]
            column[3] = BLANK
    # Note: Because the `column` list is modified in-place, this function doesn't need to return anything.


def makeMove(board, move):
    if move == 'W':
        allIndexes = (((0, 0), (0, 1), (0, 2), (0, 3)),
                      ((1, 0), (1, 1), (1, 2), (1, 3)),
                      ((2, 0), (2, 1), (2, 2), (2, 3)),
                      ((3, 0), (3, 1), (3, 2), (3, 3)))
    elif move == 'S':
        allIndexes = (((0, 3), (0, 2), (0, 1), (0, 0)),
                      ((1, 3), (1, 2), (1, 1), (1, 0)),
                      ((2, 3), (2, 2), (2, 1), (2, 0)),
                      ((3, 3), (3, 2), (3, 1), (3, 0)))
    elif move == 'A':
        allIndexes = (((0, 0), (1, 0), (2, 0), (3, 0)),
                      ((0, 1), (1, 1), (2, 1), (3, 1)),
                      ((0, 2), (1, 2), (2, 2), (3, 2)),
                      ((0, 3), (1, 3), (2, 3), (3, 3)))
    elif move == 'D':
        allIndexes = (((3, 0), (2, 0), (1, 0), (0, 0)),
                      ((3, 1), (2, 1), (1, 1), (0, 1)),
                      ((3, 2), (2, 2), (1, 2), (0, 2)),
                      ((3, 3), (2, 3), (1, 3), (0, 3)))

    for columnIndexes in allIndexes:
        column = [board[columnIndexes[0]], board[columnIndexes[1]], board[columnIndexes[2]], board[columnIndexes[3]]]
        squishColumn(column)
        board[columnIndexes[0]] = column[0]
        board[columnIndexes[1]] = column[1]
        board[columnIndexes[2]] = column[2]
        board[columnIndexes[3]] = column[3]
    # Note: Because the `board` dictionary is modified in-place, this function doesn't need to return anything.


def getPlayerMove():
    print('Enter move: (WASD)')
    while True:
        move = input().upper()
        if move in 'WASD' and move != '':
            return move


def addTwoToBoard(board):
    # TODO: If that side is grounded already, don't let the player move in that direction.
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if board[(x, y)] == BLANK:
            board[(x, y)] = 2
            return


def isFull(board):
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
    return True


def runGame():
    gameBoard = getNewBoard()

    while True:
        drawBoard(gameBoard)
        playerMove = getPlayerMove()
        makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over')
            return




if __name__ == '__main__':
    runGame()
    pass

