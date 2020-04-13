"""Fish Tank, by Al Sweigart al@inventwithpython.com
A peaceful animation of a fish tank. Press Ctrl-C to stop.
Similar to ASCIIQuarium, but mine is based on an older ASCII fish tank
program for DOS. https://robobunny.com/projects/asciiquarium/html/
This and other games are available at https://nostarch.com/XX
Tags: extra-large, artistic, bext"""
__version__ = 0
import random, time, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUM_KELP = 2  # (!) Try changing this number.
NUM_FISH = 10  # (!) Try changing this number.
NUM_BUBBLERS = 1  # (!) Try changing this number.
FRAMES_PER_SECOND = 4  # (!) Try changing this number.
# (!) Try changing the constants to create a fish tank with only kelp,
# or only bubblers.

FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*[[[><']},
  {'right': ['}-[[[*>'],      'left': ['<*)))-{']},
  {'right': [']-<)))b>'],     'left': ['<d[[[>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
  ]  # (!) Try adding your own fish to FISH_TYPES.
LONGEST_FISH_LENGTH = 10  # Longest single string in FISH_TYPES.

# The x position where a fish runs into the edge of the screen:
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH


def main():
    """Run the fish tank animation."""

    # Setup the screen.
    bext.bg('black')
    bext.clear()

    global FISHES, BUBBLERS, BUBBLES, KELPS

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # NOTE: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position.
        BUBBLERS.append(random.randint(0, WIDTH - 1))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelp = {'x': random.randint(0, WIDTH - 2), 'segments': []}
        # Generate each segment of the kelp.
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Run the simulation:
    step = 1
    while True:
        drawAquarium(step)
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        step += 1


def getRandomColor():
    """Return a string of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generateFish():
    """Return a dictionary that represents a fish."""
    fishType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # All the same color.
    if colorPattern == 'head-tail':  # Head/tail different from body.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # Set head color.
        colors[-1] = headTailColor  # Set tail color.

    # Set up the rest of fish data structure:
    fish = {'right':      fishType['right'],
            'left':       fishType['left'],
            'colors':     colors,
            'hspeed':     random.randint(1, 6),
            'vspeed':     random.randint(5, 15),
            'hchange':    random.randint(10, 60),
            'vchange':    random.randint(2, 20),
            'goingRight': random.choice((True, False)),
            'goingDown':  random.choice((True, False))}

    # 'location' is always the leftmost side of the fish body:
    xStartingLocation = random.randint(4, WIDTH - LONGEST_FISH_LENGTH)
    yStartingLocation = random.randint(0, HEIGHT - 2)
    fish['location'] = {'x': xStartingLocation, 'y': yStartingLocation}
    return fish


def drawAquarium(step):
    """Draw the aquarium on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Simulate the fish for one step:
    for fish in FISHES:
        # Move the fish horizontally:
        if step % fish['hspeed'] == 0:
            if fish['goingRight']:
                if fish['location']['x'] != RIGHT_EDGE:
                    fish['location']['x'] += 1  # Move the fish left.
                else:
                    # Turn the fish around:
                    fish['goingRight'] = not fish['goingRight']
                    fish['colors'].reverse()  # Turn the colors around.
            elif not fish['goingRight']:
                if fish['location']['x'] != 0:
                    fish['location']['x'] -= 1  # Move the fish right.
                else:
                    # Turn the fish around:
                    fish['goingRight'] = not fish['goingRight']
                    fish['colors'].reverse()  # Turn the colors around.

        # Fish can randomly change their horizontal direction:
        fish['hchange'] -= 1
        if fish['hchange'] == 0:
            fish['hchange'] = random.randint(10, 60)
            # Turn the fish around:
            fish['goingRight'] = not fish['goingRight']

        # Move the fish vertically:
        if step % fish['vspeed'] == 0:
            if fish['goingDown']:
                if fish['location']['y'] != HEIGHT - 2:
                    fish['location']['y'] += 1  # Move the fish down.
                else:
                    # Turn the fish around:
                    fish['goingDown'] = not fish['goingDown']
            elif not fish['goingDown']:
                if fish['location']['y'] != 0:
                    fish['location']['y'] -= 1  # Move the fish up.
                else:
                    # Turn the fish around:
                    fish['goingDown'] = not fish['goingDown']

        # Fish can randomly change their vertical direction:
        fish['vchange'] -= 1
        if fish['vchange'] == 0:
            fish['vchange'] = random.randint(2, 20)
            # Turn the fish around:
            fish['goingDown'] = not fish['goingDown']

    # Generate bubbles from bubblers:
    for bubbler in BUBBLERS:
        if random.randint(0, 5) == 0:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # Simulate the bubbles for one step:
    for bubble in BUBBLES:
        r = random.randint(1, 5)
        if (r == 1) and (bubble['x'] != 0):
            bubble['x'] -= 1  # Bubble goes left.
        elif (r == 2) and (bubble['x'] != WIDTH - 1):
            bubble['x'] += 1  # Bubble goes right.

        bubble['y'] -= 1  # The bubble always goes up.

    # Iterate over BUBBLES in reverse because I'm modifying BUBBLES
    # while iterating over it.
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == 0:  # Delete bubbles that reach the top.
            del BUBBLES[i]

    # Simulate the kelp waving for one step:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 1 in 20 chance to change waving:
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('

    # Draw the bubbles:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish['location']['x'], fish['location']['y'])

        # Get the correct right- or left-facing fish text.
        if fish['goingRight']:
            fishText = fish['right'][step % len(fish['right'])]
        elif not fish['goingRight']:
            fishText = fish['left'][step % len(fish['left'])]

        # Draw each character of the fish text in the right color.
        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    # Draw the kelp:
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if i == 0:
                # Bottom segment is always (.
                kelp['segments'][i] = '('
            if kelpSegment == '(':
                bext.goto(kelp['x'], HEIGHT - 2 - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, HEIGHT - 2 - i)
            print(kelpSegment, end='')

    # Draw quit message.
    bext.fg('white')
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Draw the sand on the bottom:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9608) * (WIDTH - 1), end='')  # Draws '█' characters.

    sys.stdout.flush()  # (Required for bext-using programs.)


def clearAquarium():
    """Draw empty spaces over everything on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Draw the bubbles:
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish['location']['x'], fish['location']['y'])

        # Draw each character of the fish text in the right color.
        print(' ' * len(fish['left'][0]), end='')

    # Draw the kelp:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()  # (Required for bext-using programs.)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
