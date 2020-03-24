"""Barca, by Al Sweigart al@inventwithpython.com

A chess-variant where each player's mice, lions, and elephants try to
occupy the watering holes near the center of the board.

Barca was invented by Andrew Caldwell http://playbarca.com
More info at https://en.wikipedia.org/wiki/Barca_(board_game)
"""

import sys

# Set up the constants:
SQUARE_PLAYER = 'Square Player'
ROUND_PLAYER = 'Round Player'
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

SQUARE_MOUSE = '[Mo]'
SQUARE_LION = '[Li]'
SQUARE_ELEPHANT = '[El]'
ROUND_MOUSE = '(Mo)'
ROUND_LION = '(Li)'
ROUND_ELEPHANT = '(El)'
LAND = ' __ '
WATER = ' ~~ '
AFRAID_OF = {SQUARE_MOUSE: ROUND_LION,
             SQUARE_LION: ROUND_ELEPHANT,
             SQUARE_ELEPHANT: ROUND_MOUSE,
             ROUND_MOUSE: SQUARE_LION,
             ROUND_LION: SQUARE_ELEPHANT,
             ROUND_ELEPHANT: SQUARE_MOUSE}

UPLEFT   = (-1, -1)
UP       = (0, -1)
UPRIGHT  = (1, -1)
LEFT     = (-1, 0)
RIGHT    = (1, 0)
DOWNLEFT = (-1, 1)
DOWN     = (0, 1)
DOWNRIGHT = (1, 1)
CARDINAL_DIRECTIONS = (UP, LEFT, RIGHT, DOWN)
DIAGONAL_DIRECTIONS = (UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT)
ALL_DIRECTIONS = CARDINAL_DIRECTIONS + DIAGONAL_DIRECTIONS

AFRAID_OF_MOVEMENTS = {SQUARE_MOUSE: DIAGONAL_DIRECTIONS,
                       SQUARE_LION: ALL_DIRECTIONS,
                       SQUARE_ELEPHANT: CARDINAL_DIRECTIONS,
                       ROUND_MOUSE: DIAGONAL_DIRECTIONS,
                       ROUND_LION: ALL_DIRECTIONS,
                       ROUND_ELEPHANT: CARDINAL_DIRECTIONS}

EMPTY_SPACE = 'empty'
WATERING_HOLES = ((3, 3), (6, 3), (3, 6), (6, 6))


def main():
    print("""Barca, by Al Sweigart al@inventwithpython.com
Barca is a chess variant where each player has two mice (rooks), lions
(bishops), and elephants (queens). The object of the game is to occupy
three of the four "watering hole" spaces near the middle of the board.

Mice are afraid of lions, lions are afraid of elephants, and elephants
are afraid of mice. Afraid animals are in "check", and must move away
before other animals can move.

Barca was invented by Andrew Caldwell http://playbarca.com
""")

    turn = ROUND_PLAYER
    gameBoard = getNewBoard()
    while True:  # Main game loop.
        breakpoint()
        displayBoard(gameBoard)

        #move = getPlayerMove(turn, gameBoard)
        #if isWinner(turn):
        #    pass

        # Switch turns to the next player.
        if turn == SQUARE_PLAYER:
            turn = ROUND_PLAYER
        elif turn == ROUND_PLAYER:
            turn = SQUARE_PLAYER


def getNewBoard():
    # First, set the board to be completely empty:
    board = {}  # Keys are (x, y) int tuples, values are player pieces.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    # Next, place the pieces in their starting positions:
    board[(4, 0)] = board[(5, 0)] = SQUARE_ELEPHANT
    board[(3, 1)] = board[(6, 1)] = SQUARE_LION
    board[(4, 1)] = board[(5, 1)] = SQUARE_MOUSE
    board[(4, 9)] = board[(5, 9)] = ROUND_ELEPHANT
    board[(3, 8)] = board[(6, 8)] = ROUND_LION
    board[(4, 8)] = board[(5, 8)] = ROUND_MOUSE

    return board


def displayBoard(board):
    spaces = []

    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
                if board[(x, y)] == EMPTY_SPACE and (x, y) not in WATERING_HOLES:
                    spaces.append(LAND)
                elif board[(x, y)] == EMPTY_SPACE and (x, y) in WATERING_HOLES:
                    spaces.append(WATER)
                else:
                    spaces.append(getAnimalStr(board, x, y))

    print("""
 +--A---B---C---D---E---F---G---H---I---J-+
 |                                        |
 1{}{}{}{}{}{}{}{}{}{}1
 |                                        |
 2{}{}{}{}{}{}{}{}{}{}2
 |                                        |
 3{}{}{}{}{}{}{}{}{}{}3
 |                                        |
 4{}{}{}{}{}{}{}{}{}{}4
 |                                        |
 5{}{}{}{}{}{}{}{}{}{}5
 |                                        |
 6{}{}{}{}{}{}{}{}{}{}6
 |                                        |
 7{}{}{}{}{}{}{}{}{}{}7
 |                                        |
 8{}{}{}{}{}{}{}{}{}{}8
 |                                        |
 9{}{}{}{}{}{}{}{}{}{}9
 |                                        |
10{}{}{}{}{}{}{}{}{}{}10
 +--A---B---C---D---E---F---G---H---I---J-+""".format(*spaces))


def getAnimalStr(board, x, y):
    piece = board[(x, y)]
    assert piece in (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT, ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT)

    for offsetX, offsetY in AFRAID_OF_MOVEMENTS[piece]:
        # Check the directions of the animal this piece is afraid of:
        checkX, checkY = x, y  # Start at the piece's location.
        while True:
            # The space check moves further in the current direction:
            checkX += offsetX
            checkY += offsetY
            if not isOnBoard(checkX, checkY):
                break  # This space is off-board, so stop checking.
            if board[(checkX, checkY)] == AFRAID_OF[piece]:
                return piece[0:-1] + '!'  # This piece is afraid.
            elif board[(checkX, checkY)] != EMPTY_SPACE:
                break  # Another animal is blocking any feared animals.
            elif board[(checkX, checkY)] == EMPTY_SPACE:
                continue  # This space is empty, so keep checking.
    return piece  # This piece is not afraid.


def isOnBoard(x, y):
    return (0 <= x < BOARD_WIDTH) and (0 <= y < BOARD_HEIGHT)


def getPlayerMove(player, board):
    pass


def isWinner(player, board):
    squareClaims = 0
    roundClaims = 0
    for space in WATERING_HOLES:
        if board[space] in (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT):
            squareClaims += 1
        elif board[space] in (ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT):
            roundClaims += 1

    if player == SQUARE_PLAYER and squareClaims >= 3:
        return True
    elif player == ROUND_PLAYER and roundClaims >= 3:
        return True
    else:
        return False



# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()


"""
     A   B   C   D   E   F   G   H
  +--------------------------------+
  |                                |
1 | __  __  __ [El][El] __  __  __ | 1
  |                                |
2 | __  __ [Li][Mo][Mo][Li] __  __ | 2
  |                                |
3 | __  __  ~~  __  __  ~~  __  __ | 3
  |                                |
4 | __  __  __  __  __  __  __  __ | 4
  |                                |
5 | __  __  __  __  __  __  __  __ | 5
  |                                |
6 | __  __  ~~  __  __  ~~  __  __ | 6
  |                                |
7 | __  __ (Li)(Mo)(Mo)(Li) __  __ | 7
  |                                |
8 | __  __  __ (El)(El) __  __  __ | 8
  +--------------------------------+
     A   B   C   D   E   F   G   H
{El}
{Li}
{Mo}

[El]
[Li]
[Mo]


"""