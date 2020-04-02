"""Bitmap Message, by Al Sweigart al@inventwithpython.com

Displays a text message according to the provided bitmap image.
Tags: tiny, beginner, artistic"""

# (!) Try changing this multiline string to any image you like:
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
