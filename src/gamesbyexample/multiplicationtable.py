"""Multiplication Table, by Al Sweigart al@inventwithpython.com
Print a multiplication table.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, math"""
__version__ = 0
print('Multiplication Table, by Al Sweigart al@inventwithpython.com')

# Print the horizontal number labels:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# Display each row of products:
for number1 in range(0, 13):

    # Print the vertical numbers labels:
    print(str(number1).rjust(2), end='')

    # Print a separating bar:
    print('|', end='')

    for number2 in range(0, 13):
        # Print the product:
        print(str(number1 * number2).rjust(3), end='')

        # Print a separating space:
        print(' ', end='')

    print()  # Finish the row by printing a newline.
