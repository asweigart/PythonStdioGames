import pytest
import sys
import io
from gamesbyexample import fourinarow

def test_isWinner():
    for x in range(fourinarow.BOARD_WIDTH):
        for y in range(fourinarow.BOARD_HEIGHT):
            if y < fourinarow.BOARD_HEIGHT - 3:
                b = fourinarow.getNewBoard()
                b[(x, y)] = 'X'
                b[(x, y+1)] = 'X'
                b[(x, y+2)] = 'X'
                b[(x, y+3)] = 'X'
                fourinarow.displayBoard(b)
                #input()
                assert fourinarow.isWinner('X', b)

            if x < fourinarow.BOARD_WIDTH - 3:
                b = fourinarow.getNewBoard()
                b[(x, y)] = 'X'
                b[(x+1, y)] = 'X'
                b[(x+2, y)] = 'X'
                b[(x+3, y)] = 'X'
                fourinarow.displayBoard(b)
                #input()
                assert fourinarow.isWinner('X', b)

            if (x < fourinarow.BOARD_WIDTH - 3) and (y < fourinarow.BOARD_HEIGHT - 3):
                b = fourinarow.getNewBoard()
                b[(x, y)] = 'X'
                b[(x+1, y+1)] = 'X'
                b[(x+2, y+2)] = 'X'
                b[(x+3, y+3)] = 'X'
                fourinarow.displayBoard(b)
                #input()
                assert fourinarow.isWinner('X', b)

                b = fourinarow.getNewBoard()
                b[(x, y+3)] = 'X'
                b[(x+1, y+2)] = 'X'
                b[(x+2, y+1)] = 'X'
                b[(x+3, y)] = 'X'
                fourinarow.displayBoard(b)
                #input()
                assert fourinarow.isWinner('X', b)

def test_isFull():
    b = fourinarow.getNewBoard()
    for x in range(fourinarow.BOARD_WIDTH):
        for y in range(fourinarow.BOARD_HEIGHT):
            b[(x, y)] = 'X'

    fourinarow.displayBoard(b)
    assert fourinarow.isFull(b)

    for x in range(fourinarow.BOARD_WIDTH):
        for y in range(fourinarow.BOARD_HEIGHT):
            b[(x, y)] = fourinarow.EMPTY_SPACE
            assert not fourinarow.isFull(b)
            b[(x, y)] = 'X'


def test_getNewBoard():
    b1 = fourinarow.getNewBoard()
    b2 = fourinarow.getNewBoard()
    assert b1 == b2
    b1[(0,0)] = 'X'
    b1 == b2


def test_getPlayerMove():
    blankBoard = fourinarow.getNewBoard()

    # Test valid moves:
    for i in range(1, 8):
        sys.stdin = io.StringIO(str(i) + '\n')
        assert fourinarow.getPlayerMove('X', blankBoard) == (i - 1, 5)

    # Test quitting:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        fourinarow.getPlayerMove('X', blankBoard)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        fourinarow.getPlayerMove('X', blankBoard)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        fourinarow.getPlayerMove('X', blankBoard)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        fourinarow.getPlayerMove('X', blankBoard)

    # Test invalid move:
    sys.stdin = io.StringIO('invalid\n1\n')
    assert fourinarow.getPlayerMove('X', blankBoard) == (0, 5)

    # Test stacking move:
    board = fourinarow.getNewBoard()
    board[(0, 5)] = 'X'
    board[(0, 4)] = 'X'
    board[(0, 3)] = 'X'
    sys.stdin = io.StringIO('1\n')
    assert fourinarow.getPlayerMove('X', board) == (0, 2)

    # Test when the column is full:
    board = fourinarow.getNewBoard()
    for i in range(6):
        board[(0, i)] = 'X'
    sys.stdin = io.StringIO('1\n2\n')
    assert fourinarow.getPlayerMove('X', board) == (1, 5)


def test_displayBoard(capsys):
    board = fourinarow.getNewBoard()
    fourinarow.displayBoard(board)
    captured = capsys.readouterr()
    assert '     1234567\n' + \
           '    +-------+\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    +-------+\n' in captured.out

    board[(0, 5)] = 'X'
    fourinarow.displayBoard(board)
    captured = capsys.readouterr()
    assert '     1234567\n' + \
           '    +-------+\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |X......|\n' + \
           '    +-------+\n' in captured.out

    board[(1, 5)] = 'O'
    fourinarow.displayBoard(board)
    captured = capsys.readouterr()
    assert '     1234567\n' + \
           '    +-------+\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |.......|\n' + \
           '    |XO.....|\n' + \
           '    +-------+\n' in captured.out

def test_main(capsys):
    # Test a game where X wins:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('1\n2\n1\n2\n1\n2\n1\n')
        fourinarow.main()
    captured = capsys.readouterr()
    assert 'Player X has won!' in captured.out

    # Test a game where O wins:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('1\n2\n1\n2\n1\n2\n3\n2\n')
        fourinarow.main()
    captured = capsys.readouterr()
    assert 'Player O has won!' in captured.out

    # Test a game that ends in a tie:
    moves = ('123456' * 3) + ('712345' * 3) + ('67' * 3)
    moves = '\n'.join(moves) + '\n'
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(moves)
        fourinarow.main()
    captured = capsys.readouterr()
    assert 'There is a tie!' in captured.out

