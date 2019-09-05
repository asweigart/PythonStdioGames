# The Multiplication Table
# By Al Sweigart al@inventwithpython.com

print('The Multiplication Table')

# Print the horizontal number labels:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# Display each row of products:
for number1 in range(0, 13): # Loop from 0 up to but not including 13.
    print(str(number1).rjust(2), end='') # Print the vertical numbers labels.
    print('|', end='') # Print a separating bar.
    for number2 in range(0, 13): # Loop from 0 up to but not including 13.
        print(str(number1 * number2).rjust(3), end='') # Print the product.
        print(' ', end='') # Print a separating space.
    print() # Finish the row by printing a newline.
