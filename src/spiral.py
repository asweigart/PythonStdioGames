# Spiral, by Al Sweigart al@inventwithpython.com
# A simple program that draws a square spiral.

size = 22  # Change the size to any positive integer you want.
MARK = 'O' # Change the mark character to any character you want.


assert len(MARK) == 1
canvas = {'width': size, 'height': size}
x = 0
y = 0

# Draw the first line going right:
canvas[(0, 0)] = MARK
for i in range(size - 1):
    x += 1
    canvas[(x, y)] = MARK
size -= 1

while True:
    # Draw a line going down:
    for i in range(size):
        y += 1
        canvas[(x, y)] = MARK

    # Draw a line going left:
    for i in range(size):
        x -= 1
        canvas[(x, y)] = MARK

    size -= 2
    if size < 2:
        break

    # Draw a line going up:
    for i in range(size):
        y -= 1
        canvas[(x, y)] = MARK

    # Draw a line going right:
    for i in range(size):
        x += 1
        canvas[(x, y)] = MARK

    size -= 2
    if size < 2:
        break

# Open the file to output the spiral:
spiralFile = open('spiral.txt', 'w')

# Draw the canvas:
for iy in range(canvas['height']):
    for ix in range(canvas['width']):
        print(canvas.get((ix, iy), ' '), end='')
        spiralFile.write(canvas.get((ix, iy), ' '))
    print()
    spiralFile.write('\n')
spiralFile.close()
print('Spiral written to sprial.txt.')