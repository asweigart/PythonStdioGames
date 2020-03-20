"""Hexapawn, by Al Sweigart al@inventwithpython.com

A pawn-only chess variant where you must try to move one of your
pawns to the opposite end of the board. You also win if you block
your opponent from making a move. The original Hexapawn had a 3x3
board with six pawns, but this program lets you use boards of any
size.

Based on Martin Gardner's puzzle.
More info at: https://en.wikipedia.org/wiki/Hexapawn"""
__version__ = 1

import sys

# Set up the constants:
X_PLAYER = 'x'
O_PLAYER = 'o'
EMPTY_SPACE = ' '
WIDTH = 'width'
HEIGHT = 'height'


def main():
    print("""Hexapawn, by Al Sweigart al@inventwithpython.com
    A pawn-only chess variant where you must try to move one of your
    pawns to the opposite end of the board. You also win if you block
    your opponent from making a move.

    Pawns can advance one space at a time (if they are not blocked by
    an opponent's pawn), and can capture pawns that are diagonally
    in front of them.
    """)

    width, height = getBoardSize()
    board = getNewBoard(width, height)
    turn = O_PLAYER
    while True:  # Main game loop.
        displayBoard(board)

        # Carry out the player's move:
        doPlayerMove(turn, board)
        if checkIfPlayerWon(turn, board):
            displayBoard(board)
            print(turn.upper(), 'has won!')
            print('Thanks for playing!')
            sys.exit()

        if turn == X_PLAYER:
            turn = O_PLAYER
        elif turn == O_PLAYER:
            turn = X_PLAYER


def getBoardSize():
    for dimension in [WIDTH, HEIGHT]:
        while True:  # Keep looping until the user enters a valid size.
            print('Enter the board', dimension, 'to play on:')
            response = input()

            if response.isdecimal() and (3 <= int(response) <= 26):
                if dimension == WIDTH:
                    width = int(response)
                elif dimension == HEIGHT:
                    height = int(response)
                break  # The user has entered a valid size.

            print('Please enter a number between 3 and 26.')

    # Display a warning if the user choose a size larger than 10.
    if width > 8 or height > 8:
        print('WARNING: You may have to resize the terminal window to')
        print('view a board this big.')

    return width, height


def getNewBoard(width, height):
    board = {WIDTH: width, HEIGHT: height}

    # Set up the X player's pieces at the top:
    for i in range(width):
        board[(i, 0)] = X_PLAYER

    # Set up the O player's pieces at the bottom:
    for i in range(width):
        board[(i, height - 1)] = O_PLAYER

    # Set up the rest of the spaces as blank:
    for x in range(width):
        for y in range(1, height - 1):
            board[(x, y)] = EMPTY_SPACE

    return board


def getNthLetter(nth):
    return chr(nth + 65)


def getNumberForNthLetter(letter):
    return ord(letter) - 65


def displayBoard(board):
    # Print the letter labels across the top:
    print('   ', end='')  # Print the indentation for the letter labels.
    for x in range(board[WIDTH]):
        print('  ', getNthLetter(x), ' ', sep='', end='')
    print()  # Print a newline.

    for y in range(board[HEIGHT]):
        # Print the horizontal border:
        print('   ', end='')  # Print the indentation.
        for x in range(board[WIDTH]):
            print('+---', end='')
        print('+')

        # Print the number labels on the left side:
        print(str(y + 1).rjust(2) + ' ', end='')

        # Print the board spaces:
        for x in range(board[WIDTH]):
            print('| ' + board[(x, y)] + ' ', end='')
        print('|', str(y + 1).ljust(2))

    # Print the last horizontal border at the very bottom:
    print('   ', end='')  # Print the indentation.
    for x in range(board[WIDTH]):
        print('+---', end='')
    print('+')

    # Print the letter labels across the bottom:
    print('   ', end='')  # Print the indentation for the letter labels.
    for x in range(board[WIDTH]):
        print('  ', chr(x + 65), ' ', sep='', end='')
    print()  # Print a newline.


