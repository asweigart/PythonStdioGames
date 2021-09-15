"""Bouncing DVD Logo (barebones version)
by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop."""
import sys, random, time, bext

WIDTH, HEIGHT = bext.size()
WIDTH -= 1  # Adjust width for a Windows bug.

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
DIRECTIONS = ['UR', 'UL', 'DR', 'DL']


def main():
    bext.clear()
    logo = {'color': random.choice(COLORS),
            'x': random.randint(1, WIDTH - 4),
            'y': random.randint(1, HEIGHT - 4),
            'dir': random.choice(DIRECTIONS)}
    if logo['x'] % 2 == 1:
        logo['x'] -= 1  # Make sure X is even so it can hit the corner.

    while True:  # Main program loop.
        # Erase the logo's current location:
        bext.goto(logo['x'], logo['y'])
        print('   ', end='')  # (!) Try commenting this line out.

        originalDirection = logo['dir']

        # See if the logo bounces off the corners:
        if logo['x'] == 0 and logo['y'] == 0:
            logo['dir'] = 'DR'
        elif logo['x'] == 0 and logo['y'] == HEIGHT - 1:
            logo['dir'] = 'UR'
        elif logo['x'] == WIDTH - 3 and logo['y'] == 0:
            logo['dir'] = 'DL'
        elif logo['x'] == WIDTH - 3 and logo['y'] == HEIGHT - 1:
            logo['dir'] = 'UL'

        # See if the logo bounces off the left edge:
        elif logo['x'] == 0 and logo['dir'] == 'UL':
            logo['dir'] = 'UR'
        elif logo['x'] == 0 and logo['dir'] == 'DL':
            logo['dir'] = 'DR'

        # See if the logo bounces off the right edge:
        # (WIDTH - 3 because 'DVD' has 3 letters.)
        elif logo['x'] == WIDTH - 3 and logo['dir'] == 'UR':
            logo['dir'] = 'UL'
        elif logo['x'] == WIDTH - 3 and logo['dir'] == 'DR':
            logo['dir'] = 'DL'

        # See if the logo bounces off the top edge:
        elif logo['y'] == 0 and logo['dir'] == 'UL':
            logo['dir'] = 'DL'
        elif logo['y'] == 0 and logo['dir'] == 'UR':
            logo['dir'] = 'DR'

        # See if the logo bounces off the bottom edge:
        elif logo['y'] == HEIGHT - 1 and logo['dir'] == 'DL':
            logo['dir'] = 'UL'
        elif logo['y'] == HEIGHT - 1 and logo['dir'] == 'DR':
            logo['dir'] = 'UR'

        if logo['dir'] != originalDirection:
            # Change color when the logo bounces:
            logo['color'] = random.choice(COLORS)

        # Move the logo. (X moves by 2 because the terminal
        # characters are twice as tall as they are wide.)
        if logo['dir'] == 'UR':
            logo['x'] += 2
            logo['y'] -= 1
        elif logo['dir'] == 'UL':
            logo['x'] -= 2
            logo['y'] -= 1
        elif logo['dir'] == 'DR':
            logo['x'] += 2
            logo['y'] += 1
        elif logo['dir'] == 'DL':
            logo['x'] -= 2
            logo['y'] += 1

        # Draw the logo at its new location:
        bext.goto(logo['x'], logo['y'])
        bext.fg(logo['color'])
        print('DVD', end='')

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(0.2)


# Call the main() function to play the animation:
try:
    main()
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
