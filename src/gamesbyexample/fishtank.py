# Fish Tank, by Al Sweigart al@inventwithpython.com
# A peaceful animation of a fish tank. Press Ctrl-C to stop.
__version__ = 1

import random, time, sys

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you can install
by opening a Terminal window (on macOS & Linux) and running:

    python3 -m pip install --user bext

or a Command Prompt window (on Windows) and running:

    python -m pip install --user bext''')
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1 # Adjustment for a Windows newline bug that happens when you print on the right edge.

# Setup the screen.
bext.bg('black')
bext.clear()

# Constants
NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 2
PAUSE = 0.25

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
  ]
LONGEST_FISH_LENGTH = 10 # Longest single string in FISH_TYPES.


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    BUBBLERS = [] # NOTE: Bubbles are drawn, but not the bubblers themselves.
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
        time.sleep(PAUSE)
        bext.clear()
        step += 1


def getRandomColor():
    return random.choice(('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'))


def generateFish():
    fishType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random': # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength # All the same color.
    if colorPattern == 'head-tail': # Head/tail color different from body.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # set head color
        colors[-1] = headTailColor # set tail color

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
    fish['location'] = {'x': random.randint(4, WIDTH - LONGEST_FISH_LENGTH),
                        'y': random.randint(0, HEIGHT - 2)}
    return fish


def drawAquarium(step):
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Simulate the fish for one step:
    for fish in FISHES:
        # Move the fish horizontally:
        if step % fish['hspeed'] == 0:
            if fish['goingRight']:
                if fish['location']['x'] != WIDTH - 1 - LONGEST_FISH_LENGTH:
                    fish['location']['x'] += 1 # Move the fish left.
                else:
                    fish['goingRight'] = not fish['goingRight'] # Turn the fish around.
                    fish['colors'].reverse() # Turn the colors around too.
            elif not fish['goingRight']:
                if fish['location']['x'] != 0:
                    fish['location']['x'] -= 1 # Move the fish right.
                else:
                    fish['goingRight'] = not fish['goingRight'] # Turn the fish around.
                    fish['colors'].reverse() # Turn the colors around too.

        # Fish can randomly change their horizontal direction:
        fish['hchange'] -= 1
        if fish['hchange'] == 0:
            fish['hchange'] = random.randint(10, 60)
            fish['goingRight'] = not fish['goingRight'] # Turn the fish around.

        # Move the fish vertically:
        if step % fish['vspeed'] == 0:
            if fish['goingDown']:
                if fish['location']['y'] != HEIGHT - 2:
                    fish['location']['y'] += 1 # Move the fish down.
                else:
                    fish['goingDown'] = not fish['goingDown'] # Turn the fish around.
            elif not fish['goingDown']:
                if fish['location']['y'] != 0:
                    fish['location']['y'] -= 1 # Move the fish up.
                else:
                    fish['goingDown'] = not fish['goingDown'] # Turn the fish around.

        # Fish can randomly change their vertical direction:
        fish['vchange'] -= 1
        if fish['vchange'] == 0:
            fish['vchange'] = random.randint(2, 20)
            fish['goingDown'] = not fish['goingDown'] # Turn the fish around.

    # Generate bubbles from bubblers:
    for bubbler in BUBBLERS:
        if random.randint(0, 5) == 0:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    # Simulate the bubbles for one step:
    for bubble in BUBBLES:
        r = random.randint(1, 5)
        if (r == 1) and (bubble['x'] != 0):
            bubble['x'] -= 1 # Bubble goes left.
        elif (r == 2) and (bubble['x'] != WIDTH - 1):
            bubble['x'] += 1 # Bubble goes right.

        bubble['y'] -= 1 # The bubble always goes up.

    # Iterate over BUBBLES in reverse because I'm modifying BUBBLES while iterating over it.
    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == 0: # Delete bubbles that reach the top.
            del BUBBLES[i]

    # Simulate the kelp waving for one step:
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if random.randint(1, 20) == 1: # 1 in 20 chance to change waving.
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('

    # Draw the bubbles:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O', chr(176))), end='') # chr(176) is '°'

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
    print(chr(9608) * (WIDTH - 1) , end='') # Draws '█' characters.

    sys.stdout.flush() # (Required for bext-using programs.)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program.