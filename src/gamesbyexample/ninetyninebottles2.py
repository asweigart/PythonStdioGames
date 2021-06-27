"""niNety-nniinE BoOttels of Mlik On teh waLl
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! The song
gets sillier and sillier with each verse. Press Ctrl-C to stop.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, scrolling, word"""

import random, sys, time

# Set up the constants:
# (!) Try changing both of these to 0 to print all the lyrics at once.
SPEED = 0.01  # The pause in between printing letters.
LINE_PAUSE = 1.5  # The pause at the end of each line.


def slowPrint(text, pauseAmount=0.1):
    """Slowly print out the characters in text one at a time."""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='')  # end='' means no newline.
        time.sleep(pauseAmount)  # Pause in between each character.
    print()  # Print a newline.


print('niNety-nniinE BoOttels, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # This is the starting number of bottles.

# This list holds the string used for the lyrics:
lines = [' bottles of milk on the wall,',
         ' bottles of milk,',
         'Take one down, pass it around,',
         ' bottles of milk on the wall!']

try:
    while bottles > 0:  # Keep looping and display the lyrics.
        slowPrint(str(bottles) + lines[0], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(str(bottles) + lines[1], SPEED)
        time.sleep(LINE_PAUSE)
        slowPrint(lines[2], SPEED)
        time.sleep(LINE_PAUSE)
        bottles = bottles - 1  # Decrease the number of bottles by one.

        if bottles > 0:  # Print the last line of the current stanza.
            slowPrint(str(bottles) + lines[3], SPEED)
        else:  # Print the last line of the entire song.
            slowPrint('No more bottles of milk on the wall!', SPEED)

        time.sleep(LINE_PAUSE)
        print()  # Print a newline.

        # Choose a random line to make "sillier":
        lineNum = random.randint(0, 3)

        # Make a list from the line string so we can edit it. (Strings
        # in Python are immutable.)
        line = list(lines[lineNum])

        effect = random.randint(0, 3)
        if effect == 0:  # Replace a character with a space.
            charIndex = random.randint(0, len(line) - 1)
            line[charIndex] = ' '
        elif effect == 1:  # Change the casing of a character.
            charIndex = random.randint(0, len(line) - 1)
            if line[charIndex].isupper():
                line[charIndex] = line[charIndex].lower()
            elif line[charIndex].islower():
                line[charIndex] = line[charIndex].upper()
        elif effect == 2:  # Transpose two characters.
            charIndex = random.randint(0, len(line) - 2)
            firstChar = line[charIndex]
            secondChar = line[charIndex + 1]
            line[charIndex] = secondChar
            line[charIndex + 1] = firstChar
        elif effect == 3:  # Double a character.
            charIndex = random.randint(0, len(line) - 2)
            line.insert(charIndex, line[charIndex])

        # Convert the line list back to a string and put it in lines:
        lines[lineNum] = ''.join(line)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
