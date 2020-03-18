"""Shining Carpet, by Al Sweigart al@inventwithpython.com

Displays a tessellation of the carpet pattern from The Shining."""
__version__ = 1

# Set up the constants:
X_REPEAT = 6  # How many times to tessellate horizontally.
Y_REPEAT = 4  # How many times to tessellate vertically.

for i in range(Y_REPEAT):
    print(' \\_/ ___ \\ \\' * X_REPEAT)
    print('\\___/ _ \\ \\ ' * X_REPEAT)
    print('_____/ \\ \\ \\' * X_REPEAT)
    print(' ___ \\_/ / /' * X_REPEAT)
    print('/ _ \\___/ / ' * X_REPEAT)
    print(' / \\_____/ /' * X_REPEAT)
