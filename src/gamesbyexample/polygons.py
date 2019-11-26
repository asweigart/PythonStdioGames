# Polygons, by Al Sweigart al@inventwithpython.com
# A turtle program to draw polygons. Every line is the same length.

import turtle

turtle.tracer(1, 0) # Make the turtle draw faster.

# Move the turtle to the starting position:
turtle.penup()
turtle.goto(-100, -300) # The starting position is x -100, y -300.
turtle.pendown()

# (!) Uncomment the following line, and changing 30 to another number:
#turtle.setheading(30)

# (!) Try changing this pensize to other sizes:
turtle.pensize(3)
# (!) Try changing this line to other colors:
turtle.pencolor('green')

for sides in range(3, 21): # Draw polygons with 3 to 21 sides.
    for i in range(sides): # Draw each of the sides for this polygon.
        turtle.forward(100)
        turtle.left(360 / sides)

        # Write out the number of sides for the shape:
        if i == int(sides / 2.0):
            turtle.write(str(sides))
