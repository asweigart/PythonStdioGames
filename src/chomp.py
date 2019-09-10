# Chomp, by Al Sweigart al@inventwithpython.com
# Inspired by a Martin Gardner puzzle from Scientific American
# https://www.atariarchives.org/basicgames/showpage.php?page=44

# TODO - fix the UI for this game.

import random, sys

print('CHOMP')
print('By Al Sweigart al@inventwithpython.com')
print('Inspired by a Martin Gardner puzzle from Scientific American')
print()
print('In this two player game, players take turns eating a piece out of a')
print('rectangular cookie. You must always eat something on your turn. The')
print('goal is to not eat the poisonous corner in the upper left.')
print()

width = random.randint(1, 9)
height = random.randint(1, 9)
widthChomped = 0
heightChomped = 0

turn = 'X'

while True: # Main game loop.
    # Display the board:
    print('  1 2 3 4 5 6 7 8 9') # Print the horizontal labels.
    print()
    for y in range(1, 10):
        print(f'{y} ', end='') # Print the vertical labels.
        if y > height:
            print() # Print a newline.
            continue

        # Print a row of cookie pieces:
        for x in range(1, width + 1):
            if x == 1 and y == 1:
                print('P ', end='')
                continue

            if x == width - widthChomped and y == height - heightChomped:
                print('X', end='')
                continue

            # Print a cookie piece if it exists:
            if ((x > width - widthChomped) and (y > height - heightChomped)):
                print('. ', end='')
            else:
                print('* ', end='')
        print() # Print a newline.

    # Get the player's move:
    print(f'It is {turn}\'s turn.')
    if widthChomped == 0:
        columnEatMinimum = 1
    else:
        columnEatMinimum = 0
    while True: # Get the number of columns to eat:
        print(f'How many columns to eat? ({columnEatMinimum}-{width - widthChomped})')
        response = input()
        if response.isdecimal() and columnEatMinimum <= int(response) <= (width - widthChomped):
            break
        print(f'Enter a number between {columnEatMinimum} and {width - widthChomped}.')
    columnsToEat = int(response)

    if heightChomped == 0 or columnsToEat == 0:
        rowEatMinimum = 1
    else:
        rowEatMinimum = 0
    while True: # Get the number of rows to eat:
        print(f'How many rows to eat? ({rowEatMinimum}-{height - heightChomped})')
        response = input()
        if response.isdecimal() and rowEatMinimum <= int(response) <= (height - heightChomped):
            break
        print(f'Enter a number between {rowEatMinimum} and {height - heightChomped}.')
    rowsToEat = int(response)

    # Process the player's move:
    widthChomped += columnsToEat
    heightChomped += rowsToEat

    # Check to see if someone won:
    if turn == 'X':
        otherPlayer = 'O'
    elif turn == 'O':
        otherPlayer = 'X'
    if widthChomped == width and heightChomped == height:
        # Player has eaten the poison:
        print(f'{turn} has eaten the poison! {otherPlayer} wins!')
        sys.exit()
    else:
        # Continue the game with the other player:
        turn = otherPlayer
