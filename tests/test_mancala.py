import pytest
import sys
import io

from gamesbyexample import  mancala


def test_getNewBoard():
    assert mancala.getNewBoard() == {'1': 0, '2': 0, 'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4, 'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4}


def test_displayBoard(capsys):
    gameBoard = mancala.getNewBoard()
    mancala.displayBoard(gameBoard)
    captured = capsys.readouterr()
    assert captured.out.count('4') == 12
    assert captured.out.count('0') == 2


def test_makeMove():
    gameBoard = mancala.getNewBoard()
    result = mancala.makeMove(gameBoard, '1', 'C')
    assert result == '1'
    assert gameBoard == {'1': 1, '2': 0, 'A': 4, 'B': 4, 'C': 0, 'D': 5, 'E': 5, 'F': 5, 'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4}

    result = mancala.makeMove(gameBoard, '1', 'D')
    assert result == '2'
    assert gameBoard == {'1': 2, '2': 0, 'A': 4, 'B': 4, 'C': 0, 'D': 0, 'E': 6, 'F': 6, 'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 5, 'L': 5}


def test_quit():
    board = mancala.getNewBoard()
    # Test quitting:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        mancala.getPlayerMove('1', board)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        mancala.getPlayerMove('1', board)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        mancala.getPlayerMove('1', board)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        mancala.getPlayerMove('1', board)


def test_main(capsys):
    sys.stdin = io.StringIO('\nC\nD\nG\nC\nK\nI\nB\nH\nB\nJ\nD\nA\nI\nE\nH\nG\nJ\nF\nG\nH\nD\nI\nJ\nE\nH\nB\nG\n')
    with pytest.raises(SystemExit):
        mancala.main()
    captured = capsys.readouterr()
    assert 'Player 1 has won!' in captured.out


    # Tests having so many seeds in a pocket that you skip the other player's store:
    sys.stdin = io.StringIO('\nA\nG\nB\nH\nE\nI\nD\nG\nC\nH\nE\nF\nQUIT\n')
    with pytest.raises(SystemExit):
        mancala.main()
    captured = capsys.readouterr()
    assert '|  1 |  3 |' in captured.out


    sys.stdin = io.StringIO('\nG\n1\n2\nC\nC\n\nQUIT\n')
    with pytest.raises(SystemExit):
        mancala.main()
    captured = capsys.readouterr()
    assert 'Please pick a letter on your side of the board.' in captured.out
    assert 'Please pick a non-empty pit.' in captured.out