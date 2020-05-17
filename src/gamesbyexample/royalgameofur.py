"""The Royal Game of Ur, by Al Sweigart al@inventwithpython.com
A 5,000 year old board game from Mesopotamia. Two players knock each
other back as they race for the goal.
More info https://en.wikipedia.org/wiki/Royal_Game_of_Ur
This and other games are available at https://nostarch.com/XX
Tags: large, game, two-player, board game
"""
__version__ = 0
import random, sys

X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '

# Set up constants for the space labels:
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'

# The spaces in left to right, top to bottom order:
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'  # (H stands for Home, G stands for Goal.)
O_TRACK = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')

BOARD_TEMPLATE = """
                   {}           {}
                   Home              Goal
                   v v v             ^ ^ ^
+-----+-----+-----+-----+           +-----+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+v-v-v+-----+-----+-----+-----+-----+-----+^-^-^+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+^-^-^+-----+-----+-----+-----+-----+-----+v-v-v+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+-----+           +-----+-----+
                   ^ ^ ^             v v v
                   Home              Goal
                   {}           {}
"""


def main():
    print('''The Royal Game of Ur, by Al Sweigart al@inventwithpython.com

This is a 5,000 year old game. Two players must move their tokens
from their home to their goal. On your turn you flip four coins and can
move one token a number of spaces equal to the heads you got.

Ur is a racing game; the first player to move all seven of their tokens
to their goal wins. To do this, tokens must travel from their home to
their goal:

            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal

If you land on an opponent's token in the middle track, it gets sent back
home. The **flower** spaces let you take another turn. Tokens in the
middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    turn = O_PLAYER
    while True:  # Main game loop.
        # Set up some variables for this turn:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponentHome = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponentHome = X_HOME

        displayBoard(gameBoard)

        input('It is ' + turn + '\'s turn. Press Enter to flip...')

        flipTally = 0
        print('Flips: ', end='')
        for i in range(4):  # Flip 4 coins.
            result =  random.randint(0, 1)
            if result == 0:
                print('T', end='')  # Tails.
            else:
                print('H', end='')  # Heads.
            if i != 3:
                print('-', end='')  # Print separator.
            flipTally += result
        print('  ', end='')

        if flipTally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent  # Swap turns to the other player.
            continue

        # Ask the player for their move:
        validMoves = getValidMoves(gameBoard, turn, flipTally)

        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent  # Swap turns to the other player.
            continue

        while True:
            print('Select a token to move', flipTally, 'spaces: ', end='')
            print(' '.join(validMoves) + ' quit')
            move = input('> ').lower()

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in validMoves:
                break  # Exit the loop when a valid move is selected.

            print('That is not a valid move.')

        # Perform the selected move on the board:
        if move == 'home':
            # Subtract tokens at home if moving from home:
            gameBoard[home] -= 1
            nextTrackSpaceIndex = flipTally
        else:
            gameBoard[move] = EMPTY  # Set the "from" space to empty.
            nextTrackSpaceIndex = track.index(move) + flipTally

        movingOntoGoal = nextTrackSpaceIndex == len(track) - 1
        if movingOntoGoal:
            gameBoard[goal] += 1
            # Check if the player has won:
            if gameBoard[goal] == 7:
                displayBoard(gameBoard)
                print(turn, 'has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextBoardSpace = track[nextTrackSpaceIndex]
            # Check if the opponent has a tile there:
            if gameBoard[nextBoardSpace] == opponent:
                gameBoard[opponentHome] += 1

            # Set the "to" space to the player's token:
            gameBoard[nextBoardSpace] = turn

        # Check if the player landed on a flower space and can go again:
        if nextBoardSpace in FLOWER_SPACES:
            print(turn, 'landed on a flower space and gets to go again.')
            input('Press Enter to continue...')
        else:
            turn = opponent  # Swap turns to the other player.

def getNewBoard():
    """
    Returns a dictionary that represents the state of the board. The keys
    are strings of the space labels, the values are X_PLAYER, O_PLAYER,
    or EMPTY. There are also counters for how many tokens are at the
    home and goal of both players.
    """
    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    # Set each space as empty to start:
    for spaceLabel in ALL_SPACES:
        board[spaceLabel] = EMPTY

    return board


def displayBoard(board):
    """TODO"""
    # "Clear" the screen by printing many newlines, so the old
    # board isn't visible anymore.
    print('\n' * 60)

    xHomeTokens = ('X' * board[X_HOME]).ljust(7, '.')
    xGoalTokens = ('X' * board[X_GOAL]).ljust(7, '.')
    oHomeTokens = ('O' * board[O_HOME]).ljust(7, '.')
    oGoalTokens = ('O' * board[O_GOAL]).ljust(7, '.')

    # Add the strings that should populate BOARD_TEMPLATE in order,
    # going from left to right, top to bottom.
    spaces = []
    spaces.append(xHomeTokens)
    spaces.append(xGoalTokens)

    for spaceLabel in ALL_SPACES:
        spaces.append(board[spaceLabel])

    spaces.append(oHomeTokens)
    spaces.append(oGoalTokens)

    print(BOARD_TEMPLATE.format(*spaces))


def getValidMoves(board, player, flipTally):
    validMoves = []  # Contains all the spaces with tokens that can move.

    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    # Check if the player can move a token from home:
    if board[home] > 0 and board[track[flipTally]] == EMPTY:
        validMoves.append('home')

    # Check which spaces have a token the player can move:
    for trackSpaceIndex, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue

        nextTrackSpaceIndex = trackSpaceIndex + flipTally

        if nextTrackSpaceIndex >= len(track):
            # You must flip an exact number of moves onto the goal,
            # otherwise you can't move on the goal.
            continue
        else:
            nextBoardSpaceKey = track[nextTrackSpaceIndex]
            if nextBoardSpaceKey == 'G':
                # This token can move off the board:
                validMoves.append(space)
                continue

        if board[nextBoardSpaceKey] in (EMPTY, opponent):
            # If the next space is the protected middle space, you
            # can only move there if it is empty:
            if nextBoardSpaceKey == 'l' and board['l'] == opponent:
                continue  # Skip this move, the space is protected.
            validMoves.append(space)

    return validMoves


if __name__ == '__main__':
    main()