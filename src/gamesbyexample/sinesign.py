"""Sine Sign, by Al Sweigart al@inventwithpython.com

Create a sine-wavy message."""

# TODO - improve comments.

import math, shutil, sys, time

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Sine Sign, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    originalMessage = input('> ')
    if 1 <= len(originalMessage) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


multipler = (WIDTH // 2)
step = 0.0
try:
    while True:  # Main program loop.
        sinOfStep = math.sin(step)
        if sinOfStep >= 0:
            message = (' ' * int(sinOfStep * multipler)) + originalMessage
        else:
            message = originalMessage + (' ' * abs(int(sinOfStep * multipler)))
        print(message.center(WIDTH))
        time.sleep(0.1)
        step += 0.3  # (!) Try changing this.
except KeyboardInterrupt:
    sys.exit()