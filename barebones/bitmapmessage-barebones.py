"""Bitmap Message (barebones version)
by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image."""
import sys

bitmap = """
        ********
     ********
   ********
  ********
   ********
     ********
        ********
       ********
     ********
********************
********************
**************************
********************    **
********************    **
********************    **
*************************
********************
 ******************
"""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')

# Loop over each line in the multi-line bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i in range(len(line)):
        if line[i] == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.
