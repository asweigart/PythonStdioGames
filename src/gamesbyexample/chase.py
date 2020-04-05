"""Chase, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
This and other games are available at https://nostarch.com/XX
Tags: large, game"""
__version__ = 0
import os, random, sys

# Set up the constants:
WIDTH = 40           # (!) Try changing this number.
HEIGHT = 20          # (!) Try changing this number.
NUM_ROBOTS = 10      # (!) Try changing this number.
NUM_TELEPORTS = 2    # (!) Try changing this number.
NUM_DEAD_ROBOTS = 2  # (!) Try changing this number.
NUM_WALLS = 100      # (!) Try changing this number.

WALL = chr(9617)  # Character 9617 is '░'
EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'


def main():
    print('''Chase, by Al Sweigart al@inventwithpython.com

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly towards you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a random teleporter, but it only has
enough battery for {} teleports. Keep in mind, you and robots can slip
through corners!
'''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # Set up a new game:
    board = getNewBoard(WIDTH, HEIGHT, NUM_WALLS, NUM_DEAD_ROBOTS)
    robots = getRobots(board, NUM_ROBOTS)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:  # Main game loop.
        drawBoard(board, robots, playerPosition)

        if len(robots) == 0:  # Check if the player has won.
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # Move the player and robots:
        playerPosition = getPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots:  # Check if the player has lost.
            if (x, y) == playerPosition:
                drawBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def clearScreen():
    # Clear the previously drawn text:
    if sys.platform == 'win32':
        # Clear the Windows terminal with the cls command:
        os.system('cls')
    else:
        # Clear macOS/Linux terminals with the clear command:
        os.system('clear')


def getNewBoard(width, height, numWalls, numDeadRobots):
    board = {'width': width, 'height': height,
             'teleports': NUM_TELEPORTS}

    # Create an empty board:
    for x in range(width):
        for y in range(height):
            board[(x, y)] = EMPTY_SPACE

    # Add border walls.
    for x in range(width):
        board[(x, 0)] = WALL  # Make top wall.
        board[(x, height - 1)] = WALL  # Make bottom wall.
    for y in range(height):
        board[(0, y)] = WALL  # Make left wall.
        board[(width - 1, y)] = WALL  # Make right wall.

    # Add random walls:
    for i in range(numWalls):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # Add starting dead robots:
    for i in range(numDeadRobots):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    while True:
        randomX = random.randint(1, board['width'] - 2)
        randomY = random.randint(1, board['height'] - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def getRobots(board, numRobots):
    # Add robots randomly:
    robots = []
    for i in range(numRobots):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


def drawBoard(board, robots, playerPosition):
    clearScreen()
    # Loop over every space on the board:
    for y in range(board['height']):
        for x in range(board['width']):
            # Draw the appropriate character:
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            elif (x, y) == playerPosition:
                print(PLAYER, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()  # Print a newline.


def moveRobots(board, robotPositions, playerPosition):
    playerx, playery = playerPosition
    nextRobotPositions = []

    while len(robotPositions) > 0:
        robotx, roboty = robotPositions[0]

        # Determine the direction the robot moves.
        if robotx < playerx:
            movex = 1  # Move right.
        elif robotx > playerx:
            movex = -1  # Move left.
        elif robotx == playerx:
            movex = 0  # Don't move horizontally.

        if roboty < playery:
            movey = 1  # Move up.
        elif roboty > playery:
            movey = -1  # Move down.
        elif roboty == playery:
            movey = 0  # Don't move vertically.

        # Check if the robot would run into a wall, and adjust course:
        if board[(robotx + movex, roboty + movey)] == WALL:
            # Robot would run into a wall, so come up with a new move:
            if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                movey = 0  # Robot can't move horizontally.
            elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                movex = 0  # Robot can't move vertically.
            else:
                # Robot can't move.
                movex = 0
                movey = 0
        newRobotx = robotx + movex
        newRoboty = roboty + movey

        if (board[(robotx, roboty)] == DEAD_ROBOT
            or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
            # Robot is at a crash site, remove it.
            del robotPositions[0]
            continue

        # Check if it moves into a robot, then destroy both robots:
        if (newRobotx, newRoboty) in nextRobotPositions:
            board[(newRobotx, newRoboty)] = DEAD_ROBOT
            nextRobotPositions.remove((newRobotx, newRoboty))
        else:
            nextRobotPositions.append((newRobotx, newRoboty))

        # Remove robots from robotPositions as they move.
        del robotPositions[0]
    return nextRobotPositions


def getPlayerMove(board, robots, playerPosition):
    playerX, playerY = playerPosition

    # Find which directions aren't blocked by a wall:
    q = 'Q' if isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
    w = 'W' if isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
    e = 'E' if isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
    d = 'D' if isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
    c = 'C' if isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
    x = 'X' if isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
    z = 'Z' if isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
    a = 'A' if isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
    allMoves = (q + w + e + d + c + x + a + z + 'S').replace(' ', '')

    while True:
        # Get player's move:
        print('(T)eleports remaining: {}'.format(board["teleports"]))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            # Teleport the player to a random empty space:
            board['teleports'] -= 1
            return getRandomEmptySpace(board, robots)
        elif move in allMoves:
            # Return the new player position based on their move:
            return {'Q': (playerX - 1, playerY - 1),
                    'W': (playerX + 0, playerY - 1),
                    'E': (playerX + 1, playerY - 1),
                    'D': (playerX + 1, playerY + 0),
                    'C': (playerX + 1, playerY + 1),
                    'X': (playerX + 0, playerY + 1),
                    'Z': (playerX - 1, playerY + 1),
                    'A': (playerX - 1, playerY + 0),
                    'S': (playerX, playerY)}[move]


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
