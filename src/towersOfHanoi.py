# Towers of Hanoi puzzle, by Al Sweigart al@inventwithpython.com

# A puzzle where you must move the discs of one tower to another tower.
# More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi

import sys

# Set up towers A, B, and C. The end of the list is the top of the tower.
TOTAL_DISCS = 6
HEIGHT = TOTAL_DISCS + 1

# Populate Tower A:
completeTower = list(reversed(range(1, TOTAL_DISCS + 1)))
TOWERS = {'A': completeTower,
          'B': [],
          'C': []}


def printDisc(discNum):
    # Print a single disc of width discNum.
    emptySpace = ' ' * (TOTAL_DISCS - discNum)
    if discNum == 0:
        # Just draw the pole of the tower.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Draw the disc.
        discSpace = '@' * discNum
        discNumLabel = str(discNum).rjust(2, '_')
        print(emptySpace + discSpace + discNumLabel + discSpace + emptySpace, end='')


def printTowers():
    # Print all three towers.
    for level in range(HEIGHT - 1, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisc(0)
            else:
                printDisc(tower[level])
        print()
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISCS)
    print(f'{emptySpace} A{emptySpace}{emptySpace} B{emptySpace}{emptySpace} C\n')


print('THE TOWERS OF HANOI')
print('By Al Sweigart al@inventwithpython.com')
print()
print('Move the tower of discs, one disc at a time, to another pole.')
print('Larger discs cannot rest on top of a smaller disc.')

while True: # Main program loop.
    # Display the towers and ask the user for a move:
    printTowers()
    print('Enter letter of "source" and "destination" tower: A, B, C, or QUIT to quit.')
    print('(For example, "AB" to move the top disc of tower A to tower B.)')
    move = input().upper()

    if move == 'QUIT':
        sys.exit()

    # Make sure the user entered two letters:
    if len(move) != 2:
        print('Invalid move: Enter two tower letters.')
        continue

    # Put the letters in move in more readable variable names:
    srcTower = move[0]
    dstTower = move[1]

    # Make sure the user entered valid tower letters:
    if srcTower not in 'ABC' or dstTower not in 'ABC' or srcTower == dstTower:
        print('Invalid move: Enter letters A, B, or C for the two towers.')
        continue

    # Make sure the src disc is smaller than the dst tower's topmost disc:
    if len(TOWERS[srcTower]) == 0 or (len(TOWERS[dstTower]) != 0 and TOWERS[dstTower][-1] < TOWERS[srcTower][-1]):
        print('Invalid move. Larger discs cannot go on top of smaller discs.')
        continue

    # Move the top disc from srcTower to dstTower:
    disc = TOWERS[srcTower].pop()
    TOWERS[dstTower].append(disc)

    # Check if the user has solved the puzzle:
    if completeTower in (TOWERS['B'], TOWERS['C']):
        printTowers() # Display the towers one last time.
        print('You have solved the puzzle! Well done!')
        sys.exit()
