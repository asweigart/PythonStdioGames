"""Hex Grid, by Al Sweigart al@inventwithpython.com
Displays a simple tessellation of a hexagon grid.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, beginner, artistic"""
__version__ = 0
# Set up the constants:
# (!) Try changing these values to other numbers:
X_REPEAT = 19  # How many times to tessellate horizontally.
Y_REPEAT = 12  # How many times to tessellate vertically.

for y in range(Y_REPEAT):
    # Display the top half of the hexagon:
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    # Display the bottom half of the hexagon:
    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()
