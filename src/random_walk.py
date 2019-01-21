import bext
import random, time

BLOCK = chr(9608)

# Ask user what speed to run the simulation at:
while True:
    print('Move (F)ast or (S)low?')
    speed = input().upper()
    if speed == 'F' or speed == 'S':
        break

width, height = bext.size()
bext.clear()

try:
    while True:
        bext.fg('random') # Set to a random color.
        x, y = width // 2, height // 2 # Start in the middle of the screen.

        # Display quit instructions:
        bext.goto(0, height - 2)
        print('Press Ctrl-C to quit.', end='')

        while (0 <= x < width) and (0 <= y < height):
            # Print the block at it's current location:
            bext.goto(x, y)
            print(BLOCK, end='')

            # Move the block:
            direction = random.randint(0, 3)
            if direction == 0:
                x += 1
            elif direction == 1:
                x -= 1
            elif direction == 2:
                y += 1
            elif direction == 3:
                y -= 1


            if speed == 'S':
                time.sleep(0.1)
except KeyboardInterrupt:
    pass
