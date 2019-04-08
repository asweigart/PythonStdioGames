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

def isWinner(board, mark):
    """Return True if mark is a winner on board."""
    bo, m = board, mark # Shorter names for "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((bo['7'] == m and bo['8'] == m and bo['9'] == m) or
            (bo['4'] == m and bo['5'] == m and bo['6'] == m) or
            (bo['1'] == m and bo['2'] == m and bo['3'] == m) or
            (bo['7'] == m and bo['4'] == m and bo['1'] == m) or
            (bo['8'] == m and bo['5'] == m and bo['2'] == m) or
            (bo['9'] == m and bo['6'] == m and bo['3'] == m) or
            (bo['7'] == m and bo['5'] == m and bo['3'] == m) or
            (bo['9'] == m and bo['5'] == m and bo['1'] == m))

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

def setSpace(board, space, mark):
    """Sets the space on the board to mark."""
    board[space] = mark

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
