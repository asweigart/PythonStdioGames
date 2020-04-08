"""Sine Message, by Al Sweigart al@inventwithpython.com
Create a sine-wavy message.
This and other games are available at https://nostarch.com/XX
Tags: tiny, artistic"""
__version__ = 0
import math, shutil, sys, time

# Get the size of the terminal window:
WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Sine Message, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Message must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0  # The "step" determines how far into the sine wave we are.
# Sine goes from -1.0 to 1.0, so we need to change it by a multiplier:
multipler = WIDTH - len(message)
try:
    while True:  # Main program loop.
        sinOfStep = math.sin(step)
        padding = ' ' * abs(int(sinOfStep * multipler))
        if sinOfStep >= 0:
            paddedMessage = padding + message
        else:
            paddedMessage = message + padding
        print(paddedMessage.center(WIDTH))
        time.sleep(0.1)
        step += 0.25  # (!) Try changing this.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.