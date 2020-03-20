"""Fibonacci Sequence, by Al Sweigart al@inventwithpython.com

Calculates numbers in the Fibonacci sequence: 0 1 1 2 3 5 8 13...
Tags: short, math, algorithm"""
__version__ = 1

import sys


print('''Fibonacci Sequence, by Al Sweigart al@inventwithpython.com

The Fibonacci Sequence begins with 0 and 1, and the next number is the
sum of the last two numbers. The sequence continues forever:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765...
''')

while True:  # Main program loop.
    while True:  # Keep asking until the user enters valid input.
        print()
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5 or 50), or QUIT to quit:')
        response = input().upper()

        if response == 'QUIT':
            sys.exit()

        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # User entered valid input; break out of the loop.

        print('Please enter a number greater than 0, or QUIT.')
    print()

    # Handle the special cases if the user entered 1 or 2:
    if nth == 1:
        print('0')
        print()
        print('The 1st Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The 2nd Fibonacci number is 1.')
        continue

    # Display warning if the user entered a large number:
    if nth >= 10000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        print('Press Enter to begin...')
        input()

    # Calculate the Nth Fibonacci number:
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.

    # Display all the later numbers of the Fibonacci sequence:
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        # Display the next number in the sequence:
        print(nextNumber, end='')

        # Check if we've found the Nth number the user wants:
        if nth == fibNumbersCalculated:
            print()
            # Get the ordinal indicator ('st', 'nd', 'rd', or 'th')
            lastDigit = str(fibNumbersCalculated)[-1]
            if len(str(fibNumbersCalculated)) >= 2:
                secondToLastDigit = str(fibNumbersCalculated)[-2]
            else:
                secondToLastDigit = ''

            if secondToLastDigit + lastDigit == '11':
                ordInd = 'th'
            elif secondToLastDigit + lastDigit == '12':
                ordInd = 'th'
            elif secondToLastDigit + lastDigit == '13':
                ordInd = 'th'
            elif lastDigit == '1':
                ordInd = 'st'
            elif lastDigit == '2':
                ordInd = 'nd'
            elif lastDigit == '3':
                ordInd = 'rd'
            else:
                ordInd = 'th'

            print()
            print('The ', fibNumbersCalculated, ordInd, \
                  ' Fibonacci number is ', nextNumber, sep='')
            break

        # Print a comma in between the sequence numbers:
        print(', ', end='')

        # Shift the last two numbers:
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
