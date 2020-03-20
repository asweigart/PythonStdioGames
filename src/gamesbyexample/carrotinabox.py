"""Carrot in a Box, by Al Sweigart al@inventwithpython.com

A silly bluffing game between two human players. Based on the game
from the show, 8 Out of 10 Cats.
Tags: large, game, two-player"""
__version__ = 1

import random

print('''Carrot in a Box
By Al Sweigart al@inventwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')
input('Press Enter to begin.')

p1Name = input('Human player 1, enter your name:')
p2Name = input('Human player 2, enter your name:')

print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')

print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
input('Press Enter to continue...')

print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!!')
input('When ' + p2Name + '\'s eyes are closed, press Enter...')

print(p1Name + ' here is the inside of your box:')

if random.randint(1, 2) == 1:
    carrotInRedBox = True
else:
    carrotInRedBox = False

if carrotInRedBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  +___||____+    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+
 (carrot!)''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
else:
    print('''
   _________
  |         |
  |         |
  +_________+    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+
(no carrot!)''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))

input('Press Enter to continue...')

print('\n' * 100)
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue...')

print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
print('  1) There is a carrot in my box.')
print('  2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
while True:
    response = input().upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', please enter "YES" or "NO"')
    else:
        break

swappedBoxes = response.startswith('Y')

if swappedBoxes:
    print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   GOLD  | |  |   RED   | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
else:
    print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))

input('Press Enter to reveal the winner...')

if swappedBoxes and carrotInRedBox:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  +_________+    +___||____+
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|         | |  |         | |
|   GOLD  | |  |   RED   | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
    print(p2Name + ' is the winner!')
elif swappedBoxes and not carrotInRedBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  +___||____+    +_________+
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   GOLD  | |  |   RED   | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
    print(p1Name + ' is the winner!')
elif not swappedBoxes and carrotInRedBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  +___||____+    +_________+
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
    print(p1Name + ' is the winner!')
elif not swappedBoxes and not carrotInRedBox:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  +_________+    +___||____+
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|         | |  |         | |
|   RED   | |  |   GOLD  | |
|   BOX   |/   |   BOX   |/
+---------+    +---------+''')
    print(p1Name[:11].center(11) + '    ' + p2Name[:11].center(11))
    print(p2Name + ' is the winner!')

print('Thanks for playing!')
