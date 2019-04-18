# A non-OOP Tic Tac Toe game.
# By Al Sweigart al@inventwithpython.com

# Setting up constants:
ALL_SPACES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = getNewBoard()
    turn, nextTurn = X, O

    while True:
        drawBoard(gameBoard)
        move = getPlayerMove(gameBoard, turn)
        setSpace(gameBoard, move, turn)

        if isWinner(gameBoard, turn):
            drawBoard(gameBoard)
            print(turn + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            drawBoard(gameBoard)
            print('The game is a tie!')
            break

        turn, nextTurn = nextTurn, turn

def getNewBoard():
    """Create a new, blank tic tac toe board."""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def drawBoard(board):
    """Display a text-representation of the board."""
    print(f'''
        {board['7']}|{board['8']}|{board['9']}  7 8 9
        -+-+-
        {board['4']}|{board['5']}|{board['6']}  4 5 6
        -+-+-
        {board['1']}|{board['2']}|{board['3']}  1 2 3''')

def isWinner(board, player):
    """Return True if player is a winner on board."""
    bo, p = board, player # Shorter names for "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((bo['7'] == p and bo['8'] == p and bo['9'] == p) or
            (bo['4'] == p and bo['5'] == p and bo['6'] == p) or
            (bo['1'] == p and bo['2'] == p and bo['3'] == p) or
            (bo['7'] == p and bo['4'] == p and bo['1'] == p) or
            (bo['8'] == p and bo['5'] == p and bo['2'] == p) or
            (bo['9'] == p and bo['6'] == p and bo['3'] == p) or
            (bo['7'] == p and bo['5'] == p and bo['3'] == p) or
            (bo['9'] == p and bo['5'] == p and bo['1'] == p))

def getPlayerMove(board, player):
    """Let the player type in their move."""
    space = None
    while space not in ALL_SPACES or not board[space] == BLANK:
        print(f'What is {player}\'s move? (1-9)')
        space = input().upper()
    return space

def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True

def setSpace(board, space, player):
    """Sets the space on the board to player."""
    board[space] = player

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
