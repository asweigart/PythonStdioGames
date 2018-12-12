# Mancala, by Al Sweigart

POCKETS = 'ABCDEF1LKJIHG2' # Constant for every pocket label, in order.

def getNewBoard():
    """Return a new board with 4 seeds in each starting pocket."""
    board = {'1': 0, '2': 0}
    for i in 'ABCDEFGHIJKL':
        board[i] = 4
    return board


def drawBoard(board):
    """Draw the game board."""
    seedAmounts = []
    for space in 'GHIJKL21ABCDEF':
        seedAmounts.append(str(board[space]).rjust(2))

    print("""
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
""".format(*seedAmounts))


def getPlayerMove(turn, board):
    """Let a player enter their move."""
    while True:
        # Ask player to select a pocket on their side.
        if turn == '1':
            print('Player 1, choose move: A-F')
        elif turn == '2':
            print('Player 2, choose move: G-L')
        move = input().upper()

        # Make sure it is a valid pocket to select.
        if (turn == '1' and move not in 'ABCDEF') or (turn == '2' and move not in 'GHIJKL') or (move == ''):
            print('Please pick a letter on your side of the board.')
            continue # Ask again.
        if board.get(move) == 0:
            print('Please pick a non-empty pocket.')
            continue # Ask again.
        return move


def makeMove(board, turn, move):
    """Carry out the player's move."""
    seedsToSow = board[move] # Get number of seeds from selected pocket.
    board[move] = 0 # Empty out the selected pocket.

    while seedsToSow > 0: # Continue sowing until we have no more seeds.
        move = POCKETS[(POCKETS.index(move) + 1) % 14] # Next pocket.
        if (turn == '1' and move == '2') or (turn == '2' and move == '1'):
            continue # Skip opponent's mancala.
        board[move] += 1 # Add one seed to the pocket.
        seedsToSow -= 1 # Decrease one seed from seedsToSow.

    if move == turn: # i.e. if move and turn are both '1' or both '2'.
        return 'one more turn' # Last seed in player's mancala; take another turn.

    # Check if last seed was in an empty pocket; take opposite pocket's seeds.
    if (turn == '1' and move in 'ABCDEF' and board[move] == 1):
        oppositePocket = 'GHIJKL'['ABCDEF'.index(move)]
        board['1'] += board[oppositePocket]
        board[oppositePocket] = 0
    elif (turn == '2' and move in 'GHIJKL' and board[move] == 1):
        oppositePocket = 'ABCDEF'['GHIJKL'.index(move)]
        board['2'] += board[oppositePocket]
        board[oppositePocket] = 0
    return 'done'


def isWinner(board):
    b = board # Make a shorter variable name to use in this function.

    # Any player with 24 or more seeds wins.
    if b['1'] >= 24 and b['2'] < 24:
        return '1'
    if b['2'] >= 24 and b['1'] < 24:
        return '2'

    # If both players have >= 24 or one player has no seeds, the game ends.
    if (b['1'] >= 24 and b['2'] >= 24) or \
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
    gameBoard = getNewBoard()
    playerTurn = '1'

    while True: # Main game loop.
        # Display board and get player's move.
        drawBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)

        # Carry out the player's move.
        nextAction = makeMove(gameBoard, playerTurn, playerMove)
        if nextAction != 'one more turn':
            if playerTurn == '1':
                playerTurn = '2'
            elif playerTurn == '2':
                playerTurn = '1'

        # See if a player has won.
        winner = isWinner(gameBoard)
        if winner == '1' or winner == '2':
            drawBoard(gameBoard)
            print('Player %s has won!' % (winner))
            break
        elif winner == 'tie':
            drawBoard(gameBoard)
            print('There is a tie!')
            break


if __name__ == '__main__':
    main()
