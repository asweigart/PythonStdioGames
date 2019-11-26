# Rush Hour, by Al Sweigart al@inventwithpython.com
# A sliding tile puzzle game to move cars out of the way.
# Original game by Nob Yoshihagara
# More info at https://www.michaelfogleman.com/rush/
__version__ = 1

# rushhour_puzzle.txt generated from puzzles by Michael Fogleman

import math, random, sys

EMPTY_SPACE = '.'
WALL = chr(9608)

def getRandomPuzzle():
    numberOfPuzzles = 0
    puzzleFile = open('rushhourpuzzles.txt')
    while puzzleFile.readline():
        numberOfPuzzles += 1
    puzzleFile.close()

    randomPuzzleNum = random.randint(1, numberOfPuzzles)
    counter = 1
    puzzleFile = open('rushhourpuzzles.txt')
    while True:
        if counter == randomPuzzleNum:
            return puzzleFile.readline()
        else:
            puzzleFile.readline()
            counter += 1


def readPuzzle(puzzleAsString):
    # Set up data structure.
    board = {}

    # We assume that the puzzles are square shaped:
    board['width'] = int(math.sqrt(len(puzzleAsString)))
    board['height'] = int(math.sqrt(len(puzzleAsString)))

    x = 0
    y = 0
    for character in puzzleAsString:
        if character == 'x':
            character = WALL # Draw walls using the block character instead of x.
        board[(x, y)] = character

        if x == board['width'] - 1:
            y += 1
            x = 0
        else:
            x += 1
    return board


def drawBoard(board):
    for y in range(board['height']):
        for i in range(3): # We draw 3 rows per board-row.
            if i == 0 and y != 0:
                # Draw a horizontal dividing line:
                for x in range(board['width']):
                    if board[(x, y)] != EMPTY_SPACE and board[(x, y)] == board[(x, y - 1)]:
                        print(board[(x, y)] * 3 + ' ', end='') # Draw car in dividing line.
                    else:
                        print(' ' * 4, end='') # Draw empty dividing line.
                print()

            for x in range(board['width']):
                print(board[(x, y)] * 3, end='') # Draw the board space.

                if x != board['width'] - 1 and board[(x, y)] != EMPTY_SPACE and board[(x, y)] == board[(x + 1, y)]:
                    print(board[(x, y)], end='') # Draw car in vertical dividing line.
                else:
                    print(' ', end='') # Draw empty vertical dividing line.
            print()


def getValidMoves(board):
    validMoves = []
    for x in range(board['width']):
        for y in range(board['height']):
            if board[(x, y)] in (EMPTY_SPACE, WALL):
                continue # Skip this empty or wall space.

            xNotOnLeftEdge = x != 0
            xNotOnRightEdge = x != board['width'] - 1
            yNotOnTopEdge = y != 0
            yNotOnBottomEdge = y != board['height'] - 1

            # Check if the car at x, y can move down.
            if yNotOnTopEdge and board[(x, y)] == board[(x, y - 1)]:
                for i in range(1, board['height']):
                    if y + i < board['height'] and board[(x, y + i)] == EMPTY_SPACE:
                        validMoves.append(board[(x, y)] + ' d ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move up.
            if yNotOnBottomEdge and board[(x, y)] == board[(x, y + 1)]:
                for i in range(1, board['height']):
                    if y - i >= 0 and board[(x, y - i)] == EMPTY_SPACE:
                        validMoves.append(board[(x, y)] + ' u ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move right.
            if xNotOnLeftEdge and board[(x, y)] == board[(x - 1, y)]:
                for i in range(1, board['width']):
                    if x + i < board['width'] and board[(x + i, y)] == EMPTY_SPACE:
                        validMoves.append(board[(x, y)] + ' r ' + str(i))
                    else:
                        break

            # Check if the car at x, y can move left.
            if xNotOnRightEdge and board[(x, y)] == board[(x + 1, y)]:
                for i in range(1, board['width']):
                    if x - i >= 0 and board[(x - i, y)] == EMPTY_SPACE:
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
        allValidMoves = '", "'.join(validMoves)
        print('Enter a move: "{}" or "quit".'.format(allValidMoves))
        move = input().lower()
        if move == 'quit':
            sys.exit()
        if move in validMoves:
            return move


print("""RUSH HOUR
By Al Sweigart al@inventwithpython.com

Get the "a" car to the right edge of the board.
Enter moves as <car> <direction> <distance>.
Directions are (l)eft, (r)ight, (u)p, and (d)own.
""")

gameBoard = readPuzzle(getRandomPuzzle())
while True:
    drawBoard(gameBoard)
    playerMove = getPlayerMove(gameBoard)
    makeMove(gameBoard, playerMove)
    if hasWon(gameBoard):
        drawBoard(gameBoard)
        print('PUZZLE COMPLETE!')
        sys.exit()

