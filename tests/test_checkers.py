import pytest
import sys
import io
import random
from gamesbyexample import checkers


def test_main(capsys):
    pass # TODO


def test_getNewBoard():
    assert checkers.getNewBoard() == {'B1': 'x', 'D1': 'x', 'F1': 'x', 'H1': 'x', 'A2': 'x', 'C2': 'x', 'E2': 'x', 'G2': 'x', 'B3': 'x', 'D3': 'x', 'F3': 'x', 'H3': 'x', 'A4': ' ', 'C4': ' ', 'E4': ' ', 'G4': ' ', 'B5': ' ', 'D5': ' ', 'F5': ' ', 'H5': ' ', 'A6': 'o', 'C6': 'o', 'E6': 'o', 'G6': 'o', 'B7': 'o', 'D7': 'o', 'F7': 'o', 'H7': 'o', 'A8': 'o', 'C8': 'o', 'E8': 'o', 'G8': 'o'}


def test_displayBoard(capsys):
    board = checkers.getNewBoard()
    checkers.displayBoard(board)
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
    assert checkers.prevCol('A') == ''
    assert checkers.prevCol('B') == 'A'
    assert checkers.prevCol('C') == 'B'
    assert checkers.prevCol('D') == 'C'
    assert checkers.prevCol('E') == 'D'
    assert checkers.prevCol('F') == 'E'
    assert checkers.prevCol('G') == 'F'
    assert checkers.prevCol('H') == 'G'

def test_nextCol():
    assert checkers.nextCol('A') == 'B'
    assert checkers.nextCol('B') == 'C'
    assert checkers.nextCol('C') == 'D'
    assert checkers.nextCol('D') == 'E'
    assert checkers.nextCol('E') == 'F'
    assert checkers.nextCol('F') == 'G'
    assert checkers.nextCol('G') == 'H'
    assert checkers.nextCol('H') == ''


def test_otherCheckers():
    assert checkers.otherCheckers('x') == ('o', 'O')
    assert checkers.otherCheckers('X') == ('o', 'O')
    assert checkers.otherCheckers('o') == ('x', 'X')
    assert checkers.otherCheckers('O') == ('x', 'X')


def test_getPossibleDstMoves():
    board = checkers.getNewBoard()
    moves, captures = checkers.getPossibleDstMoves(board, 'B3')
    assert set(moves) == set(['A4', 'C4'])
    assert set(captures) == set([])


def test_getPlayerMove():
    board = checkers.getNewBoard()
    sys.stdin = io.StringIO('B3\nA4\n')
    assert checkers.getPlayerMove(board, 'X') == ('B3', 'A4')

    # Test quitting:
    board = checkers.getNewBoard()
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        checkers.getPlayerMove(board, 'X')

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        checkers.getPlayerMove(board, 'X')

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        checkers.getPlayerMove(board, 'X')

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        checkers.getPlayerMove(board, 'X')


def test_makeMove():
    board = checkers.getNewBoard()
    board = checkers.makeMove(board, 'B3', 'A4')
    assert board['B3'] == checkers.EMPTY
    assert board['A4'] == 'x'

    board = checkers.getNewBoard()
    board['B3'] = checkers.EMPTY
    board['D5'] = 'x'
    board = checkers.makeMove(board, 'E6', 'C4')
    assert board['E6'] == checkers.EMPTY
    assert board['C4'] == 'o'
    assert board['D5'] == checkers.EMPTY


def test_hasLost():
    board = checkers.getNewBoard()
    for space, checker in board.items():
        if checker in ('x', 'X'):
            board[space] = checkers.EMPTY

    assert checkers.hasLost(board, 'X') == True
    assert checkers.hasLost(board, 'O') == False


