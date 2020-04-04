"""Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com
A water pouring puzzle.
More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle
Tags: large, object-oriented, game, puzzle game, math"""
__version__ = 0
import sys


class Bucket:
    def __init__(self, size):
        self.size = size  # Size of the bucket in liters.
        self.water = 0  # Buckets start off with 0 liters of water.

    def fill(self):
        self.water = self.size  # Set the amount of water to the max size.

    def drain(self):
        self.water = 0  # Set the amount of water to nothing.

    def pour(self, intoBucket):
        # Figure out the amount to pour:
        remainingSpace = intoBucket.size - intoBucket.water
        amountToPour = min(remainingSpace, self.water)

        # Pour out water from this bucket:
        self.water = self.water - amountToPour

        # Put the poured out water into the other bucket:
        intoBucket.water = intoBucket.water + amountToPour

print('''WATER BUCKET PUZZLE
By Al Sweigart al@inventwithpython.com''')

GOAL = 4  # The exact amount of water to have in a bucket to win.
steps = 0  # Keep track of how many steps the player made to solve this.

# The amount of water in each bucket:
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True:  # Main game loop.
    # Display the current state of the buckets:
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets:')

    waterDisplay = []  # Contains strings for water or empty space.

    # Get the strings for the 8L bucket:
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Get the strings for the 5L bucket:
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Get the strings for the 3L bucket:
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Display the buckets with the amount of water in each one:
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterDisplay))

    # Check if any of the buckets has the goal amount of water:
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # Let the player select an action to do with a bucket:
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:  # Keep asking until the player enters a valid action.
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break  # Player has selected a valid action.
        print('Enter F, E, P, or Q')
        # At this point, go back to the start of the loop.

    # Let the player select a bucket:
    while True:  # Keep asking until valid bucket entered.
        print('Select a bucket 8, 5, 3, or QUIT:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break  # Player has selected a valid bucket.
        # At this point, go back to the start of the loop.

    # Carry out the selected action:
    if move == 'F':
        # Set the amount of water to the max size.
        srcBucketSize = int(srcBucket)
        waterInBucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        waterInBucket[srcBucket] = 0  # Set water amount to nothing.
        steps += 1

    elif move == 'P':
        # Let the player select a bucket to pour into:
        while True:  # Keep asking until valid bucket entered.
            print('Select a bucket to pour into: 8, 5, or 3')
            dstBucket = input('> ').upper()
            if dstBucket in ('8', '5', '3'):
                break  # Player has selected a valid bucket.

        # Figure out the amount to pour:
        dstBucketSize = int(dstBucket)
        emptySpaceInDstBucket = dstBucketSize - waterInBucket[dstBucket]
        waterInSrcBucket = waterInBucket[srcBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        # Pour out water from this bucket:
        waterInBucket[srcBucket] -= amountToPour

        # Put the poured out water into the other bucket:
        waterInBucket[dstBucket] += amountToPour
        steps += 1

    elif move == 'C':
        pass  # If the player selected Cancel, do nothing.

    # At this point, go back to the start of the main game loop.
