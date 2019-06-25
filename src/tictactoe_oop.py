# An object-oriented Tic Tac Toe game.
# By Al Sweigart al@inventwithpython.com

# Setting up constants:
ALL_SPACES = list('123456789') # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = TicTacToeBoard() # Create a TTT board object.
    turn, nextTurn = X, O # X goes first, O goes next.

    while True:
        gameBoard.drawBoard() # Display the board on the screen.
        move = gameBoard.getPlayerMove(turn) # Get the player's move.
        gameBoard.updateBoard(move, turn) # Update the board with the move.

        if gameBoard.isWinner(turn):
            gameBoard.drawBoard()
            print(turn + ' has won the game!')
            break
        elif gameBoard.isBoardFull():
            gameBoard.drawBoard()
            print('The game is a tie!')
            break

        turn, nextTurn = nextTurn, turn

class TicTacToeBoard:
    def __init__(self):
        """Create a new, blank tic tac toe board."""
        self.spaces = {} # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self.spaces[space] = BLANK # All spaces start as blank.

    def drawBoard(self):
        """Display a text-representation of the board."""
        print(f'''
          {self.spaces['7']}|{self.spaces['8']}|{self.spaces['9']}  7 8 9
          -+-+-
          {self.spaces['4']}|{self.spaces['5']}|{self.spaces['6']}  4 5 6
          -+-+-
          {self.spaces['1']}|{self.spaces['2']}|{self.spaces['3']}  1 2 3''')

    def isWinner(self, player):
        """Return True if player is a winner on this TicTacToeBoard."""
        b, p = self.spaces, player # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((b['7'] == b['8'] == b['9'] == p) or # Across the top
                (b['4'] == b['5'] == b['6'] == p) or # Across the middle
                (b['1'] == b['2'] == b['3'] == p) or # Across the bottom
                (b['7'] == b['4'] == b['1'] == p) or # Down the left
                (b['8'] == b['5'] == b['2'] == p) or # Down the middle
                (b['9'] == b['6'] == b['3'] == p) or # Down the right
                (b['7'] == b['5'] == b['3'] == p) or # Diagonal
                (b['9'] == b['5'] == b['1'] == p))   # Diagonal

    def getPlayerMove(self, player):
        """Let the player type in their move."""
        space = None
        # Keep asking the player until they enter a number 1-9:
        while space not in ALL_SPACES or self.spaces[space] != BLANK:
            print(f'What is {player}\'s move? (1-9)')
            space = input().upper()
        return space

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self.spaces[space] == BLANK:
                return False # If a single space is blank, return False.
        return True # No spaces are blank, so return True.

    def updateBoard(self, space, player):
        """Sets the space on the board to player."""
        self.spaces[space] = player

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
