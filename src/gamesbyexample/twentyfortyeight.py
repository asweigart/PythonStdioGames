"""2048 Game, by Al Sweigart al@inventwithpython.com

A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.
More info at https://en.wikipedia.org/wiki/2048_(video_game)
Tags: large, game, puzzle game"""
__version__ = 0
import random, sys

# Set up the constants:
BLANK = ''  # A value that represents a blank space on the board.


def main():
    """Run a single game of 2048."""
    print("""2048
By Al Sweigart al@inventwithpython.com
""")

    gameBoard = getNewBoard()

    while True:  # Main game loop.
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = getPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()
        # At this point, go back to the start of the main game loop.


def getNewBoard():
    """Returns a new data structure that represents a board.

    It's a dictionary with keys of (x, y) tuples and values of the tile
    at that space. The tile is either a power-of-two integer or BLANK.
    The coordinates are laid out as:
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""

    newBoard = {}  # Contains the board data structure to be returned.
    # Loop over every possible space and set all the tiles to blank:
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # Pick two random spaces for the two starting 2's:
    startingTwosPlaced = 0  # The number of starting spaces picked.
    while startingTwosPlaced < 2:  # Repeat, in case of duplicate spaces.
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # Make sure the randomly selected space isn't already taken:
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1

    return newBoard


def drawBoard(board):
    """Draws the board data structure on the screen."""

    # Go through each possible space left-to-right, top-to-bottom, and
    # create a list of what each space's label should be.
    labels = []  # A list of strings for the number/blank for that tile.
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]  # Get the tile at this space.
            # Make sure the label is 5 spaces long:
            labelForThisTile = str(tile).center(5)
            labels.append(labelForThisTile)

    # The {} are replaced with the label for that tile:
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
""".format(*labels))


def getScore(board):
    """Returns the sum of all the tiles on the board data structure."""
    score = 0
    # Loop over every space and add the tile to the score:
    for x in range(4):
        for y in range(4):
            # Only add non-blank tiles to the score:
            if board[(x, y)] != BLANK:
                score = score + board[(x, y)]
    return score


def combineTilesInColumn(column):
    """The column is a list of four tile. Index 0 is the "bottom" of
    the column, and tiles are pulled "down" and combine if they are the
    same. For example, combineTilesInColumn([2, BLANK, 2, BLANK])
    returns [4, BLANK, BLANK, BLANK]."""

    # Copy only the numbers (not blanks) from column to combinedTiles
    combinedTiles = []  # A list of the non-blank tiles in column.
    for i in range(4):
        if column[i] != BLANK:
            combinedTiles.append(column[i])

    # Keep adding blanks until there are 4 tiles:
    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    # Combine numbers if the one "above" it is the same, and double it.
    for i in range(3):  # Skip index 3: it's the topmost space.
        if combinedTiles[i] == combinedTiles[i + 1]:
            combinedTiles[i] *= 2  # Double the number in the tile.
            # Move the tiles above it down one space:
            for aboveIndex in range(i + 1, 3):
                combinedTiles[aboveIndex] = combinedTiles[aboveIndex + 1]
            combinedTiles[3] = BLANK  # Topmost space is always BLANK.
    return combinedTiles


def makeMove(board, move):
    """Carries out the move on the board.

    The move argument is either 'W', 'A', 'S', or 'D' and the function
    returns the resulting board data structure."""

    # The board is split up into four columns, which are different
    # depending on the direction of the move:
    if move == 'W':
        allColumnsSpaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                            [(1, 0), (1, 1), (1, 2), (1, 3)],
                            [(2, 0), (2, 1), (2, 2), (2, 3)],
                            [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        allColumnsSpaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                            [(0, 1), (1, 1), (2, 1), (3, 1)],
                            [(0, 2), (1, 2), (2, 2), (3, 2)],
                            [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        allColumnsSpaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                            [(1, 3), (1, 2), (1, 1), (1, 0)],
                            [(2, 3), (2, 2), (2, 1), (2, 0)],
                            [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        allColumnsSpaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                            [(3, 1), (2, 1), (1, 1), (0, 1)],
                            [(3, 2), (2, 2), (1, 2), (0, 2)],
                            [(3, 3), (2, 3), (1, 3), (0, 3)]]

    boardAfterMove = {}  # The board data structure after making the move.
    for columnSpaces in allColumnsSpaces:  # Loop over all 4 columns.
        # Get the tiles of this column (The first tile is the "bottom"
        # of the column):
        firstTileSpace = columnSpaces[0]
        secondTileSpace = columnSpaces[1]
        thirdTileSpace = columnSpaces[2]
        fourthTileSpace = columnSpaces[3]

        firstTile = board[firstTileSpace]
        secondTile = board[secondTileSpace]
        thirdTile = board[thirdTileSpace]
        fourthTile = board[fourthTileSpace]

        # Form the column and combine the tiles in it:
        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combineTilesInColumn(column)

        # Set up the new board data structure with the combined tiles:
        boardAfterMove[firstTileSpace] = combinedTilesColumn[0]
        boardAfterMove[secondTileSpace] = combinedTilesColumn[1]
        boardAfterMove[thirdTileSpace] = combinedTilesColumn[2]
        boardAfterMove[fourthTileSpace] = combinedTilesColumn[3]

    return boardAfterMove


def getPlayerMove():
    """Asks the player for the direction of their next move (or quit).

    Ensures they enter a valid move: either 'W', 'A', 'S' or 'D'."""
    print('Enter move: (WASD or Q to quit)')
    while True:  # Keep looping until they enter a valid move.
        move = input('> ').upper()
        if move == 'Q':
            # End the program:
            print('Thanks for playing!')
            sys.exit()

        # Either return the valid move, or loop back and ask again:
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print('Enter one of "W", "A", "S", "D", or "Q".')
        # At this point, go back to the start of the loop.


def addTwoToBoard(board):
    """Adds a new 2 tile randomly to the board."""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return  # Return after finding one non-blank tile.


def isFull(board):
    """Returns True if the board data structure has no blanks."""
    # Loop over every space on the board:
    for x in range(4):
        for y in range(4):
            # If a space is blank, return False:
            if board[(x, y)] == BLANK:
                return False
    return True  # No space is blank, so return True.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
