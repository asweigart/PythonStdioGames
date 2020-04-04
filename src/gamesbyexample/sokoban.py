"""Sokoban Clone, by Al Sweigart al@inventwithpython.com
The classic crate-pushing game originally by Hiroyuki Imabayashi
More info at: https://en.wikipedia.org/wiki/Sokoban
This and other games are available at https://nostarch.com/XX
Tags: large, game, puzzle game"""
__version__ = 0
import copy, os, sys

# Set up the constants:
WALL = chr(9608)   # Character 9608 is '█'
FACE = chr(9786)   # Character 9786 is '☺'
CRATE = chr(9679)  # Character 9679 is '●'
GOAL = chr(9675)   # Character 9675 is '○'
CRATE_ON_GOAL = '*'
PLAYER_ON_GOAL = FACE
CHAR_MAP = {'#': WALL, '@': FACE, '$': CRATE, '+': PLAYER_ON_GOAL,
            '.': GOAL, '*': CRATE_ON_GOAL, ' ': ' '}


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
        displayLevel(currentLevelNumber, currentLevel, len(allLevels))

        # Get the input from the player:
        moves = input('Enter moves> ').upper()

        if moves == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if moves.isdecimal():
            if not (1 <= int(moves) < len(allLevels)):
                print('Level numbers are between 1 and', len(allLevels))
                continue
            # Change the current level:
            currentLevelNumber = int(moves) - 1
            currentLevel = copy.copy(allLevels[currentLevelNumber])
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
                    # Can't push the crate because there's a wall or crate
                    # behind it:
                    continue
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
                displayLevel(currentLevelNumber, currentLevel)
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
        currentLevelFromFile = {'width': 0, 'height': 0}
        y = 0
        for line in levelFile.readlines():
            if line.startswith(';'):
                continue  # Ignore comments in the level file.

            if line == '\n':
                if currentLevelFromFile == {'width': 0, 'height': 0}:
                    continue  # Ignore this level file line.
                # Finished with the current level:
                allLevels.append(currentLevelFromFile)
                currentLevelFromFile = {'width': 0, 'height': 0}
                y = 0  # Reset y back to 0.
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


def displayLevel(levelNum, maxLevelNum, levelData):
    # Draw the current level.
    print('Level #' + str(levelNum + 1), 'of', maxLevelNum)
    for y in range(levelData['height']):
        for x in range(levelData['width']):
            prettyChar = CHAR_MAP[levelData.get((x, y), ' ')]
            print(prettyChar, end='')
        print()


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
