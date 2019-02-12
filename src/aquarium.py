# ASCII Aquarium, by Al Sweigart al@inventwithpython.com 2019/2/11

import bext, random, time, sys
WIDTH, HEIGHT = bext.size()
WIDTH -= 1 # Adjustment for the Windows newline bug.

bext.bg('black')
bext.clear()

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 2
PAUSE = 0.25

FISH_TYPES = (
  {'right': ('><>',),         'left': ('<><',)},
  {'right': ('>||>',),        'left': ('<||<',)},
  {'right': ('>))>',),        'left': ('<((<',)},
  {'right': ('>))o', '>))-'), 'left': ('o((<', '-((<')},
  {'right': ('>))o', '>)).'), 'left': ('o((<', '.((<')},
  {'right': ('>-==>',),       'left': ('<==-<',)},
  {'right': (r'>\\>',),       'left': (r'<//<',)},
  {'right': ('><)))*>',), 'left': ('<*(((><',)},
  {'right': ('}-(((*>',),     'left': ('<*)))-{',)},
  {'right': (']-<)))b>',),    'left': ('<d(((>-[',)},
  {'right': ('><XXX*>',), 'left': ('<*XXX><',)},
  {'right': ('_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'),
   'left':  ('<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.')},
  )
LONGEST_FISH_LENGTH = 10

def getRandomColor():
    return random.choice(('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'))

def generateFish():
    fishType = random.choice(FISH_TYPES)

    colorType = random.choice(('random', 'head-tail', 'same'))
    fishLength = len(fishType['right'][0])
    if colorType == 'random': # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorType == 'same' or colorType == 'head-tail':
        colors = [getRandomColor()] * fishLength # All parts have same color.
    if colorType == 'head-tail': # Head/tail & body have different colors.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # set head color
        colors[-1] = headTailColor # set tail color

    fish = {'right':      fishType['right'],
            'left':       fishType['left'],
            'frame':      random.randint(0, len(fishType['right']) - 1),
            'colors':     colors, # Color order when facing right.
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


# Generate the global variables.
FISHES = []
for i in range(NUM_FISH):
    FISHES.append(generateFish())

BUBBLERS = []
for i in range(NUM_BUBBLERS): # Have between 1 and 3 bubblers.
    BUBBLERS.append(random.randint(0, WIDTH - 1)) # Each bubbler starts at a random position.
BUBBLES = []

# Generate the kelp.
KELPS = []
for i in range(NUM_KELP):
    kelp = {'x': random.randint(0, WIDTH - 2), 'segments': []}
    for i in range(random.randint(6, HEIGHT - 1)):
        kelp['segments'].append({'char': random.choice(('(', ')')),
                                 'left-right': random.randint(0, 1)})
    KELPS.append(kelp)


def drawAquarium(step):
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Simulate the fish for one step:
    for fish in FISHES:
        fish['frame'] += 1
        if fish['frame'] >= len(fish['right']):
            fish['frame'] = 0

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

    for i in range(len(BUBBLES) - 1, -1, -1): # Iterate over BUBBLES in reverse because I'm modifying BUBBLES while iterating over it.
        if BUBBLES[i]['y'] == 0: # Delete bubbles that reach the top.
            del BUBBLES[i]

    # Simulate the kelp waving for one step:
    for kelp in KELPS:
        for kelpSegment in kelp['segments']:
            if random.randint(1, 20) == 1:
                if kelpSegment['left-right'] == 0:
                    kelpSegment['left-right'] = 1
                elif kelpSegment['left-right'] == 1:
                    kelpSegment['left-right'] = 0

    # Draw bubbles in the correct positions:
    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O', chr(176))), end='') # '°'

    # Draw the fish in the correct positions:
    for fish in FISHES:
        bext.goto(fish['location']['x'], fish['location']['y'])

        #bext.fg(fish['colors'][0])
        if fish['goingRight']:
            for i, fishPart in enumerate(fish['right'][fish['frame']]):
                bext.fg(fish['colors'][i])
                print(fishPart, end='')
        elif not fish['goingRight']:
            for i, fishPart in enumerate(fish['left'][fish['frame']]):
                bext.fg(fish['colors'][i])
                print(fishPart, end='')

    # Draw the kelp in the correct positions:
    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if i == 0:
                kelpSegment['left-right'] = 0
            bext.goto(kelp['x'] + kelpSegment['left-right'], HEIGHT - 2 - i)
            print(kelpSegment['char'], end='')

    # Draw quit message.
    bext.fg('white')
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Draw the sand on the bottom:
    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9608) * (WIDTH - 1) , end='') # '█'


def main():
    step = 1
    while True:
        try:
            drawAquarium(step)
            time.sleep(PAUSE)
            bext.clear()
            step += 1
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()