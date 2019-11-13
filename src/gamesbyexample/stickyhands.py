# Sticky Hands, by Al Sweigart al@inventwithpython.com
# A jewel-stealing, movement puzzle game.
# Inspired by Herding Cats https://w.itch.io/herding-cats

# TODO - Enter R to reset the entire level.

import copy, os, sys

# Setup the constants:
WALL = chr(9608)
FACE = chr(9786)
DIAMOND = chr(9830)
CHAR_MAP = {'#': WALL, '@': FACE, '$': DIAMOND, ' ': ' '} # TODO add comment

# Display the title banner and instructions:
print('''Sticky Hands: A diamond collecting game.
By Al Sweigart al@inventwithpython.com

Pick up diamonds by standing next to them. Stuck diamonds also
become sticky. Try to stick every diamond in the level.
Enter WASD letters to move, numbers to switch levels, U to undo a
move, or "quit" to quit the game. You can enter multiple WASD or U
letters to make several moves at once.
''')


# Load each level from stickyhandslevels.txt
if not os.path.exists('stickyhandslevels.txt'):
    print('Download the level file from https://github.com/asweigart/PythonStdioGames/blob/master/src/stickyhandslevels.txt')
    sys.exit()
ALL_LEVELS = []
with open('stickyhandslevels.txt') as levelFile:
    currentLevelFromFile = {'width': 0, 'height': 0, 'diamonds': 0} # Each level is represented by a dictionary.
    y = 0
    for line in levelFile.readlines():
        if line.startswith(';'):
            continue # Ignore comments in the level file.

        if line == '\n':
            if currentLevelFromFile == {'width': 0, 'height': 0, 'diamonds': 0}:
                continue # Ignore this line, and continue to the next line.
            # Finished with the current level:
            ALL_LEVELS.append(currentLevelFromFile)
            currentLevelFromFile = {'width': 0, 'height': 0, 'diamonds': 0}
            y = 0 # Reset y back to 0.
            continue

        # Add the line to the current level.
        # We use line[:-1] so we don't include the newline:
        for x, levelChar in enumerate(line[:-1]):
            currentLevelFromFile[(x, y)] = levelChar

            # Keep track of how many diamonds are in the level:
            if levelChar == '$':
                currentLevelFromFile['diamonds'] += 1
        y += 1

        if len(line) - 1 > currentLevelFromFile['width']:
            currentLevelFromFile['width'] = len(line) - 1
        if y > currentLevelFromFile['height']:
            currentLevelFromFile['height'] = y


def drawLevel(levelNum, levelData):
    # Draw the current level.
    print('Level #' + str(levelNum + 1), 'of', len(ALL_LEVELS))
    for y in range(levelData['height']):
        for x in range(levelData['width']):
            prettyChar = CHAR_MAP[levelData.get((x, y), ' ')]
            print(prettyChar, end='')
        print()

def getPlayerBlobPoints(levelData, playerx, playery):
    playerBlob = [(playerx, playery)]
    pointsToCheck = [(playerx, playery)]
    alreadyCheckedPoints = []

    while len(pointsToCheck) > 0:
        x, y = pointsToCheck.pop()

        alreadyCheckedPoints.append((x, y))

        if (x - 1, y) not in alreadyCheckedPoints and levelData[(x - 1, y)] == '$':
            playerBlob.append((x - 1, y))
            pointsToCheck.append((x - 1, y))
        if (x + 1, y) not in alreadyCheckedPoints and levelData[(x + 1, y)] == '$':
            playerBlob.append((x + 1, y))
            pointsToCheck.append((x + 1, y))
        if (x, y - 1) not in alreadyCheckedPoints and levelData[(x, y - 1)] == '$':
            playerBlob.append((x, y - 1))
            pointsToCheck.append((x, y - 1))
        if (x, y + 1) not in alreadyCheckedPoints and levelData[(x, y + 1)] == '$':
            playerBlob.append((x, y + 1))
            pointsToCheck.append((x, y + 1))

    return playerBlob




currentLevelNumber = 0
currentLevel = copy.copy(ALL_LEVELS[currentLevelNumber])
undoStack = [copy.copy(currentLevel)]

while True: # Main game loop.
    drawLevel(currentLevelNumber, currentLevel)

    # Get the input from the player:
    moves = input('Enter moves> ').upper()

    if moves == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    if moves.isdecimal():
        if not (1 <= int(moves) < len(ALL_LEVELS)):
            print('Enter a level number between 1 and', len(ALL_LEVELS))
            continue
        # Change the current level:
        currentLevelNumber = int(moves) - 1
        currentLevel = copy.copy(ALL_LEVELS[currentLevelNumber])
        undoStack = [copy.copy(currentLevel)]
        continue

    # Validate the input; make sure it only has W, A, S, D, or U:
    movesAreValid = True
    for move in moves:
        if move not in ('W', 'A', 'S', 'D', 'U'):
            movesAreValid = False
            print(move, 'is not a valid move.')
            break
    if not movesAreValid:
        continue

    # Carry out the moves:
    for move in moves:
        # Find the player position:
        for position, character in currentLevel.items():
            if character == '@':
                playerx, playery = position

        if move == 'U':
            if len(undoStack) == 1:
                continue # Can't undo past the first move.
            undoStack.pop() # Remove the last item from the undoStack list.
            currentLevel = copy.copy(undoStack[-1])
            continue

        if move == 'W':
            movex, movey = 0, -1
        elif move == 'A':
            movex, movey = -1, 0
        elif move == 'S':
            movex, movey = 0, 1
        elif move == 'D':
            movex, movey = 1, 0



        playerBlob = getPlayerBlobPoints(currentLevel, playerx, playery)
        blobCanMove = True

        for blobPoint in playerBlob:
            blobx, bloby = blobPoint[0], blobPoint[1]
            moveToSpace = currentLevel.get((blobx + movex, bloby + movey), ' ')

            # If the move-to space is a wall, don't move at all:
            if moveToSpace == '#':
                blobCanMove = False
                break

        if blobCanMove:
            newBlobPoints = []
            for blobPoint in playerBlob:
                blobx, bloby = blobPoint[0], blobPoint[1]

                # If the move-to space is empty or a goal, just move there:
                if currentLevel[(blobx, bloby)] == '@':
                    currentLevel[(blobx, bloby)] = ' '
                    newBlobPoints.append((blobx + movex, bloby + movey, '@'))
                elif currentLevel[(blobx, bloby)] == '$':
                    currentLevel[(blobx, bloby)] = ' '
                    newBlobPoints.append((blobx + movex, bloby + movey, '$'))

            for newBlobPoint in newBlobPoints:
                # Set the player's new position:
                currentLevel[(newBlobPoint[0], newBlobPoint[1])] = newBlobPoint[2] # TODO - refactor this.

        # Save the state of the level for the undo feature:
        undoStack.append(copy.copy(currentLevel))

        # Check if the player has finished the level:
        levelIsSolved = False
        playerBlob = getPlayerBlobPoints(currentLevel, playerx + movex, playery + movey)
        if len(playerBlob) - 1 == currentLevel['diamonds']:
            levelIsSolved = True

        if levelIsSolved:
            drawLevel(currentLevelNumber, currentLevel)
            print('Level complete!')
            input('Press Enter to continue...')
            currentLevelNumber = (currentLevelNumber + 1) % len(ALL_LEVELS)
            currentLevel = copy.copy(ALL_LEVELS[currentLevelNumber])
            undoStack = [copy.copy(currentLevel)]
            break # Don't carry out any remaining moves.
