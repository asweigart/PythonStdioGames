# Switchboard 2, by Al Sweigart al@inventwithpython.com
import random, sys

# TODO - make it so that the circuits reveal themselves as you enter the buttons.

NUMBER_OF_SWITCHES = 10
assert 2 <= NUMBER_OF_SWITCHES <= 10

# Create the switchboard of the connections:
UP_DOWN_CHAR    = chr(9474) # The '│' string.
LEFT_RIGHT_CHAR = chr(9472) # The '─' string.
DOWN_ARROW_CHAR = chr(8595) # The '↓' string.
UP_ARROW_CHAR   = chr(8593) # The '↑' string.
DOWN_RIGHT_CHAR = chr(9484) # The '┌' string.
DOWN_LEFT_CHAR  = chr(9488) # The '┐' string.
UP_RIGHT_CHAR   = chr(9492) # The '└' string.
UP_LEFT_CHAR    = chr(9496) # The '┘' string.

SWITCHBOARD_INDENT = 4 # How much to indent the switch board.

# Create the switchboard status and connections:
switchboardStatus = ['X'] * NUMBER_OF_SWITCHES
connections = list(range(NUMBER_OF_SWITCHES))

# Create a random (but valid) puzzle:
while True:
    random.shuffle(connections) # Randomize the switchboard connections.

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

    if not validPuzzle:
        continue

    switchboard = {}
    # Draw the X/O status of the switchboard:
    for x in range(NUMBER_OF_SWITCHES):
        switchboard[(SWITCHBOARD_INDENT + (x * 2), NUMBER_OF_SWITCHES + 1)] = 'X'
        switchboard[(SWITCHBOARD_INDENT + (x * 2), NUMBER_OF_SWITCHES + 2)] = str(x)

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
            print(connections)
            sys.exit()
            assert False

        # Drawing the arrows
        cursorx = SWITCHBOARD_INDENT + (startSwitch * 2)
        if drawDirection == -1:
            cursory = NUMBER_OF_SWITCHES + 0
        elif drawDirection == 1:
            cursory = NUMBER_OF_SWITCHES + 3
        else:
            assert False
        # Draw the first vertical "exit" line:
        for i in range(startSwitch + 1):
            switchboard[(cursorx, cursory)] = UP_DOWN_CHAR
            cursory += drawDirection
        # Draw the first turn:
        if drawDirection == -1:
            if startSwitch < endSwitch:
                switchboard[(cursorx, cursory)] = DOWN_RIGHT_CHAR
            elif startSwitch > endSwitch:
                switchboard[(cursorx, cursory)] = DOWN_LEFT_CHAR
            else:
                assert False
        elif drawDirection == 1:
            if startSwitch < endSwitch:
                switchboard[(cursorx, cursory)] = UP_RIGHT_CHAR
            elif startSwitch > endSwitch:
                switchboard[(cursorx, cursory)] = UP_LEFT_CHAR
            else:
                assert False
        # Draw the horizontal line:
        for i in range(abs(startSwitch - endSwitch) * 2 - 1):
            if startSwitch < endSwitch:
                # Move cursorx to the right
                cursorx += 1
                switchboard[(cursorx, cursory)] = LEFT_RIGHT_CHAR
            elif startSwitch > endSwitch:
                # Move cursorx to the left
                cursorx -= 1
                switchboard[(cursorx, cursory)] = LEFT_RIGHT_CHAR
            else:
                assert False
        # Draw the second turn:
        if drawDirection == -1:
            if startSwitch < endSwitch:
                # Move cursorx to the right
                cursorx += 1
                switchboard[(cursorx, cursory)] = DOWN_LEFT_CHAR
            elif startSwitch > endSwitch:
                # Move cursorx to the left
                cursorx -= 1
                switchboard[(cursorx, cursory)] = DOWN_RIGHT_CHAR
            else:
                assert False
        elif drawDirection == 1:
            if startSwitch < endSwitch:
                # Move cursorx to the right
                cursorx += 1
                switchboard[(cursorx, cursory)] = UP_LEFT_CHAR
            elif startSwitch > endSwitch:
                # Move cursorx to the left
                cursorx -= 1
                switchboard[(cursorx, cursory)] = UP_RIGHT_CHAR
            else:
                assert False

        # Draw the vertical "entrance" line:
        cursory -= drawDirection
        for i in range(startSwitch):
            switchboard[(cursorx, cursory)] = UP_DOWN_CHAR
            cursory -= drawDirection
        if drawDirection == -1:
            switchboard[(cursorx, cursory)] = DOWN_ARROW_CHAR
        elif drawDirection == 1:
            switchboard[(cursorx, cursory)] = UP_ARROW_CHAR
        else:
            assert False

    if validPuzzle:
        break


while True: # Main game loop.
    # Update the switchboard with the current switch status:
    for x in range(NUMBER_OF_SWITCHES):
        switchboard[(SWITCHBOARD_INDENT + (x * 2), NUMBER_OF_SWITCHES + 1)] = switchboardStatus[x]

    # Draw the switchboard:
    for y in range(SWITCHBOARD_INDENT + (NUMBER_OF_SWITCHES * 2) + 1):
        for x in range(2 * NUMBER_OF_SWITCHES + 4):
            print(switchboard.get((x, y), ' '), end='')
        print()

    if switchboardStatus == ['O'] * NUMBER_OF_SWITCHES:
        print('You solved the puzzle!')
        sys.exit()

    #sys.exit()

    # Get the player's move:
    move = input(f'Switch to toggle (0─{NUMBER_OF_SWITCHES - 1}, or QUIT): ')
    if move.upper() == 'QUIT':
        sys.exit()

    if not move.isdecimal() or not (0 <= int(move) < NUMBER_OF_SWITCHES):
        continue
    move = int(move)

    #move = random.randint(0, NUMBER_OF_SWITCHES ─ 1)

    # Toggle the switch the player chose:
    if switchboardStatus[move] == 'X':
        switchboardStatus[move] = 'O'
    elif switchboardStatus[move] == 'O':
        switchboardStatus[move] = 'X'

    # Toggle the switch connected to the switch the player chose:
    if switchboardStatus[connections[move]] == 'X':
        switchboardStatus[connections[move]] = 'O'
    elif switchboardStatus[connections[move]] == 'O':
        switchboardStatus[connections[move]] = 'X'


