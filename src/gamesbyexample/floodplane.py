"""Floodplane, by Al Sweigart al@inventwithpython.com
A colorful game where you try to fill the board with a single color.
Inspired by the "Flood It!" game.
This and other games are available at https://nostarch.com/XX
Tags: large, game, bext"""
__version__ = 0
import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 16
HEIGHT = 14
BLOCK     = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN    = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT  = chr(9488)  # Character 9488 is '┐'
UPRIGHT   = chr(9492)  # Character 9492 is '└'
UPLEFT    = chr(9496)  # Character 9496 is '┘'

# All the color/letter tiles used on the board:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
              3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
LETTERS_MAP = {0: 's', 1: 'o', 2:'x', 3:'m', 4:'a', 5:'i'}
LETTER_MODE = 'letter mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Floodplane, by Al Sweigart al@inventwithpython.com

Set the color/letter of the upper left square, which fills in all the
adjacent squares of that color/letter. Try to make the entire board the
same color/letter.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = LETTER_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = 20

    while True:  # Main game loop.
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def getNewBoard():
    """Return a dictionary of a new Flood It board."""

    # Keys are (x, y) tuples, values are the tile at that position.
    board = {}

    # Create random colors for the board.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # Make several tiles the same as their neighbor. This creates groups
    # of the same color/letter.
    for i in range(WIDTH * HEIGHT):
        x = random.randint(0, WIDTH - 2)
        y = random.randint(0, HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board, displayMode):
    """Display the board on the screen."""
    bext.fg('white')
    print(DOWNRIGHT + (LEFTRIGHT * WIDTH) + DOWNLEFT)

    bext.fg('white')

    # Display each row:
    for y in range(HEIGHT):
        bext.fg('white')
        if y == 0:  # The first row begins with '>'.
            print('>', end='')
        else:  # Later rows begin with a vertical line.
            print(UPDOWN, end='')

        # Display each tile in this row:
        for x in range(WIDTH):
            if displayMode == COLOR_MODE:
                bext.fg(COLORS_MAP[board[(x, y)]])
                print(BLOCK, end='')
            elif displayMode == LETTER_MODE:
                print(LETTERS_MAP[board[(x, y)]], end='')
        bext.fg('white')
        print(UPDOWN)
    bext.fg('white')
    print(UPRIGHT + (LEFTRIGHT * WIDTH) + UPLEFT)


def askForPlayerMove(displayMode):
    """Let the player select a color to paint the upper left tile."""
    while True:
        bext.fg('white')
        print('Choose one of ', end='')

        if displayMode == COLOR_MODE:
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
        elif displayMode == LETTER_MODE:
            print('s o x m a i ', end='')
        bext.fg('white')
        print(' or QUIT:')
        move = input('> ').lower()
        if move == 'quit':
            sys.exit()
        if displayMode == COLOR_MODE:
            if move == 'r':
                return 0
            elif move == 'g':
                return 1
            elif move == 'b':
                return 2
            elif move == 'y':
                return 3
            elif move == 'c':
                return 4
            elif move == 'p':
                return 5
        if displayMode == LETTER_MODE:
            if move == 's':
                return 0
            elif move == 'o':
                return 1
            elif move == 'x':
                return 2
            elif move == 'm':
                return 3
            elif move == 'a':
                return 4
            elif move == 'i':
                return 5


def changeTile(move, board, x, y, charToChange=None):
    """Change the color/letter of a tile."""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if move == charToChange:
            return  # Already is the same tile.

    board[(x, y)] = move

    if x > 0 and board[(x - 1, y)] == charToChange:
        changeTile(move, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        changeTile(move, board, x, y - 1, charToChange)
    if x < WIDTH - 1 and board[(x + 1, y)] == charToChange:
        changeTile(move, board, x + 1, y, charToChange)
    if y < HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        changeTile(move, board, x, y + 1, charToChange)


def hasWon(board):
    """Return True if the entire board is one color/letter."""
    tile = board[(0, 0)]

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
