# Ulam Spiral, by Al Sweigart al@inventwithpython.com
# The Ulam spiral is a mysterious mathematics pattern for prime numbers
# with turtle graphics.
# More info at https://en.wikipedia.org/wiki/Ulam_spiral

import turtle
import math

turtle.tracer(1000, 0) # Make the turtle draw faster.

SPACING = 3
DOT_SIZE = 4

turtle.bgcolor('#353337') # Use a dark background color.
turtle.pencolor('#CCCCCC') # The spiral is a light gray color.

def amountOfDivisors(number):
    # Return the number of divisors for `number`.
    total = 0
    for i in range(2, int(math.sqrt(number)) + 1):
        # If i evenly divides number with no remainder, increase total.
        if number % i == 0:
            total += 1
    return total

# (!) Comment this next line to draw the spiral.
turtle.penup()
turtle.forward(SPACING) # 1 is not prime, so skip
turtle.left(90)
turtle.dot(DOT_SIZE) # 2 is prime, so make a dot
turtle.forward(SPACING)
turtle.left(90)

currentNumber = 3 # This is the number we test for primality.
spiralSideLength = 3
while currentNumber < 40000:
    # We draw two sides before increasing the spiral side length:
    for i in range(2):
        for j in range(spiralSideLength):
            divs = amountOfDivisors(currentNumber)
            currentNumber += 1

            if divs == 0:
                # Mark the prime number
                turtle.dot(DOT_SIZE, '#76b7eb')
            turtle.forward(SPACING)
        turtle.left(90)
    spiralSideLength += 1

turtle.update() # Finish drawing the screen.
turtle.exitonclick() # When user clicks on the window, close it.
