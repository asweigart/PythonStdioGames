# Towers of Hanoi puzzle, by Al Sweigart al@inventwithpython.com

# A puzzle where you must move the disks of one tower to another tower.
# More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi

import sys

# Set up towers A, B, and C. The end of the list is the top of the tower.
TOTAL_DISKS = 6
HEIGHT = TOTAL_DISKS + 1

# Populate Tower A:
completeTower = list(reversed(range(1, TOTAL_DISKS + 1)))
TOWERS = {'A': completeTower,
          'B': [],
          'C': []}


def printDisk(diskNum):
    # Print a single disk of width diskNum.
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        # Just draw the pole of the tower.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # Draw the disk.
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        print(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace, end='')


def printTowers():
    # Print all three towers.
    for level in range(HEIGHT - 1, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        print()
    # Print the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('%s A%s%s B%s%s C\n' % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))


print('The Towers of Hanoi')
print('Move the tower, one disk at a time, to another pole.')
print('Larger disks cannot rest on top of a smaller disk.')

while True: # Main program loop.
    # Display the towers and ask the user for a move:
    printTowers()
    print('Enter letter of "source" and "destination" tower: A, B, C, or QUIT to quit.')
    print('(For example, "AB" to move the top disk of tower A to tower B.)')
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

    # Make sure the src disk is smaller than the dst tower's topmost disk:
    if len(TOWERS[srcTower]) == 0 or (len(TOWERS[dstTower]) != 0 and TOWERS[dstTower][-1] < TOWERS[srcTower][-1]):
        print('Invalid move. Larger disks cannot go on top of smaller disks.')
        continue

    # Move the top disk from srcTower to dstTower:
    disk = TOWERS[srcTower].pop()
    TOWERS[dstTower].append(disk)

    # Check if the user has solved the puzzle:
    if completeTower in (TOWERS['B'], TOWERS['C']):
        printTowers() # Display the towers one last time.
        print('You have solved the puzzle! Well done!')
        sys.exit()
