import pytest
import sys
import io
from gamesbyexample import chancecheckers


def test_main(capsys):
    pass # TODO


def test_getNewBoard():
    assert chancecheckers.getNewBoard() == {'B1': 'x', 'D1': 'x', 'F1': 'x', 'H1': 'x', 'A2': 'x', 'C2': 'x', 'E2': 'x', 'G2': 'x', 'B3': 'x', 'D3': 'x', 'F3': 'x', 'H3': 'x', 'A4': ' ', 'C4': ' ', 'E4': ' ', 'G4': ' ', 'B5': ' ', 'D5': ' ', 'F5': ' ', 'H5': ' ', 'A6': 'o', 'C6': 'o', 'E6': 'o', 'G6': 'o', 'B7': 'o', 'D7': 'o', 'F7': 'o', 'H7': 'o', 'A8': 'o', 'C8': 'o', 'E8': 'o', 'G8': 'o'}


def test_displayBoard(capsys):
    board = chancecheckers.getNewBoard()
    chancecheckers.displayBoard(board)
    captured = capsys.readouterr()

    lines = [
            '      A   B   C   D   E   F   G   H',
            '    +---+---+---+---+---+---+---+---+',
            '  1 |   | x |   | x |   | x |   | x | 1',
            '  2 | x |   | x |   | x |   | x |   | 2',
            '  3 |   | x |   | x |   | x |   | x | 3',
            '  4 |   |   |   |   |   |   |   |   | 4',
            '  5 |   |   |   |   |   |   |   |   | 5',
            '  6 | o |   | o |   | o |   | o |   | 6',
            '  7 |   | o |   | o |   | o |   | o | 7',
            '  8 | o |   | o |   | o |   | o |   | 8',
            ]
    for line in lines:
        assert line in captured.out


def test_prevCol():
    assert chancecheckers.prevCol('A') == ''
    assert chancecheckers.prevCol('B') == 'A'
    assert chancecheckers.prevCol('C') == 'B'
    assert chancecheckers.prevCol('D') == 'C'
    assert chancecheckers.prevCol('E') == 'D'
    assert chancecheckers.prevCol('F') == 'E'
    assert chancecheckers.prevCol('G') == 'F'
    assert chancecheckers.prevCol('H') == 'G'

def test_nextCol():
    assert chancecheckers.nextCol('A') == 'B'
    assert chancecheckers.nextCol('B') == 'C'
    assert chancecheckers.nextCol('C') == 'D'
    assert chancecheckers.nextCol('D') == 'E'
    assert chancecheckers.nextCol('E') == 'F'
    assert chancecheckers.nextCol('F') == 'G'
    assert chancecheckers.nextCol('G') == 'H'
    assert chancecheckers.nextCol('H') == ''


def test_otherCheckers():
    assert chancecheckers.otherCheckers('x') == ('o', 'O')
    assert chancecheckers.otherCheckers('X') == ('o', 'O')
    assert chancecheckers.otherCheckers('o') == ('x', 'X')
    assert chancecheckers.otherCheckers('O') == ('x', 'X')


def test_getPossibleDstMoves():
    board = chancecheckers.getNewBoard()
    moves, captures = chancecheckers.getPossibleDstMoves(board, 'B3')
    assert set(moves) == set(['A4', 'C4'])
    assert set(captures) == set([])


def test_getPlayerMove():
    board = chancecheckers.getNewBoard()
    sys.stdin = io.StringIO('B3\nA4\n')
    assert chancecheckers.getPlayerMove(board, 'X', ['x', 'x', 'o']) == ('B3', 'A4')

    # Test quitting:
    board = chancecheckers.getNewBoard()
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        chancecheckers.getPlayerMove(board, 'X', ['x', 'x', 'o'])

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        chancecheckers.getPlayerMove(board, 'X', ['x', 'x', 'o'])

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        chancecheckers.getPlayerMove(board, 'X', ['x', 'x', 'o'])

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        chancecheckers.getPlayerMove(board, 'X', ['x', 'x', 'o'])


def test_makeMove():
    board = chancecheckers.getNewBoard()
    board = chancecheckers.makeMove(board, 'B3', 'A4')
    assert board['B3'] == chancecheckers.EMPTY
    assert board['A4'] == 'x'

    board = chancecheckers.getNewBoard()
    board['B3'] = chancecheckers.EMPTY
    board['D5'] = 'x'
    board = chancecheckers.makeMove(board, 'E6', 'C4')
    assert board['E6'] == chancecheckers.EMPTY
    assert board['C4'] == 'o'
    assert board['D5'] == chancecheckers.EMPTY


def test_hasLost():
    board = chancecheckers.getNewBoard()
    for space, checker in board.items():
        if checker in ('x', 'X'):
            board[space] = chancecheckers.EMPTY

    assert chancecheckers.hasLost(board, 'X') == True
    assert chancecheckers.hasLost(board, 'O') == False


