"""Parking Valet, by Al Sweigart al@inventwithpython.com
A sliding tile puzzle game to move cars out of the way.
Inspired by Nob Yoshihagara's Rush Hour.
parkingvaletpuzzle.txt generated from puzzles by Michael Fogleman.
Download it from https://inventwithpython.com/parkingvaletpuzzles.txt
More info at https://www.michaelfogleman.com/rush/
This and other games are available at https://nostarch.com/XX
Tags: large, board game, game, puzzle"""
__version__ = 0
import math, random, sys

# Set up the constants:
EMPTY_SPACE = '.'
WALL = chr(9617)  # Character 9617 is '░'


def main():
    print("""Parking Valet, by Al Sweigart al@inventwithpython.com
Original Rush Hour game by Nob Yoshihagara.
Puzzles by Michael Fogleman.

Get the "A" car to the right edge of the board.
Enter moves as <car letter><direction>.
Directions are (L)eft, (R)ight, (U)p, and (D)own.
""")
    input('Press Enter to begin...')

    puzzle = getRandomPuzzle()
    gameBoard = getBoard(puzzle)  # Start a new puzzle boad.
    while True:
        print('\n' * 60)  # "Clear" the screen by printing many newlines.
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        if playerMove == 'RESET':
            gameBoard = getBoard(puzzle)  # Restore the original board.
        else:
            makeMove(gameBoard, playerMove)
        if hasWon(gameBoard):
            displayBoard(gameBoard)
            print()
            print('PUZZLE COMPLETE!')
            sys.exit()


def getRandomPuzzle():
    """Return a string representing a randomly selected puzzle. Here are
    three example puzzles from parkingvaletpuzzles.txt:
    BB.K..GI.KCCGIAAL.HDD.LMH.JEEMFFJ...
    ..BB.X...KDDAA.KL.HIEEL.HIJFFFGGJ...
    .EBBIK.EFGIKAAFGJL..F.JLD..H..DCCH..
    """
    numberOfPuzzles = 0
    puzzleFile = open('parkingvaletpuzzles.txt')
    while puzzleFile.readline():
        numberOfPuzzles += 1
    puzzleFile.close()

    randomPuzzleNum = random.randint(1, numberOfPuzzles)
    counter = 1
    puzzleFile = open('parkingvaletpuzzles.txt')
    while True:
        if counter == randomPuzzleNum:
            return puzzleFile.readline()
        else:
            puzzleFile.readline()
            counter += 1


def getBoard(puzzleAsString):
    """Return a board data structure based on the puzzle string."""
    # Set up data structure.
    board = {}

    # We assume that the puzzles are square shaped:
    board['width'] = int(math.sqrt(len(puzzleAsString)))
    board['height'] = int(math.sqrt(len(puzzleAsString)))

    x = 0
    y = 0
    for character in puzzleAsString:
        if character == 'X':
            # Draw walls using the block character instead of x:
            character = WALL
        board[(x, y)] = character

        if x == board['width'] - 1:
            y += 1
            x = 0
        else:
            x += 1
    return board


def displayBoard(board):
    """Display the board on the screen."""
    for y in range(board['height']):
        for i in range(3):  # We draw 3 rows per board-row.
            if i == 0 and y != 0:
                # Draw a horizontal dividing line:
                for x in range(board['width']):
                    if (board[(x, y)] != EMPTY_SPACE
                        and board[(x, y)] == board[(x, y - 1)]):
                            # Draw car in dividing line:
                            print(board[(x, y)] * 3 + ' ', end='')
                    else:
                        # Draw empty dividing line:
                        print(' ' * 4, end='')
                print()

            for x in range(board['width']):
                # Draw the board space:
                print(board[(x, y)] * 3, end='')

                if (x != board['width'] - 1
                    and board[(x, y)] != EMPTY_SPACE
                    and board[(x, y)] == board[(x + 1, y)]):
                        # Draw car in vertical dividing line:
                        print(board[(x, y)], end='')
                else:
                    # Draw empty vertical dividing line:
                    print(' ', end='')
            print()


def getValidMoves(board):
    """Return a list of valid moves that can be made on the board."""
    validMoves = []
    for x in range(board['width']):
        for y in range(board['height']):
            if board[(x, y)] in (EMPTY_SPACE, WALL):
                continue  # Skip this empty or wall space.

            xNotOnLeftEdge = x != 0
            xNotOnRightEdge = x != board['width'] - 1
            yNotOnTopEdge = y != 0
            yNotOnBottomEdge = y != board['height'] - 1

            # Check if the car at x, y can move down.
            if (yNotOnTopEdge
                and board[(x, y)] == board[(x, y - 1)]
                and y + 1 < board['height']
                and board[(x, y + 1)] == EMPTY_SPACE):
                    validMoves.append(board[(x, y)] + 'D')

            # Check if the car at x, y can move up.
            if (yNotOnBottomEdge
                and board[(x, y)] == board[(x, y + 1)]
                and y - 1 >= 0
                and board[(x, y - 1)] == EMPTY_SPACE):
                    validMoves.append(board[(x, y)] + 'U')

            # Check if the car at x, y can move right.
            if (xNotOnLeftEdge
                and board[(x, y)] == board[(x - 1, y)]
                and x + 1 < board['width']
                and board[(x + 1, y)] == EMPTY_SPACE):
                    validMoves.append(board[(x, y)] + 'R')

            # Check if the car at x, y can move left.
            if (xNotOnRightEdge
                and board[(x, y)] == board[(x + 1, y)]
                and x - 1 >= 0
                and board[(x - 1, y)] == EMPTY_SPACE):
                    validMoves.append(board[(x, y)] + 'L')

    return validMoves


def makeMove(board, move):
    """Carry out a move on the given board."""
    validMoves = getValidMoves(board)
    if move not in validMoves:
        return False

    car = move[0]
    direction = move[1]

    newCarPositions = []

    for x in range(board['width']):
        for y in range(board['height']):
            if board[(x, y)] == car:
                board[(x, y)] = '.'
                if direction == 'U':
                    newCarPositions.append((x, y - 1))
                elif direction == 'D':
                    newCarPositions.append((x, y + 1))
                elif direction == 'L':
                    newCarPositions.append((x - 1, y))
                elif direction == 'R':
                    newCarPositions.append((x + 1, y))

    for newCarPosition in newCarPositions:
        board[newCarPosition] = car


def hasWon(board):
    """Return True if the 'A' car has reached the right edge."""
    # The puzzle is solved when the 'A' car reaches the right edge.
    for y in range(board['height']):
        if board[(board['width'] - 1, y)] == 'A':
            return True

    return False


def askForPlayerMove(board):
    """Let the player enter the car and direction they want to move."""
    validMoves = getValidMoves(board)
    while True:
        allValidMoves = '", "'.join(validMoves)
        print('Moves: "{}", "RESET", or "QUIT".'.format(allValidMoves))
        move = input('> ').upper()
        if move == 'QUIT':
            sys.exit()
        if move == 'RESET':
            return 'RESET'
        if move in validMoves:
            return move


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
