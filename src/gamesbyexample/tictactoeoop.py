"""Tic-Tac-Toe (OOP), by Al Sweigart al@inventwithpython.com
The classic board game. (Object-oriented programming version.)
This and other games are available at https://nostarch.com/XX
Tags: large, board game, game, object-oriented, two-player"""
__version__ = 0
import copy

ALLspaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # Constants for string values.


def main():
    print('Welcome to Tic-Tac-Toe!')
    # (!) Try replacing TTTBoard() with MiniTTTBoard() or HintTTTBoard()
    gameBoard = TTTBoard()  # Create a TTT board object.
    currentPlayer, nextPlayer = X, O  # X goes first, O goes next.

    while True:  # Main game loop.
        # Display the board on the screen:
        print(gameBoard.getBoardStr())

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not gameBoard.isValidSpace(move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        gameBoard.updateBoard(move, currentPlayer)  # Make the move.

        # Check if the game is over:
        if gameBoard.isWinner(currentPlayer):  # Check for a winner.
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' has won the game!')
            break
        elif gameBoard.isBoardFull():  # Next check for a tie.
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        # Switch turns to the next player:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')


class TTTBoard:
    def __init__(self):
        """Create a new, blank tic-tac-toe board."""
        # Map of space numbers: 1|2|3
        #                       -+-+-
        #                       4|5|6
        #                       -+-+-
        #                       7|8|9
        # Keys are 1 through 9, the values are X, O, or BLANK.
        self.spaces = {}
        for space in ALLspaces:
            self.spaces[space] = BLANK  # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(self.spaces['1'], self.spaces['2'],
        self.spaces['3'], self.spaces['4'], self.spaces['5'],
        self.spaces['6'], self.spaces['7'], self.spaces['8'],
        self.spaces['9'])

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space
        number and the space is blank."""
        return space in ALLspaces and self.spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        # Shorter variable names used here for readablility:
        s, p = self.spaces, player
        # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals.
        return ((s['1'] == s['2'] == s['3'] == p) or  # Across top
                (s['4'] == s['5'] == s['6'] == p) or  # Across middle
                (s['7'] == s['8'] == s['9'] == p) or  # Across bottom
                (s['1'] == s['4'] == s['7'] == p) or  # Down left
                (s['2'] == s['5'] == s['8'] == p) or  # Down middle
                (s['3'] == s['6'] == s['9'] == p) or  # Down right
                (s['3'] == s['5'] == s['7'] == p) or  # Diagonal
                (s['1'] == s['5'] == s['9'] == p))    # Diagonal

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALLspaces:
            if self.spaces[space] == BLANK:
                return False  # If any space is blank, return False.
        return True  # No spaces are blank, so return True.

    def updateBoard(self, space, player):
        """Sets the space on the board to player."""
        self.spaces[space] = player


class MiniTTTBoard(TTTBoard):
    def getBoardStr(self):
        """Return a tiny text-representation of the board."""
        # Change blank spaces to a '.'
        for space in ALLspaces:
            if self.spaces[space] == BLANK:
                self.spaces[space] = '.'

        boardStr = '''
          {}{}{} 123
          {}{}{} 456
          {}{}{} 789'''.format(self.spaces['1'], self.spaces['2'],
            self.spaces['3'], self.spaces['4'], self.spaces['5'],
            self.spaces['6'], self.spaces['7'], self.spaces['8'],
            self.spaces['9'])

        # Change '.' back to blank spaces.
        for space in ALLspaces:
            if self.spaces[space] == '.':
                self.spaces[space] = BLANK
        return boardStr


class HintTTTBoard(TTTBoard):
    def getBoardStr(self):
        """Return a text-representation of the board with hints."""
        # Call getBoardStr() in the parent/super class, TTTBoard.
        boardStr = super().getBoardStr()

        if self.isWinner(X) or self.isWinner(O):
            # No need to show a hint if a someone has won.
            return boardStr

        xCanWin = False
        oCanWin = False
        originalSpaces = self.spaces  # Backup spaces.
        for space in ALLspaces:  # Check each space:
            # Simulate X moving on this space:
            self.spaces = copy.copy(originalSpaces)
            if self.spaces[space] == BLANK:
                self.spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # Simulate O moving on this space:
            self.spaces = copy.copy(originalSpaces)
            if self.spaces[space] == BLANK:
                self.spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nX can win in one more move.'
        if oCanWin:
            boardStr += '\nO can win in one more move.'
        self.spaces = originalSpaces
        return boardStr


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.
