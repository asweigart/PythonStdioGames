"""Sokoban clone, by Al Sweigart al@inventwithpython.com

The classic crate-pushing game."""
__version__ = 1

import copy, os, sys

# Setup the constants:
WALL = chr(9608)
FACE = chr(9786)
CRATE = chr(9679)
GOAL = chr(9675)
CRATE_ON_GOAL = '*'
PLAYER_ON_GOAL = FACE
CHAR_MAP = {'#': WALL, '@': FACE, '$': CRATE, '+': PLAYER_ON_GOAL,
            '.': GOAL, '*': CRATE_ON_GOAL, ' ': ' '} # TODO add comment

# Display the title banner and instructions:
print('''SOKOBAN: The classic crate-pushing game.
By Al Sweigart al@inventwithpython.com

Push the solid crates onto the squares. You can only push, you
can\'t pull them. Enter WASD letters to move, numbers to switch
levels, U to undo a move, or "quit" to quit the game.
You can enter multiple WASD or U letters to make several moves at
once.
''')

# Load each level from sokobanlevels.txt
if not os.path.exists('sokobanlevels.txt'):
    print('Download the level file from https://github.com/asweigart/PythonStdioGames/blob/master/src/sokobanlevels.txt')
    sys.exit()
ALL_LEVELS = []
with open('sokobanlevels.txt') as levelFile:
    currentLevelFromFile = {'width': 0, 'height': 0} # Each level is represented by a dictionary.
    y = 0
    for line in levelFile.readlines():
        if line.startswith(';'):
            continue # Ignore comments in the level file.

        if line == '\n':
            if currentLevelFromFile == {'width': 0, 'height': 0}:
                continue # Ignore this line, and continue to the next line.
            # Finished with the current level:
            ALL_LEVELS.append(currentLevelFromFile)
            currentLevelFromFile = {'width': 0, 'height': 0}
            y = 0 # Reset y back to 0.
            continue

        # Add the line to the current level.
        # We use line[:-1] so we don't include the newline:
        for x, levelChar in enumerate(line[:-1]):
            currentLevelFromFile[(x, y)] = levelChar
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
            if character in ('@', '+'):
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

        moveToSpace = currentLevel.get((playerx + movex, playery + movey), ' ')

        # If the move-to space is empty or a goal, just move there:
        if moveToSpace in (' ', '.'):
            # Change the player's old position:
            if currentLevel[(playerx, playery)] == '@':
                currentLevel[(playerx, playery)] = ' '
            elif currentLevel[(playerx, playery)] == '+':
                currentLevel[(playerx, playery)] = '.'

            # Set the player's new position:
            if moveToSpace == ' ':
                currentLevel[(playerx + movex, playery + movey)] = '@'
            elif moveToSpace == '.':
                currentLevel[(playerx + movex, playery + movey)] = '+'

        # If the move-to space is a wall, don't move at all:
        elif moveToSpace == '#':
            pass

        # If the move-to space is a crate, determine if we can push it:
        elif moveToSpace in ('$', '*'):
            spaceAfterMoveToSpace = currentLevel.get((playerx + (movex * 2), playery + (movey * 2)), ' ')
            if spaceAfterMoveToSpace in ('#', '$', '*'):
                continue # Can't push the crate because there's a wall or crate behind it.
            if spaceAfterMoveToSpace in ('.', ' '):
                # Change the player's old position:
                if currentLevel[(playerx, playery)] == '@':
                    currentLevel[(playerx, playery)] = ' '
                elif currentLevel[(playerx, playery)] == '+':
                    currentLevel[(playerx, playery)] = '.'

                # Set the player's new position:
                if moveToSpace == '$':
                    currentLevel[(playerx + movex, playery + movey)] = '@'
                elif moveToSpace == '*':
                    currentLevel[(playerx + movex, playery + movey)] = '+'

                # Set the crate's new position:
                if spaceAfterMoveToSpace == ' ':
                    currentLevel[(playerx + (movex * 2), playery + (movey * 2))] = '$'
                elif spaceAfterMoveToSpace == '.':
                    currentLevel[(playerx + (movex * 2), playery + (movey * 2))] = '*'

        # Save the state of the level for the undo feature:
        undoStack.append(copy.copy(currentLevel))

        # Check if the player has finished the level:
        levelIsSolved = True
        for position, character in currentLevel.items():
            if character == '$':
                levelIsSolved = False
                break
        if levelIsSolved:
            drawLevel(currentLevelNumber, currentLevel)
            print('Level complete!')
            input('Press Enter to continue...')
            currentLevelNumber = (currentLevelNumber + 1) % len(ALL_LEVELS)
            currentLevel = copy.copy(ALL_LEVELS[currentLevelNumber])
            undoStack = [copy.copy(currentLevel)]
            break # Don't carry out any remaining moves.
    # At this point, go back to the start of the main game loop.
