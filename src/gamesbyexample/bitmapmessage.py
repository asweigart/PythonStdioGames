"""Bitmap Message, by Al Sweigart al@inventwithpython.com

Displays a text message according to the provided bitmap image.
Tags: tiny, artistic"""

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
print('Enter the message you\'d like to display with the bitmap.')
message = input('> ')

# Loop over each line:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print the character from the messge in this space:
            print(message[i % len(message)], end='')
    print()  # Print a newline.
