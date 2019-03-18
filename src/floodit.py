import random, sys
assert sys.version_info.major == 3, 'Run this program on Python 3.'

try:
    import bext # Attempt to import the bext module.
except:
    sys.exit('Bext is required to run this. Run `pip install bext` from the shell to install it.')

BLOCK     = chr(9608) # Character 9608 is '█'
LEFTRIGHT = chr(9472) # Character 9472 is '─'
UPDOWN    = chr(9474) # Character 9474 is '│'
DOWNRIGHT = chr(9484) # Character 9484 is '┌'
DOWNLEFT  = chr(9488) # Character 9488 is '┐'
UPRIGHT   = chr(9492) # Character 9492 is '└'
UPLEFT    = chr(9496) # Character 9496 is '┘'

# This constant maps letters to colors.
CMAP = {'R': 'red', 'G': 'green', 'B': 'blue',
        'Y': 'yellow', 'C': 'cyan', 'P': 'purple'}
COLORS = list(CMAP.keys())


def getNewBoard(width=16, height=16):
    assert width > 1 and height > 1
    board = []

    # Create random colors for the board.
    for x in range(height):
        column = []
        for y in range(width):
            column.append(random.choice(COLORS))
        board.append(column)

    # Make several tiles the same color as their neighbor.
    for i in range(width * height):
        x = random.randint(0, width - 2)
        y = random.randint(0, height - 1)
        board[x + 1][y] = board[x][y]
    return board


def drawBoard(board):
    width = len(board)
    height = len(board[0])
    bext.fg('white')
    print(DOWNRIGHT + (LEFTRIGHT * width) + DOWNLEFT)

    # Print first row with '>'.
    bext.fg('white')
    print('>', end='')
    for x in range(width):
        bext.fg(CMAP[board[x][0]])
        print(BLOCK, end='')
    bext.fg('white')
    print(UPDOWN)

    # Print each row after the first.
    for y in range(1, height):
        bext.fg('white')
        print(UPDOWN, end='')
        for x in range(width):
            bext.fg(CMAP[board[x][y]])
            print(BLOCK, end='')
        bext.fg('white')
        print(UPDOWN)
    bext.fg('white')
    print(UPRIGHT + (LEFTRIGHT * width) + UPLEFT)


def getPlayerMove():
    while True:
        bext.fg('white')
        print('Choose one of ', end='')
        bext.fg('red')
        print('R ', end='')
        bext.fg('green')
        print('G ', end='')
        bext.fg('blue')
        print('B ', end='')
        bext.fg('yellow')
        print('Y ', end='')
        bext.fg('cyan')
        print('C ', end='')
        bext.fg('purple')
        print('P ', end='')
        bext.fg('white')
        print(' or quit:')
        move = input().upper()
        if move == 'QUIT':
            sys.exit()
        if move in COLORS:
            return move


def changeTile(move, board, x, y, charToChange=None):
    if x == 0 and y == 0:
        charToChange = board[x][y]
        if move == charToChange:
            return # Already is the same color.

    board[x][y] = move

    width = len(board)
    height = len(board[0])

    if x > 0 and board[x - 1][y] == charToChange:
        changeTile(move, board, x - 1, y, charToChange)
    if y > 0 and board[x][y - 1] == charToChange:
        changeTile(move, board, x, y - 1, charToChange)
    if x < width - 1 and board[x + 1][y] == charToChange:
        changeTile(move, board, x + 1, y, charToChange)
    if y < height - 1 and board[x][y + 1] == charToChange:
        changeTile(move, board, x, y + 1, charToChange)


def hasWon(board):
    tile = board[0][0]
    width = len(board)
    height = len(board[0])

    for x in range(width):
        for y in range(height):
            if board[x][y] != tile:
                return False
    return True


def main():
    bext.fg('white')
    print(' FLOOD IT! '.center(40, '*'))
    gameBoard = getNewBoard()
    movesLeft = 20

    while True:
        drawBoard(gameBoard)

        print('Moves left:', movesLeft)
        playerMove = getPlayerMove()
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            drawBoard(gameBoard)
            print('You have won!')
            break
        elif movesLeft == 0:
            print('You have run out of moves!')
            break


if __name__ == '__main__':
    main()
