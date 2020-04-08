r"""Diamond Drawings, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
 Tags: short, beginner, artistic"""
__version__ = 0

def main():
    print('Diamond Drawings, by Al Sweigart al@inventwithpython.com')
    print()

    # Display diamonds of sizes 1 through 6:
    for diamondSize in range(1, 6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()


def displayOutlineDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/', end='')  # Left side of diamond.
        print(' ' * (i * 2), end='')  # Interior of diamond.
        print('\\', end='')  # Right side of diamond.
        print()  # A newline.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * (i), end='')  # Left side space.
        print('\\', end='')  # Left side of diamond.
        print(' ' * ((size - i - 1) * 2), end='')  # Interior of diamond.
        print('/', end='')  # Right side of diamond.
        print()  # A newline.


def displayFilledDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/', end='')  # Left side of diamond.
        print('/' * i, end='')  # Interior of diamond.
        print('\\' * i, end='')  # Interior of diamond.
        print('\\', end='')  # Right side of diamond.
        print()  # A newline.

    # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * (i), end='')  # Left side space.
        print('\\', end='')  # Left side of diamond.
        print('\\' * (size - i - 1), end='')  # Interior of diamond.
        print('/' * (size - i - 1), end='')  # Interior of diamond.
        print('/', end='')  # Right side of diamond.
        print()  # A newline.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
