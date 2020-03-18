"""Shining Carpet, by Al Sweigart al@inventwithpython.com

Displays a tesselation of the carpet pattern from The Shining."""
__version__ = 1

# Set up the constants:


X_REPEAT = 6
Y_REPEAT = 4

for i in range(Y_REPEAT):
    print(' \\_/ ___ \\ \\' * X_REPEAT)
    print('\\___/ _ \\ \\ ' * X_REPEAT)
    print('_____/ \\ \\ \\' * X_REPEAT)
    print(' ___ \\_/ / /' * X_REPEAT)
    print('/ _ \\___/ / ' * X_REPEAT)
    print(' / \\_____/ /' * X_REPEAT)
