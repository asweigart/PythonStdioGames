"""Sokoban Clone, by Al Sweigart al@inventwithpython.com
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
FACE_DISPLAY = chr(9786)   # Character 9786 is '☺'
CRATE_DISPLAY = chr(9632)  # Character 9679 is '■'
GOAL_DISPLAY = chr(9633)   # Character 9633 is '□'
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

You can enter multiple WASD or U letters to make several moves at once.
''')

    allLevels = loadLevels('sokobanlevels.txt')
    currentLevelNumber = 0
    currentLevel = copy.copy(allLevels[currentLevelNumber])
    undoStack = [copy.copy(currentLevel)]

    while True:  # Main game loop.
        displayLevel(currentLevelNumber, len(allLevels), currentLevel)

        moves = getPlayerMoves(len(allLevels))

        if len(moves) == 0:
            continue  # Player entered no moves.
        elif moves[0].isdecimal():
            currentLevelNumber = int(moves[0]) # Set new level number.
            # Refresh the level data and undo stack:
            currentLevel = copy.copy(allLevels[currentLevelNumber])
            undoStack = [copy.copy(currentLevel)]
            continue

        # Carry out the moves:
        for move in moves:
            # Find the player position:
            for position, character in currentLevel.items():
                if character in (FACE, PLAYER_ON_GOAL):
                    playerx, playery = position

            if move == 'U':
                if len(undoStack) == 1:
                    continue  # Can't undo past the first move.
                undoStack.pop()  # Remove the last item from undoStack.
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

            moveToSpace = currentLevel.get((playerx + movex, playery + movey), EMPTY)

            # If the move-to space is empty or a goal, just move there:
            if moveToSpace in (EMPTY, GOAL):
                # Change the player's old position:
                if currentLevel[(playerx, playery)] == FACE:
                    currentLevel[(playerx, playery)] = EMPTY
                elif currentLevel[(playerx, playery)] == PLAYER_ON_GOAL:
                    currentLevel[(playerx, playery)] = GOAL

                # Set the player's new position:
                if moveToSpace == EMPTY:
                    currentLevel[(playerx + movex, playery + movey)] = FACE
                elif moveToSpace == GOAL:
                    currentLevel[(playerx + movex, playery + movey)] = PLAYER_ON_GOAL

            # If the move-to space is a wall, don't move at all:
            elif moveToSpace == WALL:
                pass

            # If the move-to space is a crate, determine if we can push it:
            elif moveToSpace in (CRATE, CRATE_ON_GOAL):
                spaceAfterMoveToSpace = currentLevel.get((playerx + (movex * 2), playery + (movey * 2)), EMPTY)
                if spaceAfterMoveToSpace in (WALL, CRATE, CRATE_ON_GOAL):
                    # Can't push the crate because there's a wall or crate
                    # behind it:
                    continue
                if spaceAfterMoveToSpace in (GOAL, EMPTY):
                    # Change the player's old position:
                    if currentLevel[(playerx, playery)] == FACE:
                        currentLevel[(playerx, playery)] = EMPTY
                    elif currentLevel[(playerx, playery)] == PLAYER_ON_GOAL:
                        currentLevel[(playerx, playery)] = GOAL

                    # Set the player's new position:
                    if moveToSpace == CRATE:
                        currentLevel[(playerx + movex, playery + movey)] = FACE
                    elif moveToSpace == CRATE_ON_GOAL:
                        currentLevel[(playerx + movex, playery + movey)] = PLAYER_ON_GOAL

                    # Set the crate's new position:
                    if spaceAfterMoveToSpace == EMPTY:
                        currentLevel[(playerx + (movex * 2), playery + (movey * 2))] = CRATE
                    elif spaceAfterMoveToSpace == GOAL:
                        currentLevel[(playerx + (movex * 2), playery + (movey * 2))] = CRATE_ON_GOAL

            # Save the state of the level for the undo feature:
            undoStack.append(copy.copy(currentLevel))

            # Check if the player has finished the level:
            levelIsSolved = True
            for position, character in currentLevel.items():
                if character == CRATE:
                    levelIsSolved = False
                    break
            if levelIsSolved:
                displayLevel(currentLevelNumber, len(allLevels), currentLevel)
                print('Level complete!')
                input('Press Enter to continue...')
                currentLevelNumber = (currentLevelNumber + 1) % len(allLevels)
                currentLevel = copy.copy(allLevels[currentLevelNumber])
                undoStack = [copy.copy(currentLevel)]
                break  # Don't carry out any remaining moves.


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


def getPlayerMoves(maxLevelNum):
    # Get the input from the player:
    moves = input('Enter move(s)> ').upper()

    if moves == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    if moves.isdecimal():
        if not (1 <= int(moves) < maxLevelNum):
            print('Level numbers are between 1 and', maxLevelNum)
            return []  # Player entered no valid move.
        return [str(int(moves) - 1)]  # Return the new level number.

    # Validate the input; make sure it only has W, A, S, D, or U:
    movesAreValid = True
    for move in moves:
        if move not in ('W', 'A', 'S', 'D', 'U'):
            movesAreValid = False
            print(move, 'is not a valid move.')
            break
    if not movesAreValid:
        return []  # Player entered no valid move.

    return moves

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
