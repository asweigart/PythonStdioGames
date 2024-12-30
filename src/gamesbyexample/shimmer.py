import random
import sys
import time

import bext

WIDTH, HEIGHT = 80, 25

CAP = max(WIDTH, HEIGHT) * 2

canvas = {}
shimmers = {}

ON = 'O'
OFF = '.'

# Starting state
bext.clear()
for y in range(HEIGHT):
    for x in range(WIDTH):
        canvas[(x, y)] = False
        print(OFF, end='')
    print()


while True:
    changed = set()

    if random.randint(1, 8) == 1:
        rx = random.randint(0, WIDTH - 1)
        ry = random.randint(0, HEIGHT - 1)
        shimmers[(rx, ry)] = 0

    toDelete = []
    for (sx, sy), sval in shimmers.items():
        if sval == 0:
            canvas[(sx, sy)] = not canvas[(sx, sy)]
            changed.add((sx, sy))
            shimmers[(sx, sy)] += 1
            continue

        for si in range(sval):
            topCoord = (sx + si, sy - sval + si)
            bottomCoord = (sx - si, sy + sval - si)
            leftCoord = (sx - sval + si, sy - si)
            rightCoord = (sx + sval - si, sy + si)

            if topCoord in canvas:
                canvas[topCoord] = not canvas[topCoord]
                changed.add(topCoord)
            if bottomCoord in canvas:
                canvas[bottomCoord] = not canvas[bottomCoord]
                changed.add(bottomCoord)
            if leftCoord in canvas:
                canvas[leftCoord] = not canvas[leftCoord]
                changed.add(leftCoord)
            if rightCoord in canvas:
                canvas[rightCoord] = not canvas[rightCoord]
                changed.add(rightCoord)
        shimmers[(sx, sy)] += 1
        if shimmers[(sx, sy)] > CAP:
            toDelete.append((sx, sy))

    for toDel in toDelete:
        del shimmers[(toDel[0], toDel[1])]

    # Draw
    for change in changed:
        bext.goto(change[0], change[1])
        if canvas[(change[0], change[1])]:
            print(ON, end='')
        else:
            print(OFF, end='')

    try:
        time.sleep(0.05)
    except KeyboardInterrupt:
        sys.exit()
