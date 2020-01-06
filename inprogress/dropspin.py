# Dropspin, by Al Sweigart al@inventwithpython.com

# TODO - check when puzzle is complete

import sys, random, copy

BLOCK_CHAR = chr(9608)

TOP_BLOCK = chr(9600) # Character 9600 is '▀'
BOTTOM_BLOCK = chr(9604) # Character 9604 is '▄'
FULL_BLOCK = chr(9608) # Character 9608 is '█'
NO_BLOCK = ' '

BORDER_CHAR = chr(9617) # Character 9617 is '░'.

FILLED = True
EMPTY = False


class DropspinBoard:
    def __init__(self, size):
        assert size % 2 == 0, 'Board size must be even.'
        assert size < 100, 'Board size must be less than 100.'
        self.size = size

        self.clear()


    def clear(self):
        self.board = {} # Keys are (x, y) tuples, values are Boolean.
        for column in range(self.size):
            for row in range(self.size):
                self.board[(column, row)] = EMPTY
        self.moves = []
        self.rememberBoard()


    def display(self):
        # Print the column labels:
        print(' ', end='') # Print a space to make room for the left edge border.
        for columnNumber in range(10, self.size + 1, 10):
            print((' ' * 9) + str(columnNumber // 10), end='')
        print() # Print a newline.
        print(' ', end='') # Print a space to make room for the left edge border.
        for columnNumber in range(1, self.size + 1):
            print(str(columnNumber % 10), end='')
        print() # Print a newline.

        # Print the top edge of the border:
        print(BORDER_CHAR * (self.size + 2))

        for row in range(0, self.size, 2):
            print(BORDER_CHAR, end='') # Print the left edge border.
            for column in range(self.size):
                if self.board[(column, row)] == FILLED and self.board[(column, row + 1)] == FILLED:
                    print(FULL_BLOCK, end='')
                elif self.board[(column, row)] == FILLED and self.board[(column, row + 1)] == EMPTY:
                    print(TOP_BLOCK, end='')
                elif self.board[(column, row)] == EMPTY and self.board[(column, row + 1)] == FILLED:
                    print(BOTTOM_BLOCK, end='')
                elif self.board[(column, row)] == EMPTY and self.board[(column, row + 1)] == EMPTY:
                    print(NO_BLOCK, end='')
                #if self.board[(column, row)]:
                #    print(BLOCK_CHAR, end='')
                #else:
                #    print('.', end='')
            print(BORDER_CHAR, end='') # Print the right edge border.
            print() # Print a newline.

        # Print the bottom edge of the border:
        print(BORDER_CHAR * (self.size + 2))


    def dropOnColumn(self, column):
        if self.board[(column, 0)] == FILLED:
            # This column is completely full, do nothing:
            return

        # Check if the column is entirely empty:
        columnIsEmpty = True
        for row in range(self.size):
            if self.board[(column, row)] == FILLED:
                columnIsEmpty = False
        if columnIsEmpty:
            # There are no blocks in this column, fill in the last one:
            self.board[(column, self.size - 1)] = FILLED
            self.rememberBoard()
            return

        # Find the first block from the top, and place a block above it:
        for row in range(1, self.size):
            if self.board[(column, row)] == FILLED:
                self.board[(column, row - 1)] = FILLED
                self.rememberBoard()
                return


    def rotateRight(self):
        rotatedBoard = {}
        for column in range(self.size):
            for row in range(self.size):
                rotatedBoard[(self.size - 1 - row, column)] = self.board[(column, row)]
        self.board = rotatedBoard

        self.rememberBoard()


    def rotateLeft(self):
        rotatedBoard = {}
        for column in range(self.size):
            for row in range(self.size):
                rotatedBoard[(row, self.size - 1 - column)] = self.board[(column, row)]
        self.board = rotatedBoard

        self.rememberBoard()


    def _generateRandom(self, steps=100):
        for i in range(steps):
            if random.randint(1, 5) == 1:
                self.rotateLeft()
            elif random.randint(1, 5) == 1:
                self.rotateRight()
            else:
                self.dropOnColumn(random.randint(0, self.size - 1))

    def rememberBoard(self):
        self.moves.append(copy.copy(self.board))

    def undo(self):
        #breakpoint()
        if len(self.moves) > 1:
            self.moves.pop()
            self.board = copy.copy(self.moves[-1])


'''
import random

b = DropspinBoard(10)
for i in range(100):
    if random.randint(1, 5) == 1:
        b.rotateLeft()
    elif random.randint(1, 5) == 1:
        b.rotateRight()
    else:
        b.dropOnColumn(random.randint(0, 9))
b.display()

sys.exit()
'''

print('''Dropspin, by Al Sweigart al@inventwithpython.com

A puzzle game where you must recreate the image shown by dropping blocks
in each column and spinning the image.
''')

target = DropspinBoard(8)
target._generateRandom(40)

board = DropspinBoard(8)
while True:
    #print('Try to make this board:')
    #target.display()
    #print()

    board.display()

    print('Moves: Q (rotate left), E (rotate right), U (undo),')
    print('C (clear), 1 to ' + str(board.size) + ', or QUIT to quit.')

    response = input().upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif response == 'Q':
        board.rotateLeft()
    elif response == 'E':
        board.rotateRight()
    elif response == 'U':
        board.undo()
    elif response == 'C':
        board.clear()
    elif not response.isdecimal():
        print('Please enter R or L, or a number 1 to', board.size)
    elif int(response) == 0 or int(response) > board.size:
        print('Please enter a number 1 to', board.size)
    else:
        board.dropOnColumn(int(response) - 1)
    print('\n' * 40)