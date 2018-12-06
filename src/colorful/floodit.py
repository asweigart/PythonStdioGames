import random
from colorama import init, Fore
init() # colorama.init() needs to be called first for colors to work.

# This constant maps letters to colors.
CMAP = {'R': Fore.RED, 'G': Fore.GREEN, 'B': Fore.BLUE,
        'Y': Fore.YELLOW, 'C': Fore.CYAN, 'P': Fore.MAGENTA}
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
    print(Fore.WHITE + '+' + ('-' * width) + '+')

    # Print first row with '>'.
    print(Fore.WHITE + '>', end='')
    for x in range(width):
        print(CMAP[board[x][0]] + chr(9608), end='')
    print(Fore.WHITE + '|')

    # Print each row after the first.
    for y in range(1, height):
        print(Fore.WHITE + '|', end='')
        for x in range(width):
            print(CMAP[board[x][y]] + chr(9608), end='')
        print(Fore.WHITE + '|')

    print(Fore.WHITE + '+' + ('-' * width) + '+')


def getPlayerMove():
    while True:
        print(Fore.WHITE + 'Choose one of ' + Fore.RED + 'R ' + Fore.GREEN + 'G ' + Fore.BLUE + 'B ' + Fore.YELLOW + 'Y ' + Fore.CYAN + 'C ' + Fore.MAGENTA + 'P' + Fore.WHITE + ' or quit:')
        move = input().upper()
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
    print(Fore.WHITE + ' FLOOD IT! '.center(40, '*'))
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
