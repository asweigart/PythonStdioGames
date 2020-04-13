"""Ninety Nine Bottles of Milk on the Wall
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the most longest songs ever!
Press Ctrl-C to stop.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, scrolling"""
__version__ = 0
import sys, time

print('Ninety Nine Bottles, by Al Sweigart al@inventwithpython.com')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99  # This is the starting number of bottles.
PAUSE = 2  # (!) Try changing this to 0 to see the full song at once.

try:
    while bottles > 1:  # Keep looping and display the lyrics.
        print(bottles, 'bottles of milk on the wall,')
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.
        print(bottles, 'bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1  # Decrease the number of bottles by one.
        print(bottles, 'bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()  # Print a newline.

    # Display the last stanza:
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
s