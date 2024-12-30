"""Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, object-oriented, scrolling"""
__version__ = 0
import random, shutil, sys, time

# Set up the constants:
PAUSE = 0.2  # (!) Try changing this to 1.0 or 0.0.
DENSITY = 0.10  # (!) Try changing this to anything from 0.0 to 1.0.

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
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
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # Main program loop.
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # See if we should create a duckling in this lane:
            if (ducklingObj == None and random.random() <= DENSITY):
                    # Place a duckling in this lane:
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                # Draw a duckling if there is one in this lane:
                print(ducklingObj.getNextBodyPart(), end='')
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
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """Returns the string of the duckling's head."""
        headStr = ''
        if self.direction == LEFT:
            # Get the mouth:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') '  # Get the back of the head.

        if self.direction == RIGHT:
            headStr += ' ('  # Get the back of the head.

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # Get the mouth:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            headStr += ' '

        return headStr

    def getBodyStr(self):
        """Returns the string of the duckling's body."""
        bodyStr = '('  # Get the left side of the body.
        if self.direction == LEFT:
            # Get the interior body space:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            # Get the wing:
            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:
            # Get the wing:
            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            # Get the interior body space:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'  # Get the right side of the body.

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            bodyStr += ' '

        return bodyStr

    def getFeetStr(self):
        """Returns the string of the duckling's feet."""
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    def getNextBodyPart(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets partToDisplayNext to
        None when finished."""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
