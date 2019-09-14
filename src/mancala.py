# Mancala, by Al Sweigart al@inventwithpython.com
# Rules at http://www.mancalarules.com/
# More info at https://en.wikipedia.org/wiki/Mancala

import sys

POCKETS = 'ABCDEF1LKJIHG2' # Every pocket label, in counterclockwise order.

def getNewBoard():
    """Return a dictionary representing a Mancala board in the starting
    state: 4 seeds in each pocket and 0 in the mancalas."""

    # Create the data structure for the board, with 4 seeds in each pocket.
    board = {'1': 0, '2': 0}
    for pocket in 'ABCDEFGHIJKL':
        board[pocket] = 4 # EXPERIMENT! Change the starting number of seeds.

    # Return the newly created board data structure.
    return board


def drawBoard(board):
    """Draws the game board as ASCII-art based on the `board` dictionary."""

    seedAmounts = []
    for space in 'GHIJKL21ABCDEF': # This string is the order of the pockets.
        seedAmounts.append(str(board[space]).rjust(2))

    # EXPERIMENT! Change the look of this board.
    boardToDraw = """
                <-<-<-<-<
+------+----+---Player 2---+----+----+------+
|M  2  |G   |H   |I   |J   |K   |L   |  1  M|
|A     | {} | {} | {} | {} | {} | {} |     A|
|N     |    |    |    |    |    |    |     N|
|C {}  +----+----+----+----+----+----+  {} C|
|A     |A   |B   |C   |D   |E   |F   |     A|
|L     | {} | {} | {} | {} | {} | {} |     L|
|A     |    |    |    |    |    |    |     A|
+------+----+---Player 1---+----+----+------+
                >->->->->
""".format(*seedAmounts)
    print(boardToDraw)


def getPlayerMove(turn, board):
    """Asks the player which pocket on their side of the board they select
    to sow seeds from. Returns the uppercase letter label of the pocket
    as a string."""

    while True: # Keep asking the player until they enter a valid move.
        # Ask player to select a pocket on their side:
        if turn == '1':
            print('Player 1, choose move: A-F (or QUIT)')
        elif turn == '2':
            print('Player 2, choose move: G-L (or QUIT)')
        pocket = input().upper()

        if pocket == 'QUIT':
            sys.exit()

        # Make sure it is a valid pocket to select:
        # EXPERIMENT! Delete this if-block to let the player select any pocket.
        if (turn == '1' and pocket not in 'ABCDEF') or (turn == '2' and pocket not in 'GHIJKL') or (pocket == ''):
            print('Please pick a letter on your side of the board.')
            continue # Ask again.
        if board.get(pocket) == 0:
            print('Please pick a non-empty pocket.')
            continue # Ask again.
        return pocket


def makeMove(board, turn, pocket):
    """Modify the `board` data structure so that the player 1 or 2 in `turn`
    selected `pocket` as their pocket to sow seeds from. Returns either '1'
    or '2' for whose turn it is next."""

    seedsToSow = board[pocket] # Get number of seeds from selected pocket.
    board[pocket] = 0 # Empty out the selected pocket.

    while seedsToSow > 0: # Continue sowing until we have no more seeds.
        pocket = POCKETS[(POCKETS.index(pocket) + 1) % 14] # Next pocket.
        if (turn == '1' and pocket == '2') or (turn == '2' and pocket == '1'):
            continue # Skip opponent's mancala.
        board[pocket] += 1 # Add one seed to the pocket.
        seedsToSow -= 1 # Decrease one seed from seedsToSow.

    if pocket == turn: # i.e. if pocket and turn are both '1' or both '2'.
        return turn # Last seed in player's mancala; take another turn.

    # Check if last seed was in an empty pocket; take opposite pocket's seeds.
    if (turn == '1' and pocket in 'ABCDEF' and board[pocket] == 1):
        oppositePocket = 'GHIJKL'['ABCDEF'.index(pocket)]
        board['1'] += board[oppositePocket]
        board[oppositePocket] = 0
    elif (turn == '2' and pocket in 'GHIJKL' and board[pocket] == 1):
        oppositePocket = 'ABCDEF'['GHIJKL'.index(pocket)]
        board['2'] += board[oppositePocket]
        board[oppositePocket] = 0

    # Return the other player as the next player.
    if turn == '1':
        return '2'
    elif turn == '2':
        return '1'


def isWinner(board):
    """Looks at `board` and returns either '1' or '2' if there is a winner or
    'tie' or 'no winner' if there isn't. The game ends when a player has 24 or
    more seeds in their mancala or one side of the board has 0 seeds in each
    pocket."""

    b = board # Make a shorter variable name to use in this function.

    # If either players has >= 24 or no seeds, the game ends.
    if (b['1'] >= 24) or (b['2'] >= 24) or \
       (b['A'] + b['B'] + b['C'] + b['D'] + b['E'] + b['F'] == 0) or \
       (b['G'] + b['H'] + b['I'] + b['J'] + b['K'] + b['L'] == 0):

        # Game is over, find player with largest score.
        if b['1'] > b['2']:
            return '1'
        elif b['2'] > b['1']:
            return '2'
        else:
            return 'tie'
    return 'no winner' # No one has won yet.


def main():
    """Runs a single game of Mancala."""
    print('''MANCALA - The seed sowing game.
By Al Sweigart al@inventwithpython.com
''')

    gameBoard = getNewBoard()
    playerTurn = '1' # Player 1 starts.

    while True: # Main game loop.
        # Display board and get player's move.
        drawBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)

        # Carry out the player's move.
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # Check if the game ended and a player has won.
        winner = isWinner(gameBoard)
        if winner == '1' or winner == '2':
            drawBoard(gameBoard)
            print(f'Player {winner} has won!')
            break
        elif winner == 'tie':
            drawBoard(gameBoard)
            print('There is a tie!')
            break


# If the player runs this program (instead of importing it), run the game:
if __name__ == '__main__':
    main()
