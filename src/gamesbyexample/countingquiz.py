"""Counting Quiz, by Al Sweigart al@inventwithpython.com
Use multiplication and subtraction to count the number of stars shown
as fast as possible.

This and other games are available at https://nostarch.com/XX
Tags: short, math"""

import math, random, time

def main():
    print('''Counting Quiz, by Al Sweigart al@inventwithpython.com

    Use multiplication and subtraction to count the number of stars
    shown as fast as possible. For example:

      * * * * * *
      * * * * *
      *   * * * *

    This is a 6 x 3 star field with 2 missing stars.
    The answer is 6 x 3 - 2 = 16

    The quiz is 60 seconds long.
    ''')

    while True:
        input('Press Enter to begin...')
        runQuiz()
        print('Would you like to play again? Y/N')
        response = input('> ').upper()
        if not response.startswith('Y'):
            print('Thanks for playing!')
            break


def runQuiz():
    correct = 0
    startTime = time.time()
    while time.time() < startTime + 60:
        print('\n' * 60)  # Clear the screen by printing newlines.

        # Generate the problem and the star field to display:
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        starField = {}  # Keys are (x, y) tuples, values are '*' or ' '.

        # First, populate the entire field with stars:
        for x in range(width):
            for y in range(height):
                starField[(x, y)] = '*'

        # Next, remove some stars from the field:
        numMissing = random.randint(0, math.sqrt(width * height) // 2)
        for i in range(numMissing):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)

                # Make sure we don't remove a star that has already
                # been removed:
                if starField[(x, y)] == '*':
                    break
            starField[(x, y)] = ' '  # Set this star to an empty space.
        answer = width * height - numMissing

        # Display the star field:
        for y in range(height):
            for x in range(width):
                print(starField[(x, y)] + ' ', end='')
            print()  # Print a newline.

        # Let the player answer and determine if they're right or wrong.
        response = input('Enter the number of stars. > ')
        if response.isdecimal() and int(response) == answer:
            correct += 1
        else:
            print('No, answer is ', answer)
            time.sleep(1)

    print('Time\'s up!')
    print('You were able to count', correct, 'star fields correctly.')
    print()


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
