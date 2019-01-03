import random

ODD_DARK_COLUMNS = 'BDFH'
EVEN_DARK_COLUMNS = 'ACEG'
EMPTY = '.'

def getNewBoard():
    # Set up the board data structure with empty spaces.
    board = {}
    for row in range(1, 9):
        if row % 2 == 0:
            for column in EVEN_DARK_COLUMNS:
                board[column + str(row)] = EMPTY
        else:
            for column in ODD_DARK_COLUMNS:
                board[column + str(row)] = EMPTY

    # Place the starting pieces for player X at the top:
    for space in 'B1 D1 F1 H1 A2 C2 E2 G2 B3 D3 F3 H3'.split():
        board[space] = 'x'

    # Place the starting pieces for player O at the bottom:
    for space in 'A6 C6 E6 G6 B7 D7 F7 H7 A8 C8 E8 G8'.split():
        board[space] = 'o'

    return board


def drawBoard(board):
    spaces = []

    for row in range(1, 9):
        if row % 2 == 0:
            for column in EVEN_DARK_COLUMNS:
                for i in range(3):
                    cell = board[column + str(row)]
                    spaces.append(cell) # The top/bottom part of the cell has 1 {}.
                    if i == 1:
                        spaces.append(cell) # The middle part of the cell has 3 {}.
                        spaces.append(cell)
        else:
            for column in ODD_DARK_COLUMNS:
                for i in range(3):
                    cell = board[column + str(row)]
                    spaces.append(cell) # The top/bottom part of the cell has 1 {}.
                    if i == 1:
                        spaces.append(cell) # The middle part of the cell has 3 {}.
                        spaces.append(cell)

    print("""
    A   B   C   D   E   F   G   H
  +---+---+---+---+---+---+---+---+
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
1 |   |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}| 1
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
  +---+---+---+---+---+---+---+---+
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
2 |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}|   | 2
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
  +---+---+---+---+---+---+---+---+
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
3 |   |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}| 3
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
  +---+---+---+---+---+---+---+---+
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
4 |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}|   | 4
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
  +---+---+---+---+---+---+---+---+
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
5 |   |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}| 5
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
  +---+---+---+---+---+---+---+---+
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
6 |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}|   | 6
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
  +---+---+---+---+---+---+---+---+
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
7 |   |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}| 7
  |   |.{}.|   |.{}.|   |.{}.|   |.{}.|
  +---+---+---+---+---+---+---+---+
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
8 |{}{}{}|   |{}{}{}|   |{}{}{}|   |{}{}{}|   | 8
  |.{}.|   |.{}.|   |.{}.|   |.{}.|   |
  +---+---+---+---+---+---+---+---+
    A   B   C   D   E   F   G   H""".format(*spaces))


def getMove(board, turn):
    assert turn in ('X', 'O')
    moves = []
    for i in range(3):
        if random.randint(0, 1) == 0:
            moves.append('x')
        else:
            moves.append('o')
    print('Available Moves:', ' '.join(moves))

    # Get possible pieces to select:
    possibleFrom = []
    for row in range(1, 9):
        if row % 2 == 0:
            for column in EVEN_DARK_COLUMNS:
                if board[str(row) + column].upper() == turn:
                    possibleFrom.append(str(row) + column)

    while True: # Loop until a valid "from" space is selected.
        print('Player {}, select your piece to move:', ' '.join(possibleFrom))
        move = input()
        if move in possibleFrom:
            break
        if len(move) == 2 and move[1] + move[0] in possibleFrom:
            # Player entered the coordinates backwards, fix it and move on.
            move = move[1] + move[0]
            break


    while True: # Loop until a valid "to" space is selected.
        pass



def getValidMoves(board, fromSpace, toSpace):
    assert board[fromSpace] in ('X', 'x', 'O', 'o')
    isX = board[fromSpace] in ('X', 'x')

    # LEFT OFF





drawBoard(getNewBoard())