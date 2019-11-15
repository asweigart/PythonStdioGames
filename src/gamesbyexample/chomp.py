# Chomp, by Al Sweigart al@inventwithpython.com
# A dangerously delicious logic game.
# Inspired by a Frederik Schuh and David Gale puzzle, published by
# Martin Gardner in Scientific American (January 1973)
# More info at: https://en.wikipedia.org/wiki/Chomp

import random, sys

print('''CHOMP
By Al Sweigart al@inventwithpython.com
Inspired by a Frederik Schuh and David Gale puzzle.

In this two player game, players take turns picking a piece from a chocolate
bar and eating that piece and all pieces below and to the right of it. The
upper left piece is poisonous, and the player to eat that piece loses.
''')

width = random.randint(2, 9)
height = random.randint(2, 9)

# Create a dictionary to represent the uneaten parts of the chocolate bar:
uneatenBar = {}
for x in 'ABCDEFGHI'[:width]:
    for y in '123456789'[:height]:
        uneatenBar[(x, y)] = True

turn = 'X'
while True: # Main game loop.

    # Display the chocolate bar:
    print(' ABCDEFGHI'[:width + 1]) # Print the horizontal labels.
    for iy in range(height):
        print(iy + 1, end='') # + 1 because the labels should start at 1, not 0.
        for ix in range(width):
            x = 'ABCDEFGHI'[ix]
            y = '123456789'[iy]
            if x == 'A' and y == '1':
                print('P', end='') # Display P for poison piece.
            elif uneatenBar[(x, y)] == True:
                print('#', end='') # Display # for a chocolate bar piece.
            else:
                print('.', end='') # Display . for an eaten piece.
        print() # Print a newline.

    # Get the player's move:
    print('It is {}\'s turn.'.format(turn))
    while True:
        print()
        print('Select the piece to eat (or QUIT):')
        response = input().upper()

        # Check if the player wants to stop playing:
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if len(response) != 2:
            print('Enter a coordinate like "B3" or "D5".')
            continue

        piecex = response[0]
        piecey = response[1]

        if (piecex, piecey) not in uneatenBar.keys():
            print('That coordinate doesn\'t exist on this chocolate bar.')

        if uneatenBar.get((piecex, piecey), False) == True:
            break

        print('Select a piece that hasn\'t already been eaten.')

    # Determine the other player's mark.
    if turn == 'X':
        otherPlayer = 'O'
    elif turn == 'O':
        otherPlayer = 'X'

    # Check if the player ate the poison piece:
    if piecex == 'A' and piecey == '1':
        print('{} has eaten the poison piece!'.format(turn))
        print('{} wins!'.format(otherPlayer))
        break # Break out of the main game loop.

    # Mark the selected piece and all pieces below and to the right as eaten:
    for x in 'ABCDEFGHI'['ABCDEFGHI'.index(piecex):]:
        for y in '123456789'[int(piecey) - 1:]:
            uneatenBar[(x, y)] = False

    # Switch turns:
    turn = otherPlayer