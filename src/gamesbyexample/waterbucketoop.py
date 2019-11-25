# Water Bucket Puzzle (OOP), by Al Sweigart al@inventwithpython.com
# A water pouring puzzle. (Object-oriented programming style.)
# More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle

import sys

class Bucket:
    def __init__(self, size):
        self.size = size # Size of the bucket in liters.
        self.water = 0 # Buckets start off with 0 liters of water.

    def fill(self):
        # Set the amount of water to the max size.
        self.water = self.size

    def drain(self):
        self.water = 0 # Set the amount of water to nothing.

    def pour(self, intoBucket):
        # Figure out the amount to pour:
        remainingSpace = intoBucket.size - intoBucket.water
        amountToPour = min(remainingSpace, self.water)

        # Pour out water from this bucket:
        self.water = self.water - amountToPour

        # Put the poured out water into the other bucket:
        intoBucket.water = intoBucket.water + amountToPour

    def description(self):
        return '{}L bucket filled with {}L'.format(self.size, self.water)

# Set up the constants used in this program:
BUCKETS = [Bucket(8), Bucket(5), Bucket(3)] # The bucket sizes available.
LABELS = 'ABC' # Have as many letters as you have buckets.
GOAL = 4 # The goal amount of water to have.

# Make sure the above settings are valid:
assert len(BUCKETS) == len(LABELS) == len(set(LABELS))

while True: # Main game loop.
    # Display the current state of the buckets:
    print('Try to get ' + str(GOAL) + 'L of water with these', len(BUCKETS), 'buckets:')
    for i, bucket in enumerate(BUCKETS):
        print('  {}. {}'.format(LABELS[i], bucket.description()))
    print()

    # Check if any of the buckets has the goal amount of water:
    for bucket in BUCKETS:
        if bucket.water == GOAL:
            print('Good job! You have solved the puzzle!')
            sys.exit()

    # Let the player select a bucket:
    while True: # Keep asking until the player enters a valid bucket.
        print('Select a bucket A to', LABELS[-1], 'or QUIT:')
        selectedLabel = input().upper()

        if selectedLabel == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if selectedLabel in tuple(LABELS):
            break # Player has selected a valid bucket.
    selectedBucket = BUCKETS[LABELS.index(selectedLabel)]

    # Let the player select an action to do with that bucket:
    print('You can:')
    print('  (F)ill the bucket')
    print('  (D)rain the bucket')
    print('  (P)our the bucket into another')
    print('  (C)ancel and select another bucket')

    while True: # Keep asking until the player enters a valid action.
        move = input().upper()
        if move in ('F', 'D', 'P', 'C'):
            break # Player has selected a valid action.
        print('Enter F, D, P, or C')

    # Carry out the selected action:
    if move == 'F':
        selectedBucket.fill()

    elif move == 'D':
        selectedBucket.drain()

    elif move == 'P':
        # Let the player select a bucket to pour into:
        while True: # Keep asking until the player enters a valid bucket.
            print('Select a bucket A to', LABELS[-1], 'to pour into:')
            selectedLabel = input().upper()
            if selectedLabel in tuple(LABELS):
                break # Player has selected a valid bucket.
        selectedTarget = BUCKETS[LABELS.index(selectedLabel)]

        # Pour water into the bucket:
        selectedBucket.pour(selectedTarget)

    elif move == 'C':
        pass # If the player selected Cancel, do nothing.
