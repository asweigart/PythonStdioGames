# Mona Lisa, by Al Sweigart al@inventwithpython.com
# Draws an Andy Warhol-like drawing of the Mona Lisa with turtle
# graphics.

import turtle
turtle.tracer(400, 0) # Make the turtle draw faster.

"""The image data for the Mona Lisa. I created this through a complicated
process: I found a picture of the Mona Lisa online, converted it to
grayscale in Photoshop, then greatly increased the contrast, then shrunk
it down, and converted that image into a pure black/white image. I wrote
a script using the Pillow module to turn the black/white pixel
information in to a stream of 1s and 0s, and then turned that binary
number into this hexadecimal number."""
monaLisaData = '0x54a9554ebaaab5555b776eeb56addebdb5db5b33fd9b6d5d6db55affcaeed576d559dd71576ab7a9a76ee32ceb59b556edd591df6b5aead5b265add256954aa52ad5aa55aa96ab55fd576d569d2b556affea992a955b4aa94effd4dd555496aa57f7feb45554a51534b9dfecb2aa36caa4a627ff14a49c254922d12ffd69345b54552c037f88a951423249a89ffe6905494892bc44bfda6689e74925a22bfd7125432a927800bff9d24bdeac83b5edfef6935fb7757fbbfff6d10adddd4ba9b5ffff4d5eeef37a913ff55255fabaff86aaffff92aafffd59103feafaadfb6fffc99fffe8ab5bff5ffc947ffffbdffd6f7f571ffffeeb6f7bfefe3d57eeffffffff77d9afbf7f5b7bbd7ffe5b7fff7efbff7fbff29fffafbffeffdebf97ffffdfedff6ffffdffffded7feffdd6fffffff7fd5fdb76ffedefffffffffffb7ff77fbb7dbbfef5b7feb57fdd6ddbf5efbdeb5bfffd6feeffdffe9afffdedefbb7fff8227fefafbfdfbefe5116bfcbbb7eeffde048fffe4dddfbbffca027ffbb6ff75f7fa090bf7fdd7bbabdfc0096fbee33ffdf7e2484ffbfbd1ddebff000170dffbef7fcfca910affffe9fb5ffe00897bffffdbdc7ff90017fffffefabffee805ffffeafefefefb757beefffb76ebf7fbfffffbffbf76ffbeedbfffffdffdbdffff7ffffffffffffffbbeff6bfefb76ffffdffffff7fbffb3fbfffffffbbfefd59efffdbefeffffbeafffffffffffffff7f7fefffffffffeedfbeffedfbffffffffeffffffbffeffffff7efdf7ffffffffff7fffefffffffffdfffeffffffbefffffbfbffdffffffff7bffff7ffffffffbfffffffbdfffbbdfffffffbdffebbffffffffffffff7efffffffffffff7feff5ffffff7f7ffbf76f05ffdffdfffff7bf892bffffffdfffffbe4a5fffffffefffffd50affffffffffffdf6a43fffffffffffffbb51f7fdfbfffffffd4baad57ffdfbfffd6b4f7ffffffffffff3ae7affffffffbff5be73f77effffeff7e8bbdffffffddffff5bfcefbf7ffffff7fd8def7fffefffffffeffffbfffffffffffb7fffffffffffffffefb77fffffffffffffffffffffffbffffffbfffffffffffffffffffffffffffffff7fffffffffffffffffffffff7ffffffffffffffffffffffff7ff7ffdfffffffeffffffffffffffffffffffff7fffffffffffffffffffffffffff'

def drawFromData(image_data, image_width, image_height, left, top, pixel_size):
    turtle.penup()

    inBinary = bin(int(image_data, 16))

    # Remove '0b' from the start of the hex number:
    inBinary = inBinary[2:]

    # Add leading zeros to the binary number, if needed:
    inBinary = inBinary.rjust(image_width * image_height, '0')

    for y in range(image_height):
        for x in range(image_width):
            turtle.goto(left + (x * pixel_size), top - (y * pixel_size))

            if inBinary[y * image_width + x] == '1': # (!) Try switching this to '0'.
                turtle.begin_fill()
                turtle.setheading(0)
                turtle.forward(pixel_size) # draw top of the box
                turtle.right(90)
                turtle.forward(pixel_size) # draw right edge of the box
                turtle.right(90)
                turtle.forward(pixel_size) # draw bottom of the box
                turtle.right(90)
                turtle.forward(pixel_size) # draw left edge of the box
                turtle.end_fill()          # fill in the box

turtle.bgcolor('#FFF7D0')
turtle.fillcolor('#FF0C6B')
drawFromData(monaLisaData, 68, 100, -272, 400, 4)
turtle.fillcolor('#CE18FF')
drawFromData(monaLisaData, 68, 100, 0, 400, 4)
turtle.fillcolor('#7C0BE8')
drawFromData(monaLisaData, 68, 100, -272, 0, 4)
turtle.fillcolor('#460CFF')
drawFromData(monaLisaData, 68, 100, 0, 0, 4)

turtle.update() # Finish drawing the screen.
turtle.exitonclick() # When user clicks on the window, close it.
