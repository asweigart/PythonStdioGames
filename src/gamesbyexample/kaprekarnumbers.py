"""Kaprekar Numbers, by Al Sweigart al@inventwithpython.com

Kaprekar Numbers are numbers whose square in that base can be split into
2 parts that add up to the original number. For example:

45^2 = 2025 -> 20 + 25 = 45

Tags: tiny, math
"""
__version__ = 0

print("""Kaprekar Numbers, by Al Sweigart al@inventwithpython.com

Kaprekar Numbers are numbers whose square in that base can be split into
2 parts that add up to the original number. For example:

45^2 = 2025 -> 20 + 25 = 45""")

print('What number do you wish to start searching from? (min. 4)')
while True:  # Keep looping until the user enters a number > 3.
    response = input('> ')
    if response.isdecimal() and int(response) > 3:
        break
    print('Please enter a number 4 or greater.')

number = int(response) - 1
print('Ctrl-C will stop the program.')
print('Press Enter to begin...')
input()
print('Calculating Kraprekar numbers...')

foundKraprekarNumbers = []

try:
    while True:  # Main program loop.
        number += 1
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
    pass