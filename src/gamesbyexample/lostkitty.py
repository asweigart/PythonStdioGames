"""Lost Kitty, by Al Sweigart al@inventwithpython.com
Try to find your lost kitten Zophie by moving around the neighborhood
streets and avenues. You'll get hints at how near or far she is.
This game that teaches cartesian coordinates, cardinal directions, and
the Pythagorean Theorem.
Tags: large, game"""
__version__ = 0
import math, random, sys

# Set up the constants:
UPDOWN    = chr(9474)  # Character 9474 is '│'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
CROSS     = chr(9532)  # Character 9532 is '┼'

WIDTH = 16  # The number of vertical avenues on the map.
HEIGHT = 8  # The number of horizontal streets on the map.

assert WIDTH < 100, 'The map is set too wide!'
assert HEIGHT < 10, 'The map is set too tall!'


def main():
    """Runs the game."""
    steps = 0  # Keep track of how many steps the player has moved.
    playerx = 4  # Current x position of the player.
    playery = 2  # Current y position of the player.
    # (x, y) tuples of intersections the player has already visited:
    visitedIntersections = set()

    print('LOST KITTY')
    print('By Al Sweigart al@inventwithpython.com')
    print()
    print('Zophie the kitten is lost in the city! Move around until')
    print('you find her!')
    input('Press Enter to begin...')

    # Get a random hidden position for the cat.
    while True:
        catx = random.randint(0, WIDTH - 1)
        caty = random.randint(0, HEIGHT - 1)

        # Keep looping until the cat is not near the player:
        if getDistance(playerx, playery, catx, caty) > 2:
            break

    while True:  # Main game loop.
        visitedIntersections.add((playerx, playery))

        displayMap(playerx, playery, visitedIntersections)
        displayClue(playerx, playery, catx, caty)
        print('Blocks travelled:', steps)
        playerx, playery = getPlayerMove(playerx, playery)
        steps += 1

        # Detect if the player has found the cat:
        if playerx == catx and playery == caty:
            displayMap(playerx, playery, visitedIntersections)
            print('You have found your lost kitty Zophie! Hooray!')
            print('You travelled', steps, 'blocks to find her!')
            print('Thanks for playing!')
            sys.exit()


def getDistance(x1, y1, x2, y2):
    """Returns the distance between (x1, y1) and (x2, y2) by using the
    Pythagorean Theorem."""
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def displayClue(playerx, playery, catx, caty):
    """Display a clue telling the player that the cat is very near,
    near, far, or very far away."""
    distance = getDistance(playerx, playery, catx, caty)
    if distance <= 2.0:
        print('You hear a meow very nearby.')
    elif distance <= 4.0:
        print('You hear a meow nearby.')
    elif distance <= 6.0:
        print('You hear a meow far away.')
    else:
        print('You hear a meow very far away.')


def getOrdIndicator(number):
    """Returns the "ordinal indicator" of number, e.g. 'st' for 1 and
    'rd' for 23, because we write them as "1st" and "23rd"."""
    lastDigit = str(number)[-1]

    if len(str(number)) >= 2:
        secondToLastDigit = str(number)[-2]
    else:
        secondToLastDigit = ''

    if secondToLastDigit + lastDigit == '11':
        return 'th'
    elif secondToLastDigit + lastDigit == '12':
        return 'th'
    elif secondToLastDigit + lastDigit == '13':
        return 'th'
    elif lastDigit == '1':
        return 'st'
    elif lastDigit == '2':
        return 'nd'
    elif lastDigit == '3':
        return 'rd'
    else:
        return 'th'


def displayMap(playerx, playery, visitedIntersections):
    """Display the map, with visited intersections and the player's
    current position."""
    # Print the avenue names at the top:
    print('      ', end='')
    for x in range(WIDTH):
        print(x, getOrdIndicator(x), sep='', end='')
        if x < 10:
            # Single-digit names need an extra space at the end:
            print(' ', end='')
    print()  # Print a newline.

    print('      ', end='')
    for x in range(WIDTH):
        print('Ave ', end='')
    print()  # Print a newline.

    # Print the lines for all the roads:
    for y in range(HEIGHT - 1, -1, -1):
        # Print the street names on the left edge:
        print(y, getOrdIndicator(y), ' St ', sep='', end='')
        for x in range(WIDTH):
            if x == playerx and y == playery:
                print('X', end='')  # Print the player location.
            elif (x, y) in visitedIntersections:
                print('O', end='')  # Print a visited intersection.
            else:
                print(CROSS, end='')  # Print an unvisited intersection.

            # Print the horizontal street segment:
            if x < WIDTH - 1:
                print(LEFTRIGHT * 3, end='')

        # Print the compass rose in the lower right corner:
        if y == 1:
            print('   N')
        elif y == 0:
            print('   S')
        else:
            print()  # Just print a newline.

        # Print the vertical avenue segment.
        if y > 0:
            for x in range(WIDTH - 1):
                if x == 0:
                    print('       ', end='')  # Print indentation.
                print(UPDOWN + '   ', end='')  # Print an avenue segment.
            print(UPDOWN, end='')  # Print the rightmost avenue segment.

        # Print the compass rose in the lower right corner:
        if y == 1:
            print(' W' + LEFTRIGHT + CROSS + LEFTRIGHT + 'E')
        elif y != 0:
            print()  # Just print a newline.


def getPlayerMove(playerx, playery):
    """Let the player enter which direction they want to move, or if
    they want to quit. Make sure the player can't move off the edge of
    the map."""
    while True:
        print('Enter your move: north south east west or QUIT')
        response = input('> ').lower()
        if response == 'quit':
            print('Thanks for playing!')
            sys.exit()
        elif response.startswith('n') and playery != HEIGHT - 1:
            return (playerx, playery + 1)
        elif response.startswith('s') and playery != 0:
            return (playerx, playery - 1)
        elif response.startswith('w') and playerx != 0:
            return (playerx - 1, playery)
        elif response.startswith('e') and playerx != WIDTH - 1:
            return (playerx + 1, playery)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
