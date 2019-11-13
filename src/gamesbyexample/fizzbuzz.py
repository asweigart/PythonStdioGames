# FizzBuzz Calculation, by Al Sweigart al@inventwithpython.com
# Calculates and prints the answers for a fizz buzz game. This is a common
# programming problem.

number = 1
while number < 100000:
    if number % 3 == 0 and number % 5 == 0:
        # The number is evenly divisible by 3 and 5, so print "FizzBuzz":
        print('FizzBuzz', end='') # Don't print a newline at the end.
    elif number % 3 == 0:
        # The number is evenly divisible by 3, so print "Fizz":
        print('Fizz', end='') # Don't print a newline at the end.
    elif number % 5 == 0:
        # The number is evenly divisible by 5, so print "Buzz":
        print('Buzz', end='') # Don't print a newline at the end.
    else:
        # The number isn't evenly divisible by 3 or 5, so print the number:
        print(number, end='') # Don't print a newline at the end.

    number += 1 # Move on to the next number.

    if number < 100000:
        print(', ', end='') # Print a separating comma.
    else:
        print() # Print a newline character.
