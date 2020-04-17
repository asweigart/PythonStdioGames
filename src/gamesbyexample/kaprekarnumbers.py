"""Kaprekar Numbers, by Al Sweigart al@inventwithpython.com
Kaprekar Numbers are numbers whose square in that base can be split into
2 parts that add up to the original number. For example:
45^2 = 2025 -> 20 + 25 = 45
More info at: https://en.wikipedia.org/wiki/Kaprekar_number
This and other games are available at https://nostarch.com/XX
Tags: tiny, math, scrolling"""
__version__ = 0
import sys

print("""Kaprekar Numbers, by Al Sweigart al@inventwithpython.com

Kaprekar Numbers are numbers whose square can be split into
2 parts that add up to the original number. For example:

45^2 = 2025 -> 20 + 25 = 45""")

print('What number do you wish to start searching from?')
while True:  # Keep looping until the user enters a number.
    response = input('> ')
    if response.isdecimal():
        if int(response) < 4:
            # The minimum is 4, because 3 * 3 is 9, and 9 does not have
            # at least two digits. However, 4 * 4 is 16, which does:
            response = 4
        break
    print('Please enter a number 4 or greater.')

# Subtract one because the first thing the main program loop does is
# increment the number:
number = int(response) - 1
print('The program will run until you press Ctrl-C.')
input('Press Enter to begin...')

foundKraprekarNumbers = []

try:
    while True:  # Main program loop.
        number += 1  # Go to the next number.
        square = str(number * number)

        # Split the square into two parts:
        firstPart  = square[0:len(square) // 2]
        secondPart = square[len(square) // 2:]

        # Check if their sum is the original number:
        if int(firstPart) + int(secondPart) == number:
            foundKraprekarNumbers.append(number)
            print(str(number) + '^2 =', square, '->', firstPart, '+', secondPart, '=', str(number))
            continue

        if len(square) % 2 == 0:
            continue

        # Split the square into two parts:
        firstPart  = square[0:len(square) // 2 + 1]
        secondPart = square[len(square) // 2 + 1:]

        # Check if their sum is the original number:
        if int(firstPart) + int(secondPart) == number:
            foundKraprekarNumbers.append(number)
            print(str(number) + '^2 =', square, '->', firstPart, '+', secondPart, '=', str(number))
            continue
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.