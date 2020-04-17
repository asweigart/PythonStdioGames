"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, artistic"""

# (!) Try changing this multiline string to any image you like:
__version__ = 0
bitmap = """
               **   *  *** **  *
           * **********      **      ****   ***     ******    ***
  ******************* **    **      *  * ****************************
  ********************* ** ** *  * ****************************** **
  ******************* *** *   *  ** **************************  **
***      *****************       ******************************
          *************                **** ** ************** *
           *********            *******   **************** * *
            ********           ********* *****************  *
  **         *****  ***      * *************** ******  ** *
               ****   *       ****************   *** ***  *
                 ********       ** ***********    *  ** ***
                   ********         ********         *  *** ****
                   **********        ******  *        **** ** * **
                    *********        ****** **            *** *   **
                     *******          ***** **          ********   **
                    *******           ****              *********
                    ******             *                 *******   *
                    ******                                    *    *
                    ****
                    ***  *
                      **"""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')

# Loop over each line:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the messge:
            print(message[i % len(message)], end='')
    print()  # Print a newline.
