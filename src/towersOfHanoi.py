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
        # Just draw the pole.
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

def moveOneDisk(startTower, endTower):
    # Move the top disk from startTower to endTower.
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)


while True:
    printTowers()
    try:
        print('Enter letter of "source" and "destination" tower: A, B, C, or Ctrl-C to quit.')
        print('(For example, "AB" to move the top disk of tower A to tower B.)')
        move = input().upper()
    except KeyboardInterrupt:
        sys.exit()

    if len(move) != 2:
        print('Invalid move.')
        continue

    srcTower, dstTower = move

    if srcTower in ('A', 'B', 'C') and len(TOWERS[srcTower]) > 0 and \
       dstTower in ('A', 'B', 'C') and (len(TOWERS[dstTower]) == 0 or TOWERS[dstTower][0] > TOWERS[srcTower][0]) and \
       srcTower != dstTower:
        moveOneDisk(srcTower, dstTower)
        if completeTower in (TOWERS['B'], TOWERS['C']):
            printTowers()
            print('You have solved the puzzle! Well done!')
            sys.exit()
    else:
        print('Invalid move.')
