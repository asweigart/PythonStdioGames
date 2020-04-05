"""Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.

>" )   ='')    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

Ducklings based on ASCII art designs from the now-defunct Moijie's Room:
http://www.geocities.jp/luckynopopo/
This and other games are available at https://nostarch.com/XX
Tags: large, artistic, object-oriented, scrolling"""
__version__ = 0
import random, shutil, sys, time

# Set up the constants:
PAUSE = 0.2
DENSITY = 10.0  # (!) Density can range from 0.0 to 100.0.
DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to quit...')
    time.sleep(3)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # Main program loop.
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # See if we should create a duckling in this lane:
            if ducklingObj == None and (random.randint(1, 10000) / 100) <= DENSITY:
                # Place a duckling in this lane:
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Draw a duckling if there is one in this lane:
                ducklingObj.displayNext()
                # Delete the duckling if we've finished drawing it:
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                # Draw five spaces since there is no duckling here.
                print(' ' * DUCKLING_WIDTH, end='')

        print()  # Print a newline.
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """Create a new duckling with random body features."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # Chubby ducklings can only have beady eyes.
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY])

        self.partToDisplayNext = HEAD

    def displayHead(self):
        """Prints the duckling's head."""
        if self.direction == LEFT:
            # Print the mouth:
            if self.mouth == OPEN:
                print('>', end='')
            elif self.mouth == CLOSED:
                print('=', end='')

            # Print the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                print('"', end='')
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                print('" ', end='')
            elif self.eyes == WIDE:
                print("''", end='')
            elif self.eyes == HAPPY:
                print('``', end='')

            print(') ', end='')  # Print the back of the head.

        if self.direction == RIGHT:
            print(' (', end='')  # Print the back of the head.

            # Print the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                print('"', end='')
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                print(' "', end='')
            elif self.eyes == WIDE:
                print("''", end='')
            elif self.eyes == HAPPY:
                print('``', end='')

            # Print the mouth:
            if self.mouth == OPEN:
                print('<', end='')
            elif self.mouth == CLOSED:
                print('=', end='')

        if self.body == CHUBBY:
            # Print an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            print(' ', end='')

    def displayBody(self):
        """Prints the duckling's body."""
        print('(', end='')  # Print the left side of the body.
        if self.direction == LEFT:
            # Print the interior body space:
            if self.body == CHUBBY:
                print(' ', end='')
            elif self.body == VERY_CHUBBY:
                print('  ', end='')

            # Print the wing:
            if self.wing == OUT:
                print('>', end='')
            elif self.wing == UP:
                print('^', end='')
            elif self.wing == DOWN:
                print('v', end='')

        if self.direction == RIGHT:
            # Print the wing:
            if self.wing == OUT:
                print('<', end='')
            elif self.wing == UP:
                print('^', end='')
            elif self.wing == DOWN:
                print('v', end='')

            # Print the interior body space:
            if self.body == CHUBBY:
                print(' ', end='')
            elif self.body == VERY_CHUBBY:
                print('  ', end='')

        print(')', end='')  # Print the right side of the body.

        if self.body == CHUBBY:
            # Print an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            print(' ', end='')

    def displayFeet(self):
        """Prints the duckling's feet."""
        if self.body == CHUBBY:
            print(' ^^  ', end='')
        elif self.body == VERY_CHUBBY:
            print(' ^ ^ ', end='')

    def displayNext(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets partToDisplayNext to
        None when finished."""
        if self.partToDisplayNext == HEAD:
            self.displayHead()
            self.partToDisplayNext = BODY
        elif self.partToDisplayNext == BODY:
            self.displayBody()
            self.partToDisplayNext = FEET
        elif self.partToDisplayNext == FEET:
            self.displayFeet()
            self.partToDisplayNext = None


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
