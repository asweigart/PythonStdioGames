"""FizzBuzz Game, by Al Sweigart al@inventwithpython.com
A number game where you also race against the clock.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, game, math"""
__version__ = 0
import sys, time

print('''Fizz Buzz Game, by Al Sweigart al@inventwithpython.com

Starting with 1, enter increasing numbers.
However, if the number is a multiple of 3, type "fizz" instead of
the number. If the number is a multiple of 5, type "buzz". If the
the number of is a multiple of 3 and 5, type "fizzbuzz".

So the pattern is:
1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16...

A doom clock is counting down. Entering correct responses gives you
more time. How long can you keep entering the correct pattern?''')
input('Press Enter to begin...')

number = 1
doomClock = time.time() + 10  # Player starts with 10 seconds.

while True:  # Main game loop.
    # Determine the correct response for the current number:
    if number % 3 == 0 and number % 5 == 0:
        correctResponse = 'fizzbuzz'
    elif number % 3 == 0:
        correctResponse = 'fizz'
    elif number % 5 == 0:
        correctResponse = 'buzz'
    else:
        correctResponse = str(number)

    # For the first 16 responses, give them the answer:
    if number <= 16:
        hint = '(Enter ' + correctResponse + ') '
    elif number == 17:
        hint = '(You are on your own now!) '
    else:
        hint = ''

    # Get the player's response:
    response = input('Next response: ' + hint)
    response = response.lower().replace(' ', '')

    # See if the player has lost:
    if response != correctResponse:
        print('NOOOOO! Correct response: ' + correctResponse)
        print('Thanks for playing!')
        sys.exit()
    elif time.time() > doomClock:
        print('NOOOOO! You have run out of time!')
        print('Thanks for playing!')
        sys.exit()

    # If the player was right, add 2 seconds to the doom clock.
    doomClock += 2
    secondsRemaining = round(doomClock - time.time(), 1)
    print('DOOM CLOCK: ' + str(secondsRemaining) + ' seconds remaining')
    print()
    number += 1  # Proceed to the next number to enter.
