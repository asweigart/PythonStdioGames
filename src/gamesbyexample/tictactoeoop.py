"""Tic Tac Toe (OOP), by Al Sweigart al@inventwithpython.com

The classic board game. (Object-oriented programming version.)
Tags: large, game, two-player, board game, object-oriented"""
__version__ = 1

import copy

ALL_SPACES = list('123456789') # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' ' # Constants for string values.

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = HintTTTBoard() # Create a TTT board object.
    currentPlayer, nextPlayer = X, O # X goes first, O goes next.

    while True: # Main game loop.
        print(gameBoard.getBoardStr()) # Display the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not gameBoard.isValidSpace(move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input()
        gameBoard.updateBoard(move, currentPlayer) # Make the move.

        # Check if the game is over:
        if gameBoard.isWinner(currentPlayer): # First check for victory.
            print(gameBoard.getBoardStr())
            print(currentPlayer + ' has won the game!')
            break
        elif gameBoard.isBoardFull(): # Next check for a tie.
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # Swap turns.
        # At this point, go back to the start of the main program loop.
    print('Thanks for playing!')

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic tac toe board."""
        self._spaces = {} # The board is represented as a Python dictionary.
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All spaces start as blank.

    def getBoardStr(self):
        """Return a text-representation of the board."""
        return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(self._spaces['1'], self._spaces['2'], self._spaces['3'], self._spaces['4'], self._spaces['5'], self._spaces['6'], self._spaces['7'], self._spaces['8'], self._spaces['9'])

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space number
        and the space is blank."""
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard."""
        s, p = self._spaces, player # Shorter names as "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((s['1'] == s['2'] == s['3'] == p) or # Across the top
                (s['4'] == s['5'] == s['6'] == p) or # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or # Down the left
                (s['2'] == s['5'] == s['8'] == p) or # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or # Down the right
                (s['3'] == s['5'] == s['7'] == p) or # Diagonal
                (s['1'] == s['5'] == s['9'] == p))   # Diagonal

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False # If a single space is blank, return False.
        return True # No spaces are blank, so return True.

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
          {}{}{} 789'''.format(self._spaces['1'], self._spaces['2'], self._spaces['3'], self._spaces['4'], self._spaces['5'], self._spaces['6'], self._spaces['7'], self._spaces['8'], self._spaces['9'])

        # Change '.' back to blank spaces.
        for space in ALL_SPACES:
            if self._spaces[space] == '.':
                self._spaces[space] = BLANK
        return boardStr

class HintTTTBoard(TTTBoard):
    def getBoardStr(self):
        """Return a text-representation of the board with hints."""
        boardStr = super().getBoardStr() # Call getBoardStr() in TTTBoard.

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces # Backup _spaces.
        for space in ALL_SPACES: # Check each space:
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





class PrettyTTTBoard(TTTBoard):
    def getBoardStr(self):
        canvas = {}
        # Draw the board lines:
        for i in range(17):
            canvas[(5, i)] = '#'
            canvas[(11, i)] = '#'
            canvas[(i, 5)] = '#'
            canvas[(i, 11)] = '#'

        # Draw the Xs and Os or space numbers:
        i = 0
        for y in (0, 6, 12):
            for x in (0, 6, 12):
                i += 1
                if self._spaces[str(i)] == X:
                    # Draw an X:
                    canvas[(1 + x, 1 + y)] = X
                    canvas[(3 + x, 1 + y)] = X
                    canvas[(2 + x, 2 + y)] = X
                    canvas[(1 + x, 3 + y)] = X
                    canvas[(3 + x, 3 + y)] = X
                elif self._spaces[str(i)] == O:
                    # Draw an O:
                    canvas[(1 + x, 1 + y)] = O
                    canvas[(2 + x, 1 + y)] = O
                    canvas[(3 + x, 1 + y)] = O
                    canvas[(1 + x, 2 + y)] = O
                    canvas[(3 + x, 2 + y)] = O
                    canvas[(1 + x, 3 + y)] = O
                    canvas[(2 + x, 3 + y)] = O
                    canvas[(3 + x, 3 + y)] = O
                else:
                    # Draw the space number label:
                    canvas[(2 + x, 2 + y)] = str(i)

        # Print the canvas on the screen:
        boardStrAsList = [] # Print a blank line as a spacer.
        for y in range(17):
            for x in range(17):
                if (x, y) in canvas:
                    boardStrAsList.append(canvas[(x, y)])
                else:
                    boardStrAsList.append(' ')
            boardStrAsList.append('\n')
        return ''.join(boardStrAsList)


class LoggingTTTBoard(TTTBoard):
    def __init__(self, logFilename):
        """Create a new, blank tic tac toe board."""
        super().__init__()
        self.logFilename = logFilename

    def updateBoard(self, space, player):
        """Sets the space on the board to player, but also records each move
        to the log file."""
        super().updateBoard(space, player)
        with open(self.logFilename, 'a') as logFile:
            logFile.write('{} moved on space {}:\n'.format(player, space))
            logFile.write(super().getBoardStr() + '\n')


class LoggingPrettyTTTBoard(LoggingTTTBoard, PrettyTTTBoard):
    def __init__(self, crossChar, logFilename):
        self.logFilename = logFilename
        PrettyTTTBoard.__init__(self, crossChar)


if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
