"""Fizz Buzz Calculation, by Al Sweigart al@inventwithpython.com
Fizz Buzz is a game where you count up from 1, substituting "fizz" for
multiples of 3, "buzz" for multiples of 5, and "fizzbuzz" for multiples
of 3 and 5.
More info at: https://en.wikipedia.org/wiki/Fizz_buzz
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, math"""
__version__ = 0
print('''Fizz Buzz Calculation, by Al Sweigart al@inventwithpython.com
Fizz Buzz is a game where you count up from 1, substituting "fizz" for
multiples of 3, "buzz" for multiples of 5, and "fizzbuzz" for multiples
of 3 and 5.

This program plays fizz buzz for the first one million numbers.
''')
input('Press Enter to begin...')

number = 1
while number < 1000000:  # Main program loop.
    if number % 3 == 0 and number % 5 == 0:
        # The number is evenly divisible by 3 and 5, so print "FizzBuzz":
        print('FizzBuzz', end=' ')  # Don't print a newline at the end.
    elif number % 3 == 0:
        # The number is evenly divisible by 3, so print "Fizz":
        print('Fizz', end=' ')  # Don't print a newline at the end.
    elif number % 5 == 0:
        # The number is evenly divisible by 5, so print "Buzz":
        print('Buzz', end=' ')  # Don't print a newline at the end.
    else:
        # The number isn't evenly divisible by 3 or 5, so print it:
        print(number, end=' ')  # Don't print a newline at the end.

    number += 1  # Move on to the next number.

print()  # Print a newline character at the end.
