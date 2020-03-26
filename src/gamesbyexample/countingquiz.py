"""Counting Quiz, by Al Sweigart al@inventwithpython.com

Use multiplication and subtraction to count the number of stars shown
as fast as possible.

Tags: short, math"""

import math, random, time

def main():
    print('''Counting Quiz, by Al Sweigart al@inventwithpython.com

    Use multiplication and subtraction to count the number of stars shown
    as fast as possible. The quiz is 60 seconds long. For example:

      * * * * * *
      * * * * *
      *   * * * *

    This is a 6 x 3 star field with 2 missing stars.
    The answer is 6 x 3 - 2 = 16
    ''')

    while True:
        input('Press Enter to begin...')
        runQuiz()
        print('Would you like to play again? Y/N')
        response = input().upper()
        if not response.startswith('Y'):
            print('Thanks for playing!')
            break


def runQuiz():
    correct = 0
    startTime = time.time()
    while time.time() < startTime + 60:
        print('\n' * 40)  # Clear the screen by printing several newlines.

        # Generate the problem and the star field to display:
        width = random.randint(1, 10)
        height = random.randint(1, 10)
        canvas = {}
        for x in range(width):
            for y in range(height):
                canvas[(x, y)] = '*'
        numMissing = random.randint(0, math.sqrt(width * height) // 2)
        for i in range(numMissing):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if canvas[(x, y)] == '*':
                    break
            canvas[(x, y)] = ' '
        answer = width * height - numMissing

        # Display the star field:
        for y in range(height):
            for x in range(width):
                print(canvas[(x, y)] + ' ', end='')
            print()  # Print a newline.

        # Let the player answer and determine if they're right or wrong.
        response = input('Enter the number of stars. > ')
        if response.isdecimal() and int(response) == answer:
            correct += 1
        else:
            print('Wrong:', answer)
            time.sleep(1)

    print('Time\'s up!')
    print('You were able to count', correct, 'star fields correctly.')
    print()


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
