# A non-OOP Tic Tac Toe game.
# By Al Sweigart al@inventwithpython.com

# Setting up constants:
ALL_SPACES = list('123456789') # The keys for a TTT board dictionary.
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = getNewBoard() # Create a TTT board dictionary.
    turn, nextTurn = X, O # X goes first, O goes next.

    while True:
        drawBoard(gameBoard) # Display the board on the screen.
        move = getPlayerMove(gameBoard, turn) # Get the player's move.
        updateBoard(gameBoard, move, turn) # Update the board with the move.

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
    board = {} # The board is represented as a Python dictionary.
    for space in ALL_SPACES:
        board[space] = BLANK # All spaces start as blank.
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
    b, p = board, player # Shorter names as "syntactic sugar".
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['7'] == b['8'] == b['9'] == p) or # Across the top
            (b['4'] == b['5'] == b['6'] == p) or # Across the middle
            (b['1'] == b['2'] == b['3'] == p) or # Across the bottom
            (b['7'] == b['4'] == b['1'] == p) or # Down the left
            (b['8'] == b['5'] == b['2'] == p) or # Down the middle
            (b['9'] == b['6'] == b['3'] == p) or # Down the right
            (b['7'] == b['5'] == b['3'] == p) or # Diagonal
            (b['9'] == b['5'] == b['1'] == p))   # Diagonal

def getPlayerMove(board, player):
    """Let the player type in their move."""
    space = None
    # Keep asking the player until they enter a number 1-9:
    while space not in ALL_SPACES or board[space] != BLANK:
        print(f'What is {player}\'s move? (1-9)')
        space = input().upper()
    return space

def isBoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False # If a single space is blank, return False.
    return True # No spaces are blank, so return True.

def updateBoard(board, space, player):
    """Sets the space on the board to player."""
    board[space] = player

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
