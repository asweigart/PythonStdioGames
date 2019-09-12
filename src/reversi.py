# Reversi, by Al Sweigart al@inventwithpython.com
# Also called Othello, this is a tile flipping game.
# https://en.wikipedia.org/wiki/Reversi
# A version of this game is featured in the book, "Invent Your Own Computer
# Games with Python. https://nostarch.com/inventwithpython

import random, sys

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    scores = {'X': 0, 'O': 0}
    for x in range(8):
        for y in range(8):
            if board[(x, y)] in ('X', 'O'):
                scores[board[(x, y)]] += 1
    return scores


def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    print('  12345678')
    print(' +--------+')
    for y in range(8):
        print(f'{(y+1)}|', end='')
        for x in range(8):
            print(board[(x, y)], end='')
        print('|')
    print(' +--------+')
    # Prints out the current score.
    scores = getScoreOfBoard(board)
    print(f'X has {scores["X"]} points. O has {scores["O"]} points.')


def getNewBoard():
    # Blanks out the board it is passed, except for the original starting position.
    board = {}
    for x in range(8):
        for y in range(8):
            board[(x, y)] = ' '

    # Starting pieces:
    board[(3, 3)] = 'X'
    board[(3, 4)] = 'O'
    board[(4, 3)] = 'O'
    board[(4, 4)] = 'X'
    return board


def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[(xstart, ystart)] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[(xstart, ystart)] = tile # temporarily set the tile on the board.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[(x, y)] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[(x, y)] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[(x, y)] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[(xstart, ystart)] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[(x, y)] = '.'
    return dupeBoard


def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def enterPlayerTile():
    # Let's the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # the first element in the list is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[(xstart, ystart)] = tile
    for x, y in tilesToFlip:
        board[(x, y)] = tile
    return True


def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate.
    dupeBoard = {}

    for x in range(8):
        for y in range(8):
            dupeBoard[(x, y)] = board[(x, y)]

    return dupeBoard


def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Returns the move as [x, y] (or returns the string 'quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, or type quit to end the game.')
        move = input().lower()
        if move == 'quit':
            return 'quit'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')

    return [x, y]


def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def main():
    # Reset the board and game.
    mainBoard = getNewBoard()
    playerTile, computerTile = enterPlayerTile()
    isPlayersTurn = True

    while True:
        if getValidMoves(mainBoard, 'X') == [] and getValidMoves(mainBoard, 'O') == []:
            break # Neither player can move, so quit.

        if isPlayersTurn: # Player's turn:
            drawBoard(getBoardWithValidMoves(mainBoard, playerTile))
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                sys.exit() # terminate the program
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
        elif not isPlayersTurn: # Computer's turn:
            drawBoard(mainBoard)
            input('Press Enter to see the computer\'s move.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)

        isPlayersTurn = not isPlayersTurn

    # Display the final board and score.
    drawBoard(mainBoard)
    print('Good game!')

if __name__ == '__main__':
    main()