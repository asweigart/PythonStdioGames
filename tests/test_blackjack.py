import pytest
import sys
import io
import random
from gamesbyexample import blackjack


def test_displayCards(capsys):
    # Test displaying no cards:
    blackjack.displayCards([])
    captured = capsys.readouterr()
    assert captured.out == '\n\n\n\n'

    # Test displaying a single card:
    blackjack.displayCards([('K', blackjack.HEARTS)])
    captured = capsys.readouterr()
    assert captured.out == ' ___  \n' + \
                           '|K  | \n' + \
                           '| ♥ | \n' + \
                           '|__K| \n'

    # Test displaying a 10 card:
    blackjack.displayCards([('10', blackjack.HEARTS)])
    captured = capsys.readouterr()
    assert captured.out == ' ___  \n' + \
                           '|10 | \n' + \
                           '| ♥ | \n' + \
                           '|_10| \n'

    # Test displaying multiple cards:
    blackjack.displayCards([('K', blackjack.HEARTS), ('9', blackjack.HEARTS), ])
    captured = capsys.readouterr()
    assert captured.out == ' ___   ___  \n' + \
                           '|K  | |9  | \n' + \
                           '| ♥ | | ♥ | \n' + \
                           '|__K| |__9| \n'

    # Test displaying a flipped card:
    blackjack.displayCards([blackjack.BACKSIDE])
    captured = capsys.readouterr()
    assert captured.out == ' ___  \n' + \
                           '|## | \n' + \
                           '|###| \n' + \
                           '|_##| \n'

def test_getCardValue():
    # Test the pip card values:
    for i in range(2, 11):
        assert blackjack.getCardValue([(str(i), blackjack.HEARTS)]) == i

    # Test the pip card values (multiple cards):
    for i in range(2, 11):
        for j in range(2, 11):
            assert blackjack.getCardValue([(str(i), blackjack.HEARTS), (str(j), blackjack.HEARTS)]) == i + j

    # Test the face cards:
    for i in ('J', 'Q', 'K'):
        assert blackjack.getCardValue([(i, blackjack.HEARTS)]) == 10

    # Test the ace cards:
    assert blackjack.getCardValue([('A', blackjack.HEARTS)]) == 11
    assert blackjack.getCardValue([('A', blackjack.HEARTS), ('K', blackjack.HEARTS)]) == 21
    assert blackjack.getCardValue([('A', blackjack.HEARTS), ('K', blackjack.HEARTS), ('K', blackjack.DIAMONDS)]) == 21
    assert blackjack.getCardValue([('A', blackjack.HEARTS), ('6', blackjack.HEARTS), ('6', blackjack.DIAMONDS)]) == 13


def test_getDeck():
    deck = blackjack.getDeck()
    assert len(deck) == 52
    for rank in range(2, 11):
        for suit in (blackjack.HEARTS, blackjack.DIAMONDS, blackjack.CLUBS, blackjack.SPADES):
            assert (str(rank), suit) in deck

    for rank in ('A', 'J', 'Q', 'K'):
        for suit in (blackjack.HEARTS, blackjack.DIAMONDS, blackjack.CLUBS, blackjack.SPADES):
            assert (str(rank), suit) in deck


def test_displayHands(capsys):
    playerHand = [('A', blackjack.HEARTS), ('K', blackjack.HEARTS)]
    dealerHand = [('6', blackjack.HEARTS), ('6', blackjack.DIAMONDS)]
    blackjack.displayHands(playerHand, dealerHand, False)
    captured = capsys.readouterr()
    assert captured.out == '\n' + \
                           'DEALER: ???\n' + \
                           ' ___   ___  \n' + \
                           '|## | |6  | \n' + \
                           '|###| | ♦ | \n' + \
                           '|_##| |__6| \n' + \
                           'PLAYER: 21\n' + \
                           ' ___   ___  \n' + \
                           '|A  | |K  | \n' + \
                           '| ♥ | | ♥ | \n' + \
                           '|__A| |__K| \n'

    blackjack.displayHands(playerHand, dealerHand, True)
    captured = capsys.readouterr()
    assert captured.out == '\n' + \
                           'DEALER: 12\n' + \
                           ' ___   ___  \n' + \
                           '|6  | |6  | \n' + \
                           '| ♥ | | ♦ | \n' + \
                           '|__6| |__6| \n' + \
                           'PLAYER: 21\n' + \
                           ' ___   ___  \n' + \
                           '|A  | |K  | \n' + \
                           '| ♥ | | ♥ | \n' + \
                           '|__A| |__K| \n'


def test_getBet():
    # Basic test:
    sys.stdin = io.StringIO('50\n')
    assert blackjack.getBet(100) == 50

    sys.stdin = io.StringIO(' 50 \n')
    assert blackjack.getBet(100) == 50

    # Test quitting:
    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('QUIT\n')
        blackjack.getBet(100)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('quit\n')
        blackjack.getBet(100)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO('qUiT\n')
        blackjack.getBet(100)

    with pytest.raises(SystemExit):
        sys.stdin = io.StringIO(' quit \n')
        blackjack.getBet(100)

    # Test bad input:
    sys.stdin = io.StringIO('invalid\n50\n')
    assert blackjack.getBet(100) == 50

    # Test bet that is too high:
    sys.stdin = io.StringIO('101\n50\n')
    assert blackjack.getBet(100) == 50


def test_pause(capsys):
    sys.stdin = io.StringIO('\n')
    blackjack.pause()
    captured = capsys.readouterr()
    assert captured.out == 'Press Enter to continue...\n\n\n'


def test_getMove():
    playerHand = [('A', blackjack.HEARTS), ('K', blackjack.HEARTS)]

    # Test basic stand:
    sys.stdin = io.StringIO('S\n')
    assert blackjack.getMove(playerHand, 100) == 'S'
    sys.stdin = io.StringIO('s\n')
    assert blackjack.getMove(playerHand, 100) == 'S'

    # Test basic hit:
    sys.stdin = io.StringIO('H\n')
    assert blackjack.getMove(playerHand, 100) == 'H'
    sys.stdin = io.StringIO('h\n')
    assert blackjack.getMove(playerHand, 100) == 'H'

    # Test basic double down:
    sys.stdin = io.StringIO('D\n')
    assert blackjack.getMove(playerHand, 100) == 'D'
    sys.stdin = io.StringIO('d\n')
    assert blackjack.getMove(playerHand, 100) == 'D'

    # Test basic double down that's not available, so stand:
    sys.stdin = io.StringIO('D\nH\n')
    assert blackjack.getMove(playerHand + playerHand, 100) == 'H'

    # Test double down but player doesn't have any money:
    sys.stdin = io.StringIO('D\nH\n')
    assert blackjack.getMove(playerHand, 0) == 'H'


def test_main(capsys):
    # Test basic game:
    random.seed(42)
    sys.stdin = io.StringIO('100\nS\n\n\n')
    with pytest.raises(SystemExit):
        blackjack.main()
    captured = capsys.readouterr()
    assert '|3  | |10 |' in captured.out

    # Test quitting:
    random.seed(42)
    sys.stdin = io.StringIO('quit\n')
    with pytest.raises(SystemExit):
        blackjack.main()