def doPlayerMove(player, board):
    validMoves = getValidMoves(player, board)

    # Check if the player is blocked and can't make any moves:
    if len(validMoves) == 0:
        print(player.upper(), 'is blocked and cannot move!')
        if player == X_PLAYER:
            print('O has won!')
        elif player == O_PLAYER:
            print('X has won!')
        print('Thanks for playing!')
        sys.exit()

    print('It is player ' + player.upper() + '\'s turn.')
    print('Select which pawn you want to move:', ' '.join(validMoves))
    print('(Or enter QUIT to quit.)')
    while True:  # Keep looping until the player enters a valid move.
        selectedPawn = input().upper()

        if selectedPawn == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if selectedPawn in validMoves:
            break  # The user entered a valid move, so break.
        print('Enter the space label of one of your pawns.')  # TODO fix this message

    # Figure out which moves the selected pawn can make:
    x = getNumberForNthLetter(selectedPawn[0])
    y = int(selectedPawn[1]) - 1
    possibleMoves = []
    if pieceCanCaptureLeft(player, x, y, board):
        possibleMoves.append('L')
    if pieceCanAdvance(player, x, y, board):
        possibleMoves.append('A')
    if pieceCanCaptureRight(player, x, y, board):
        possibleMoves.append('R')

    if len(possibleMoves) != 1:
        # There are multiple possible moves, so ask the player which
        # move they want to make:
        print('Enter the move this pawn will make:')
        if 'L' in possibleMoves:
            print('(L)eft Capture ', end='')
        if 'A' in possibleMoves:
            print('(A)dvance Forward ', end='')
        if 'R' in possibleMoves:
            print('(R)ight Capture', end='')
        print()
        while True:  # Keep asking the player until they enter a valid move.
            move = input().upper()
            if move in possibleMoves:
                break
            print('Enter which move this pawn will take.')
    elif len(possibleMoves) == 1:
        # There's only one possible move, so automatically select it.
        move = possibleMoves[0]

    # Carry out this pawn's move:
    board[(x, y)] = EMPTY_SPACE
    if move == 'A':
        if player == X_PLAYER:
            board[(x, y + 1)] = X_PLAYER
        elif player == O_PLAYER:
            board[(x, y - 1)] = O_PLAYER
    elif move == 'L':
        if player == X_PLAYER:
            board[(x - 1, y + 1)] = X_PLAYER
        elif player == O_PLAYER:
            board[(x - 1, y - 1)] = O_PLAYER
    elif move == 'R':
        if player == X_PLAYER:
            board[(x + 1, y + 1)] = X_PLAYER
        elif player == O_PLAYER:
            board[(x + 1, y - 1)] = O_PLAYER



def getValidMoves(player, board):
    """Return a list of board space labels that have a player piece
    that can make a move."""
    validMoves = []
    for x in range(board[WIDTH]):
        for y in range(board[HEIGHT]):
            if board[(x, y)] == player:
                if pieceCanAdvance(player, x, y, board) or pieceCanCaptureLeft(player, x, y, board) or pieceCanCaptureRight(player, x, y, board):
                    validMoves.append(getNthLetter(x) + str(y + 1))
    return validMoves


def pieceCanAdvance(player, x, y, board):
    # Can this piece advance forward?
    if player == X_PLAYER: # X's "forward" is the space below.
        if (x, y + 1) in board and board[(x, y + 1)] == EMPTY_SPACE:
            return True
    elif player == O_PLAYER:  # O's "forward" is the space above.
        if (x, y - 1) in board and board[(x, y - 1)] == EMPTY_SPACE:
            return True
    return False


def pieceCanCaptureLeft(player, x, y, board):
    # Can this piece capture an opponent's piece?
    if player == X_PLAYER: # X's "forward" is the space below.
        # Check diagonally forward and left:
        if (x - 1, y + 1) in board and board[(x - 1, y + 1)] == O_PLAYER:
            return True
    elif player == O_PLAYER:  # O's "forward" is the space above.
        # Check diagonally forward and left:
        if (x - 1, y - 1) in board and board[(x - 1, y - 1)] == X_PLAYER:
            return True
    return False  # This piece cannot capture.


def pieceCanCaptureRight(player, x, y, board):
    # Can this piece capture an opponent's piece?
    if player == X_PLAYER: # X's "forward" is the space below.
        # Check diagonally forward and right:
        if (x + 1, y + 1) in board and board[(x + 1, y + 1)] == O_PLAYER:
            return True
    elif player == O_PLAYER:  # O's "forward" is the space above.
        # Check diagonally forward and right:
        if (x + 1, y - 1) in board and board[(x + 1, y - 1)] == X_PLAYER:
            return True
    return False  # This piece cannot capture.


def checkIfPlayerWon(player, board):
    if player == X_PLAYER:
        # Check if X has any pieces on the bottom row:
        for x in range(board['width']):
            if board[(x, board['height'] - 1)] == X_PLAYER:
                return True
        return False
    elif player == O_PLAYER:
        # Check if O has any pieces on the top row:
        for x in range(board['width']):
            if board[(x, 0)] == O_PLAYER:
                return True
        return False


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
