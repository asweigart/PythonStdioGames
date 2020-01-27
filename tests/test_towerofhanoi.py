import pytest
import sys
import io
import copy
import random
from gamesbyexample import towerofhanoi

def test_constants():
    assert towerofhanoi.TOTAL_DISKS == 5
    assert towerofhanoi.COMPLETE_TOWER == [5, 4, 3, 2, 1]

def test_getPlayerMove(capsys):
    towers = {'A': copy.copy(towerofhanoi.COMPLETE_TOWER), 'B': [], 'C': []}

    sys.stdin = io.StringIO('AB\n')
    assert towerofhanoi.getPlayerMove(towers) == ('A', 'B')

    sys.stdin = io.StringIO(' ab \n')
    assert towerofhanoi.getPlayerMove(towers) == ('A', 'B')

    # Test entering an invalid move:
    sys.stdin = io.StringIO('invalid\nquit\n')
    with pytest.raises(SystemExit):
        towerofhanoi.getPlayerMove(towers)
    captured = capsys.readouterr()
    assert 'Enter one of AB, AC, BA, BC, CA, or CB.' in captured.out

    # Test quitting:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        towerofhanoi.getPlayerMove(towers)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        towerofhanoi.getPlayerMove(towers)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        towerofhanoi.getPlayerMove(towers)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        towerofhanoi.getPlayerMove(towers)

    # Test selecting an empty tower:
    sys.stdin = io.StringIO('ba\nquit\n')
    with pytest.raises(SystemExit):
        towerofhanoi.getPlayerMove(towers)
    captured = capsys.readouterr()
    assert 'You selected a tower with no disks.' in captured.out

    # Test trying to put a disk on a smaller disk:
    towers = {'A': [5, 4, 3, 2], 'B': [1], 'C': []}
    sys.stdin = io.StringIO('ab\nquit\n')
    with pytest.raises(SystemExit):
        towerofhanoi.getPlayerMove(towers)
    captured = capsys.readouterr()
    assert 'Can\'t put larger disks on top of smaller ones.' in captured.out


def test_main(capsys):
    # Test winning a game:
    sys.stdin = io.StringIO('ab\nac\nbc\nab\nca\ncb\nab\nac\nbc\nba\nca\nbc\nab\nac\nbc\nab\nca\ncb\nab\nca\nbc\nba\nca\ncb\nab\nac\nbc\nab\nca\ncb\nab\n')
    with pytest.raises(SystemExit):
        towerofhanoi.main()
    captured = capsys.readouterr()
    assert 'You have solved the puzzle! Well done!' in captured.out


def test_displayDisk(capsys):
    # Test displaying an empty pole:
    towerofhanoi.displayDisk(0)
    captured = capsys.readouterr()
    assert captured.out == '     ||     '

    # Test displaying a disk:
    towerofhanoi.displayDisk(1)
    captured = capsys.readouterr()
    assert captured.out == '    @_1@    '

    towerofhanoi.displayDisk(2)
    captured = capsys.readouterr()
    assert captured.out == '   @@_2@@   '

    towerofhanoi.displayDisk(3)
    captured = capsys.readouterr()
    assert captured.out == '  @@@_3@@@  '

    towerofhanoi.displayDisk(4)
    captured = capsys.readouterr()
    assert captured.out == ' @@@@_4@@@@ '

    towerofhanoi.displayDisk(5)
    captured = capsys.readouterr()
    assert captured.out == '@@@@@_5@@@@@'


def test_displayTowers(capsys):
    towers = {'A': copy.copy(towerofhanoi.COMPLETE_TOWER), 'B': [], 'C': []}
    towerofhanoi.displayTowers(towers)
    captured = capsys.readouterr()
    assert captured.out == '     ||          ||          ||     \n' + \
                           '    @_1@         ||          ||     \n' + \
                           '   @@_2@@        ||          ||     \n' + \
                           '  @@@_3@@@       ||          ||     \n' + \
                           ' @@@@_4@@@@      ||          ||     \n' + \
                           '@@@@@_5@@@@@     ||          ||     \n' + \
                           '      A           B           C\n\n'

    towers = {'B': copy.copy(towerofhanoi.COMPLETE_TOWER), 'A': [], 'C': []}
    towerofhanoi.displayTowers(towers)
    captured = capsys.readouterr()
    assert captured.out == '     ||          ||          ||     \n' + \
                           '     ||         @_1@         ||     \n' + \
                           '     ||        @@_2@@        ||     \n' + \
                           '     ||       @@@_3@@@       ||     \n' + \
                           '     ||      @@@@_4@@@@      ||     \n' + \
                           '     ||     @@@@@_5@@@@@     ||     \n' + \
                           '      A           B           C\n\n'


    towers = {'C': copy.copy(towerofhanoi.COMPLETE_TOWER), 'A': [], 'B': []}
    towerofhanoi.displayTowers(towers)
    captured = capsys.readouterr()
    assert captured.out == '     ||          ||          ||     \n' + \
                           '     ||          ||         @_1@    \n' + \
                           '     ||          ||        @@_2@@   \n' + \
                           '     ||          ||       @@@_3@@@  \n' + \
                           '     ||          ||      @@@@_4@@@@ \n' + \
                           '     ||          ||     @@@@@_5@@@@@\n' + \
                           '      A           B           C\n\n'

def isValidTowerConfiguration(towers):
    # Make sure there are exactly 5 disks:
    assert len(towers['A'] + towers['B'] + towers['C']) == 5

    # Make sure there's only one disk of each size:
    assert len(towers['A'] + towers['B'] + towers['C']) == len(set(towers['A'] + towers['B'] + towers['C']))
    assert set(towers['A'] + towers['B'] + towers['C']) == set([1, 2, 3, 4, 5])

    # Make sure a larger disk is not on a smaller disk:
    for label in ('A', 'B', 'C'):
        for i in range(len(towers[label]) - 1):
            assert towers[label][i] > towers[label][i + 1]


def test_randomMoves():
    towers = {'A': copy.copy(towerofhanoi.COMPLETE_TOWER), 'B': [], 'C': []}

    random.seed(42)
    for i in range(10000):
        randomMove = random.choice(('AB', 'AC', 'BA', 'BC', 'CA', 'CB'))
        sys.stdin = io.StringIO(randomMove + '\nQUIT\n')
        try:
            move = towerofhanoi.getPlayerMove(towers)
        except SystemExit:
            continue

        # (Copy/pasted from main())
        # Ask the user for a move:
        fromTower, toTower = move

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        isValidTowerConfiguration(towers)
