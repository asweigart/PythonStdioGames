"""Shining Carpet, by Al Sweigart al@inventwithpython.com

Displays a tesselation of the carpet pattern from The Shining."""
__version__ = 1

# Setup the constants:

F = chr(9585) # The ╱ character.
B = chr(9586) # The ╲ character.

X_REPEAT = 6
Y_REPEAT = 4

for i in range(Y_REPEAT):
    print(' \\_/ ___ \\ \\'.replace('\\', B).replace('/', F) * X_REPEAT)
    print('\\___/ _ \\ \\ '.replace('\\', B).replace('/', F) * X_REPEAT)
    print('_____/ \\ \\ \\'.replace('\\', B).replace('/', F) * X_REPEAT)
    print(' ___ \\_/ / /'.replace('\\', B).replace('/', F) * X_REPEAT)
    print('/ _ \\___/ / '.replace('\\', B).replace('/', F) * X_REPEAT)
    print(' / \\_____/ /'.replace('\\', B).replace('/', F) * X_REPEAT)
