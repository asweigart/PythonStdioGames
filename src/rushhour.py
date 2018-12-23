PUZZLES = ['''
bb...c
d..e.c
daae.c
d..e..
f...gg
f.hhh.'''.strip(), # beginner #1
'''
bccd..
b..d..
baad..
..efff
..e..g
..hhhg'''.strip(), # intermediate #11
'''
bbcd..
e.cd..
eaad..
efff..
......
...ggg'''.strip(), # advanced # 21
'''
bb.ccc
...dee
faad.g
f.hiig
jjh..g
..hkkk'''.strip(), # expert #31
]

PUZZLE = PUZZLES[0]

def readPuzzle(puzzleAsString):
    # Set up data structure.
    board = {}
    x = 0
    y = 0
    for character in puzzleAsString:
        if character == '\n':
            board['width'] = x
            y += 1
            x = 0
        else:
            board[(x, y)] = character
            x += 1
    board['height'] = y + 1
    return board


def drawBoard(board):
    for y in range(board['height']):
        for x in range(board['width']):
            print(board[(x, y)], end='')
        print()


def getValidMoves(board):
    validMoves = []
    for x in range(board['width']):
        for y in range(board['height']):
            if board[(x, y)] == '.':
                continue # Skip this empty space.

            # Check if the car at x, y can move down.
            if y != 0 and board[(x, y)] == board[(x, y - 1)]:
                for i in range(1, board['height']):
                    if y + i < board['height'] and board[(x, y + i)] == '.':
                        validMoves.append(board[(x, y)] + ' d ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move up.
            if y != board['height'] - 1 and board[(x, y)] == board[(x, y + 1)]:
                for i in range(1, board['height']):
                    if y - i >= 0 and board[(x, y - i)] == '.':
                        validMoves.append(board[(x, y)] + ' u ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move right.
            if x != 0 and board[(x, y)] == board[(x - 1, y)]:
                for i in range(1, board['width']):
                    if x + i < board['width'] and board[(x + i, y)] == '.':
                        validMoves.append(board[(x, y)] + ' r ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move left.
            if x != board['width'] - 1 and board[(x, y)] == board[(x + 1, y)]:
                for i in range(1, board['width']):
                    if x - i >= 0 and board[(x - i, y)] == '.':
                        validMoves.append(board[(x, y)] + ' l ' + str(i))
                    else:
                        break

    return validMoves


def makeMove(board, move):
    validMoves = getValidMoves(board)
    if move not in validMoves:
        return False

    car, direction, distance = move.split(' ')
    distance = int(distance)

    newCarPositions = []

    for x in range(board['width']):
        for y in range(board['height']):
            if board[(x, y)] == car:
                board[(x, y)] = '.'
                if direction == 'u':
                    newCarPositions.append((x, y - distance))
                elif direction == 'd':
                    newCarPositions.append((x, y + distance))
                elif direction == 'l':
                    newCarPositions.append((x - distance, y))
                elif direction == 'r':
                    newCarPositions.append((x + distance, y))

    for newCarPosition in newCarPositions:
        board[newCarPosition] = car


def hasWon(board):
    # The puzzle is solved when the 'a' car reaches the right edge.
    for y in range(board['height']):
        if board[(board['width'] - 1, y)] == 'a':
            return True

    return False


def getPlayerMove(board):
    validMoves = getValidMoves(board)
    while True:
        print('Enter a move: "' + '", "'.join(validMoves) + '"')
        print('(Or enter "help" for help or "quit" to quit.)')
        move = input().lower()
        if move in validMoves:
            return move


def runGame():
    gameBoard = readPuzzle(PUZZLE)
    while True:
        drawBoard(gameBoard)
        playerMove = getPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)
        if hasWon(gameBoard):
            drawBoard(gameBoard)
            print('PUZZLE COMPLETE!')
            return

if __name__ == '__main__':
    runGame()