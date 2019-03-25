# Switch Switch 2 by Al Sweigart, al@inventwithpython.com
import random, sys

NUMBER_OF_SWITCHES = 10
assert 2 <= NUMBER_OF_SWITCHES <= 10


# Create the canvas of the connections:
UP_DOWN_CHAR    = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_ARROW_CHAR = chr(8595)
UP_ARROW_CHAR   = chr(8593)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR  = chr(9488)
UP_RIGHT_CHAR   = chr(9492)
UP_LEFT_CHAR    = chr(9496)

CANVAS_INDENT = 4
"""
          ┌─┐
          │ │
        ┌─│─│─┐
        │ │ │ │
    ┌─┐ │ │ │ │
    │ ↓ │ ↓ │ ↓
    O O O O O O
    0 1 2 3 4 5
    ↑ │ ↑ │ ↑ │
    │ │ │ │ │ │
    └─┘ │ │ │ │
        │ │ │ │
        └─┘ │ │
            │ │
            └─┘
"""


switches = ['X'] * NUMBER_OF_SWITCHES
connections = list(range(NUMBER_OF_SWITCHES))
while True:
    random.shuffle(connections)

    # Check for odd─numbered loops. Valid puzzles can only have even─numbered loops.
    validPuzzle = True
    for startingSwitch in range(NUMBER_OF_SWITCHES):
        currentSwitch = startingSwitch
        hops = 0
        while hops == 0 or currentSwitch != startingSwitch:
            currentSwitch = connections[currentSwitch]
            hops += 1
        if hops % 2 == 1:
            # This is an odd─numbered loop, so the puzzle is invalid
            validPuzzle = False
            break

    try:
        canvas = {}
        # Draw the X/O switches:
        for x in range(NUMBER_OF_SWITCHES):
            canvas[(CANVAS_INDENT + (x * 2), NUMBER_OF_SWITCHES + 1)] = 'X'
            canvas[(CANVAS_INDENT + (x * 2), NUMBER_OF_SWITCHES + 2)] = str(x)

        topFree = [True] * NUMBER_OF_SWITCHES
        bottomFree = [True] * NUMBER_OF_SWITCHES
        #print('debug: connections =', connections)
        for startSwitch in range(NUMBER_OF_SWITCHES):
            #print('debug: startSwitch =', startSwitch)
            #print('debug: topFree     =', topFree)
            #print('debug: bottomFree  =', bottomFree)
            endSwitch = connections[startSwitch]
            # Decide to draw the arrow on the top or bottom
            if topFree[startSwitch] and topFree[endSwitch]:
                drawDirection = -1
                topFree[startSwitch] = False
                topFree[endSwitch] = False
            elif bottomFree[startSwitch] and bottomFree[endSwitch]:
                drawDirection = 1
                bottomFree[startSwitch] = False
                bottomFree[endSwitch] = False
            else:
                raise Exception()

            # Drawing the arrows
            cursorx = CANVAS_INDENT + (startSwitch * 2)
            if drawDirection == -1:
                cursory = NUMBER_OF_SWITCHES + 0
            elif drawDirection == 1:
                cursory = NUMBER_OF_SWITCHES + 3
            else:
                assert False
            # Draw the first vertical "exit" line:
            for i in range(startSwitch + 1):
                canvas[(cursorx, cursory)] = UP_DOWN_CHAR
                cursory += drawDirection
            # Draw the first turn:
            if drawDirection == -1:
                if startSwitch < endSwitch:
                    canvas[(cursorx, cursory)] = DOWN_RIGHT_CHAR
                elif startSwitch > endSwitch:
                    canvas[(cursorx, cursory)] = DOWN_LEFT_CHAR
                else:
                    assert False
            elif drawDirection == 1:
                if startSwitch < endSwitch:
                    canvas[(cursorx, cursory)] = UP_RIGHT_CHAR
                elif startSwitch > endSwitch:
                    canvas[(cursorx, cursory)] = UP_LEFT_CHAR
                else:
                    assert False
            # Draw the horizontal line:
            for i in range(abs(startSwitch - endSwitch) * 2 - 1):
                if startSwitch < endSwitch:
                    # Move cursorx to the right
                    cursorx += 1
                    canvas[(cursorx, cursory)] = LEFT_RIGHT_CHAR
                elif startSwitch > endSwitch:
                    # Move cursorx to the left
                    cursorx -= 1
                    canvas[(cursorx, cursory)] = LEFT_RIGHT_CHAR
                else:
                    assert False
            # Draw the second turn:
            if drawDirection == -1:
                if startSwitch < endSwitch:
                    # Move cursorx to the right
                    cursorx += 1
                    canvas[(cursorx, cursory)] = DOWN_LEFT_CHAR
                elif startSwitch > endSwitch:
                    # Move cursorx to the left
                    cursorx -= 1
                    canvas[(cursorx, cursory)] = DOWN_RIGHT_CHAR
                else:
                    assert False
            elif drawDirection == 1:
                if startSwitch < endSwitch:
                    # Move cursorx to the right
                    cursorx += 1
                    canvas[(cursorx, cursory)] = UP_LEFT_CHAR
                elif startSwitch > endSwitch:
                    # Move cursorx to the left
                    cursorx -= 1
                    canvas[(cursorx, cursory)] = UP_RIGHT_CHAR
                else:
                    assert False

            # Draw the vertical "entrance" line:
            cursory -= drawDirection
            for i in range(startSwitch):
                canvas[(cursorx, cursory)] = UP_DOWN_CHAR
                cursory -= drawDirection
            if drawDirection == -1:
                canvas[(cursorx, cursory)] = DOWN_ARROW_CHAR
            elif drawDirection == 1:
                canvas[(cursorx, cursory)] = UP_ARROW_CHAR
            else:
                assert False
    except Exception:
        validPuzzle = False

    if validPuzzle:
        break


while True: # Main game loop.
    # Update the canvas with the current switch status:
    for x in range(NUMBER_OF_SWITCHES):
        canvas[(CANVAS_INDENT + (x * 2), NUMBER_OF_SWITCHES + 1)] = switches[x]

    # Draw the canvas:
    for y in range(CANVAS_INDENT + (NUMBER_OF_SWITCHES * 2) + 1):
        for x in range(2 * NUMBER_OF_SWITCHES + 4):
            print(canvas.get((x, y), ' '), end='')
        print()

    if switches == ['O'] * NUMBER_OF_SWITCHES:
        print('You solved the puzzle!')
        sys.exit()

    #sys.exit()

    # Get the player's move:
    move = input('Switch to toggle (0─%s): ' % (NUMBER_OF_SWITCHES - 1))
    if move.lower() == 'quit':
        sys.exit()

    if not move.isdigit() or not (0 <= int(move) < NUMBER_OF_SWITCHES):
        continue
    move = int(move)

    #move = random.randint(0, NUMBER_OF_SWITCHES ─ 1)

    # Toggle the switch the player chose:
    if switches[move] == 'X':
        switches[move] = 'O'
    elif switches[move] == 'O':
        switches[move] = 'X'

    # Toggle the switch connected to the switch the player chose:
    if switches[connections[move]] == 'X':
        switches[connections[move]] = 'O'
    elif switches[connections[move]] == 'O':
        switches[connections[move]] = 'X'


