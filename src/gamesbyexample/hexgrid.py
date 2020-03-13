"""Hex Grid, by Al Sweigart al@inventwithpython.com

Displays a simple tesselation of a hexagon grid."""
__version__ = 1

# Setup the constants:
Y_REPEAT = 12
X_REPEAT = 19

for y in range(Y_REPEAT):
    # Display the top half of the hexagon:
    for x in range(X_REPEAT):
        print(r'/ \_', end='')
    print()

    # Display the bottom half of the hexagon:
    for x in range(X_REPEAT):
        print(r'\_/ ', end='')
    print()
