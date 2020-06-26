"""Sokoban Crate Pushing Game, by Al Sweigart al@inventwithpython.com
The classic crate-pushing game originally by Hiroyuki Imabayashi
More info at: https://en.wikipedia.org/wiki/Sokoban
This and other games are available at https://nostarch.com/XX
Tags: large, game, puzzle game"""
__version__ = 0
import copy, os, sys

# Set up the constants:
WIDTH = 'width'
HEIGHT = 'height'

# Characters in level files that represent objects:
WALL = '#'
FACE = '@'
CRATE = '$'
GOAL = '.'
CRATE_ON_GOAL = '*'
PLAYER_ON_GOAL = '+'
EMPTY = ' '

# How objects should be displayed on the screen:
WALL_DISPLAY = chr(9617)   # Character 9617 is '░'
FACE_DISPLAY = '@'
CRATE_DISPLAY = chr(9642)  # Character 9679 is '▪'
GOAL_DISPLAY = chr(9643)   # Character 9633 is '▫'
# A list of chr() codes is at https://inventwithpython.com/chr
CRATE_ON_GOAL_DISPLAY = '*'
PLAYER_ON_GOAL_DISPLAY = FACE_DISPLAY
EMPTY_DISPLAY = ' '

CHAR_MAP = {WALL: WALL_DISPLAY, FACE: FACE_DISPLAY,
            CRATE: CRATE_DISPLAY, PLAYER_ON_GOAL: PLAYER_ON_GOAL_DISPLAY,
            GOAL: GOAL_DISPLAY, CRATE_ON_GOAL: CRATE_ON_GOAL_DISPLAY,
            EMPTY: EMPTY_DISPLAY}


def main():
    # Display the instructions:
    print('''Sokoban: The classic crate-pushing game.
By Al Sweigart al@inventwithpython.com

Push the solid crates onto the circle outlines. You can only push,
you cannot pull. Enter W-A-S-D letters to move up-left-down-right,
respectively. Enter numbers to switch levels, U to undo a move, or
QUIT to quit the game.
''')

    allLevels = loadLevels('sokobanlevels.txt')
    currentLevelNum = 0
    currentLevel = copy.copy(allLevels[currentLevelNum])
    undoStack = [copy.copy(currentLevel)]

    while True:  # Main game loop.
        displayLevel(currentLevelNum, len(allLevels), currentLevel)
        move = askForPlayerMove(len(allLevels))

        # Change to a different level:
        if move.isdecimal():
            currentLevelNum = int(move)  # Set new level number.
            # Refresh the level data and undo stack:
            currentLevel = copy.copy(allLevels[currentLevelNum])
            undoStack = [copy.copy(currentLevel)]
            continue

        # Undo the last move.
        if move == 'U':
            if len(undoStack) == 1:
                continue  # Can't undo past the first move.
            undoStack.pop()  # Remove the last item from undoStack.
            currentLevel = copy.copy(undoStack[-1])
            continue

        # Find the player position:
        for position, character in currentLevel.items():
            if character in (FACE, PLAYER_ON_GOAL):
                playerX, playerY = position

        if move == 'W':
            moveX, moveY = 0, -1
        elif move == 'A':
            moveX, moveY = -1, 0
        elif move == 'S':
            moveX, moveY = 0, 1
        elif move == 'D':
            moveX, moveY = 1, 0
        moveToX = playerX + moveX
        moveToY = playerY + moveY

        moveToSpace = currentLevel.get((moveToX, moveToY), EMPTY)

        # If the move-to space is empty or a goal, just move there:
        if moveToSpace == EMPTY or moveToSpace == GOAL:
            # Change the player's old position:
            if currentLevel[(playerX, playerY)] == FACE:
                currentLevel[(playerX, playerY)] = EMPTY
            elif currentLevel[(playerX, playerY)] == PLAYER_ON_GOAL:
                currentLevel[(playerX, playerY)] = GOAL

            # Set the player's new position:
            if moveToSpace == EMPTY:
                currentLevel[(moveToX, moveToY)] = FACE
            elif moveToSpace == GOAL:
                currentLevel[(moveToX, moveToY)] = PLAYER_ON_GOAL

        # If the move-to space is a wall, don't move at all:
        elif moveToSpace == WALL:
            pass

        # If the move-to space has a crate, see if we can push it:
        elif moveToSpace in (CRATE, CRATE_ON_GOAL):
            behindMoveToX = playerX + (moveX * 2)
            behindMoveToY = playerY + (moveY * 2)
            behindMoveToSpace = currentLevel.get((behindMoveToX, behindMoveToY), EMPTY)
            if behindMoveToSpace in (WALL, CRATE, CRATE_ON_GOAL):
                # Can't push the crate because there's a wall or
                # crate behind it:
                continue
            if behindMoveToSpace in (GOAL, EMPTY):
                # Change the player's old position:
                if currentLevel[(playerX, playerY)] == FACE:
                    currentLevel[(playerX, playerY)] = EMPTY
                elif currentLevel[(playerX, playerY)] == PLAYER_ON_GOAL:
                    currentLevel[(playerX, playerY)] = GOAL

                # Set the player's new position:
                if moveToSpace == CRATE:
                    currentLevel[(moveToX, moveToY)] = FACE
                elif moveToSpace == CRATE_ON_GOAL:
                    currentLevel[(moveToX, moveToY)] = PLAYER_ON_GOAL

                # Set the crate's new position:
                if behindMoveToSpace == EMPTY:
                    currentLevel[(behindMoveToX, behindMoveToY)] = CRATE
                elif behindMoveToSpace == GOAL:
                    currentLevel[(behindMoveToX, behindMoveToY)] = CRATE_ON_GOAL

        # Save the state of the level for the undo feature:
        undoStack.append(copy.copy(currentLevel))

        # Check if the player has finished the level:
        levelIsSolved = True
        for position, character in currentLevel.items():
            if character == CRATE:
                levelIsSolved = False
                break
        if levelIsSolved:
            displayLevel(currentLevelNum, len(allLevels), currentLevel)
            print('Level complete!')
            input('Press Enter to continue...')
            currentLevelNum = (currentLevelNum + 1) % len(allLevels)
            currentLevel = copy.copy(allLevels[currentLevelNum])
            undoStack = [copy.copy(currentLevel)]


