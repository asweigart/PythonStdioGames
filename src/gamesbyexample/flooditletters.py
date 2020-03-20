"""Flood It! (Letter Version), by Al Sweigart al@inventwithpython.com

A colorful game where you try to fill the board with a single color.
(This version uses letters instead of colors for colorblind users.)
Tags: short, game"""
__version__ = 1

import random, sys

# Set up the constants:
WIDTH = 16
HEIGHT = 14

# All the letters used on the board:
LETTERS = ('s', 'o', 'x', 'm', 'a', 'i')


def main():
    """Run a single game of Flood It."""
    print('''FLOOD IT! (Letter Version)
By Al Sweigart al@inventwithpython.com

Set the letter of the upper left square, which fills in all the
adjacent squares of that letter. Try to make the entire board the
same letter.''')
    gameBoard = getNewBoard()
    movesLeft = 20

    while True:  # Main game loop.
        displayBoard(gameBoard)

        print('Moves left:', movesLeft)
        playerMove = getPlayerMove()
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard)
            print('You have run out of moves!')
            break
        # At this point, go back to the start of the main game loop.


def getNewBoard():
    """Return a dictionary of a new Flood It board."""
    board = {}

    # Create random letters for the board.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = random.choice(LETTERS)

    # Make several tiles the same letter as their neighbor.
    for i in range(WIDTH * HEIGHT):
        x = random.randint(0, WIDTH - 2)
        y = random.randint(0, HEIGHT - 2)
        if random.randint(0, 1) == 0:
            board[(x + 1, y)] = board[(x, y)]
        else:
            board[(x, y + 1)] = board[(x, y)]
    return board


def displayBoard(board):
    """Display the board on the screen."""
    # Print first row with '>'.
    print('   >', end='')
    for x in range(WIDTH):
        print(board[(x, 0)], end='')
    print()

    # Print each row after the first.
    for y in range(1, HEIGHT):
        print('    ', end='')
        for x in range(WIDTH):
            print(board[(x, y)], end='')
        print()


def getPlayerMove():
    """Let the player select a letter to paint the upper left tile."""
    while True:
        print('Choose one of s o x m a i or QUIT.')
        move = input().lower()
        if move == 'quit':
            sys.exit()
        if move in LETTERS:
            return move
        # At this point, go back to the start of the loop.


def changeTile(move, board, x, y, charToChange=None):
    """Change the letter of a tile."""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if move == charToChange:
            return  # Already is the same letter.

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
    """Return True if the entire board is one letter."""
    tile = board[(0, 0)]

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
