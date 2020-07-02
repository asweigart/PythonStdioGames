"""Tic-Tac-Toe (OOP), by Al Sweigart al@inventwithpython.com
The classic board game. (Object-oriented programming version.)
This and other games are available at https://nostarch.com/XX
Tags: large, board game, game, object-oriented, two-player"""
__version__ = 0
import copy

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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
        # Keys are 1 through 9, the values are X, O, or BLANK. THe
        # leading underscore in _spaces means it is "private". Private
        # variables are only modified/read by code within the class
        # that contains them, rather than code anywhere in the program.
        # This way, we can know that bugs involving _spaces are likely
        # caused by buggy code somewhere in the TTTBoard class, rather
        # than anywhere in program. (This is helpful as our programs
        # become enormous.)
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK  # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(self._spaces['1'], self._spaces['2'],
        self._spaces['3'], self._spaces['4'], self._spaces['5'],
        self._spaces['6'], self._spaces['7'], self._spaces['8'],
        self._spaces['9'])

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space
        number and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        # Shorter variable names used here for readablility:
        s, p = self._spaces, player
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
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False  # If any space is blank, return False.
        return True  # No spaces are blank, so return True.

    def updateBoard(self, space, player):
        """Sets the space on the board to player."""
        self._spaces[space] = player


class MiniTTTBoard(TTTBoard):
    def getBoardStr(self):
        """Return a tiny text-representation of the board."""
        # Change blank spaces to a '.'
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = '.'

        boardStr = '''
          {}{}{} 123
          {}{}{} 456
          {}{}{} 789'''.format(self._spaces['1'], self._spaces['2'],
            self._spaces['3'], self._spaces['4'], self._spaces['5'],
            self._spaces['6'], self._spaces['7'], self._spaces['8'],
            self._spaces['9'])

        # Change '.' back to blank spaces.
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK
        return boardStr


class HintTTTBoard(TTTBoard):
    def getBoardStr(self):
        """Return a text-representation of the board with hints."""
        # Call getBoardStr() in the parent/super class, TTTBoard.
        boardStr = super().getBoardStr()

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces  # Backup _spaces.
        for space in ALL_SPACES:  # Check each space:
            # Simulate X moving on this space:
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            # Simulate O moving on this space:
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += '\nX can win in one more move.'
        if oCanWin:
            boardStr += '\nO can win in one more move.'
        self._spaces = originalSpaces
        return boardStr


if __name__ == '__main__':
    main()  # Call main() if this module is run, but not when imported.
