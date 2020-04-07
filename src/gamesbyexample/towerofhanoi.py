"""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
A stack-moving puzzle game.
This and other games are available at https://nostarch.com/XX
Tags: short, game, puzzle game"""
__version__ = 0
import copy
import sys

TOTAL_DISKS = 5  # More disks means a more difficult puzzle.

# Start with all disks on tower A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print("""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    # Set up the towers. The end of the list is the top of the tower.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:  # Run a single turn.
        # Display the towers and disks:
        displayTowers(towers)

        # Ask the user for a move:
        fromTower, toTower = askForPlayerMove(towers)

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Check if the user has solved the puzzle:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)  # Display the towers one last time.
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True:  # Keep asking player until they enter a valid move.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        print()
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # Make sure the user entered valid tower letters:
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue  # Ask player again for their move.

        # Syntactic sugar - Use more descriptive variable names:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # The "from" tower cannot be an empty tower:
            print('You selected a tower with no disks.')
            continue  # Ask player again for their move.
        elif len(towers[toTower]) == 0:
            # Any disk can be moved onto an empty "to" tower:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top of smaller ones.')
            continue  # Ask player again for their move.
        else:
            # This is a valid move, so return the selected towers:
            return fromTower, toTower


def displayTowers(towers):
    """Display the current state."""

    # Display the three towers:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)  # Display the bare pole with no disk.
            else:
                displayDisk(tower[level])  # Display the disk.
        print()

    # Display the tower labels A, B, and C.
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f'{emptySpace}||{emptySpace}', end='')
    else:
        # Display the disk:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
