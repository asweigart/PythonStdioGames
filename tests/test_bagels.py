import pytest
import sys
import io
import random
from gamesbyexample import bagels


def test_getSecretNum():
    for i in range(100):
        secNum = bagels.getSecretNum()
        assert len(secNum) == bagels.NUM_DIGITS
        assert len(set(secNum)) == len(secNum)


def test_getClues():
    assert bagels.getClues('123', '156') == 'Fermi'
    assert bagels.getClues('123', '426') == 'Fermi'
    assert bagels.getClues('123', '453') == 'Fermi'
    assert bagels.getClues('123', '126') == 'Fermi Fermi'
    assert bagels.getClues('123', '423') == 'Fermi Fermi'
    assert bagels.getClues('123', '153') == 'Fermi Fermi'
    assert bagels.getClues('123', '123') == 'You got it!'
    assert bagels.getClues('123', '456') == 'Bagels'
    assert bagels.getClues('123', '256') == 'Pico'
    assert bagels.getClues('123', '416') == 'Pico'
    assert bagels.getClues('123', '452') == 'Pico'
    assert bagels.getClues('123', '215') == 'Pico Pico'
    assert bagels.getClues('123', '213') == 'Fermi Pico Pico'
    assert bagels.getClues('123', '253') == 'Fermi Pico'
    assert bagels.getClues('123', '231') == 'Pico Pico Pico'


def test_main(capsys):
    sys.stdin = io.StringIO('123\n732\nno\n')
    random.seed(42)
    bagels.main()
    captured = capsys.readouterr()
    assert 'Pico Pico' in captured.out

    sys.stdin = io.StringIO('231\n732\nno\n')
    random.seed(42)
    bagels.main()
    captured = capsys.readouterr()
    assert 'Fermi Pico' in captured.out

    sys.stdin = io.StringIO('132\n732\nno\n')
    random.seed(42)
    bagels.main()
    captured = capsys.readouterr()
    assert 'Fermi Fermi' in captured.out

    sys.stdin = io.StringIO('732\nyes\n352\nno\n')
    random.seed(42)
    bagels.main()
    captured = capsys.readouterr()
    assert 'You got it!' in captured.out