def loadLevels(levelFilename):
    if not os.path.exists('sokobanlevels.txt'):
        print('Error: Cannot find the level file. Download it from')
        print('https://inventwithpython.com/sokobanlevels.txt')
        sys.exit()
    allLevels = []
    with open(levelFilename) as levelFile:
        # Each level is represented by a dictionary:
        currentLevelFromFile = {WIDTH: 0, HEIGHT: 0}
        y = 0
        for line in levelFile.readlines():
            if line.startswith(';'):
                continue  # Ignore comments in the level file.

            if line == '\n':
                if currentLevelFromFile == {WIDTH: 0, HEIGHT: 0}:
                    continue  # Ignore this level file line.
                # Finished with the current level:
                allLevels.append(currentLevelFromFile)
                currentLevelFromFile = {WIDTH: 0, HEIGHT: 0}
                y = 0  # Reset y back to 0.
                continue

            # Add the line to the current level.
            # We use line[:-1] so we don't include the newline:
            for x, levelChar in enumerate(line[:-1]):
                currentLevelFromFile[(x, y)] = levelChar
            y += 1

            if len(line) - 1 > currentLevelFromFile[WIDTH]:
                currentLevelFromFile[WIDTH] = len(line) - 1
            if y > currentLevelFromFile[HEIGHT]:
                currentLevelFromFile[HEIGHT] = y
    return allLevels


def displayLevel(levelNum, maxLevelNum, levelData):
    # Draw the current level.
    solvedCrates = 0
    unsolvedCrates = 0
    print('Level #' + str(levelNum + 1), 'of', maxLevelNum)
    for y in range(levelData[HEIGHT]):
        for x in range(levelData[WIDTH]):
            if levelData.get((x, y), EMPTY) == CRATE:
                unsolvedCrates += 1
            elif levelData.get((x, y), EMPTY) == CRATE_ON_GOAL:
                solvedCrates += 1
            prettyChar = CHAR_MAP[levelData.get((x, y), EMPTY)]
            print(prettyChar, end='')
        print()
    totalCrates = unsolvedCrates + solvedCrates
    print(solvedCrates, '/', totalCrates, 'solved.')


def askForPlayerMove(maxLevelNum):
    # Get the input from the player:
    while True:
        move = input('Enter move> ').upper()

        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if move.isdecimal():
            if not (1 <= int(move) < maxLevelNum):
                # There's no level for the number the player entered:
                print('Level numbers are between 1 and', maxLevelNum)
                continue
            return str(int(move) - 1)  # Return the new level number.

        # Check that the input is a valid WASD move or U for undo:
        if move in ('W', 'A', 'S', 'D', 'U'):
            return move

        print(move, 'is not valid. Enter one of W, A, S, D or QUIT.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
