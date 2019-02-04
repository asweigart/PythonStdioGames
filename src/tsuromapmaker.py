# Tsuro Map Maker, by Al Sweigart al@inventwithpython.com

import random, sys
try:
    import pytextcanvas as pytc
except:
    sys.exit('PyTextCanvas is required to run this. Run `pip install pytextcanvas` from the shell to install it.')

if len(sys.argv) == 3:
    WIDTH = int(sys.argv[1])
    HEIGHT = int(sys.argv[2])
else:
    WIDTH = 80
    HEIGHT = 25

TILE_MAP = {
    '0': ' ',
    '1': chr(9472),  # ─
    '2': chr(9474),  # │
    '3': chr(9484),  # ┌
    '4': chr(9488),  # ┐
    '5': chr(9492),  # └
    '6': chr(9496),  # ┘
    '7': chr(9608),  # █
}

ROTATE_MAP = {
    '0': '0', # ' ' becomes ' '
    '1': '2', # ─ becomes │
    '2': '1', # │ becomes ─
    '3': '4', # ┌ becomes ┐
    '4': '6', # ┐ becomes ┘
    '5': '3', # └ becomes ┌
    '6': '5', # ┘ becomes └
    '7': '7', # █ becomes █
}

# The last digit is a checksum so that the sum of numbers mod 10 is 0.
# More details at https://github.com/asweigart/PythonStdioGames/blob/master/src/tsuromapmakerreference.txt
TILES = ['02360452115121411245036209', '05420145210202012451025408',
         '02020423115111411625020204', '02020454512054060051031406',
         '02020451212002060051031409', '02360122110220016231036204',
         '05160143110220012631020207', '36360636033603660363036360',
         '05420402232326262205025407', '02020420512200062031020204',
         '05420432633211662203515464', '05160400032000260005031408',
         '36020140512200062031020208', '05364112433112660251036366',
         '05160111110000011143031261', '02020160510000014031020200',
         '05454402052020011111545404', '32160620310202012111020202',
         '02020420512200012111521402', '02020423632514211625540208',
         '02020121113216065111031406', '32160620310202045121540208',
         '05160140310202045121540201', '02020423212521411625540204',
         '05420402515121414205025401', '05114111650000043111521403',
         '02360116310511443165521405', '02020111210202016051031405',
         '05124114323126263165025401', '36360216312316062031020201',
         '02020111210202012111020206', '02020420232202262025020208',
         '05420112633111663211025400', '05420145113116065111031404',
         '36020214232022260512031263']

# This code makes sure the above TILES were typed correctly.
for i, tile in enumerate(TILES):
    assert len(tile) == 26, 'Tile %s has an incorrect length.' % (i)
    assert (sum([int(x) for x in tile]) % 10) == 0, 'Tile %s is wrong.' % (i)
    TILES[i] = TILES[i][:25] # Cut off the checksum digit.


def drawTile(tile, x, y, board):
    for ix in range(x, x + 5):
        for iy in range(y, y + 5):
            board[ix, iy] = TILE_MAP[tile[ix-x + (5 * (iy-y))]]


def rotateTile(tile, rotations): # rotations are clockwise at 90 degree increments
    assert len(tile) == 25 # Tiles should be 5x5 areas of 25 '0' through '7' characters.
    assert tile.isdigit() and '8' not in tile and '9' not in tile

    rotations = rotations % 4 # Handle excess or negative rotations.
    t = tile # Syntactic sugar to use a shorter name.

    for ir in range(rotations):
        # Indexes of each position in the tile:
        #  0  1  2  3  4
        #  5  6  7  8  9
        # 10 11 12 13 14
        # 15 16 17 18 19
        # 20 21 22 23 24

        rt = [' '] * 25 # Rotated tile as a mutable list.

        # Create the new "rotated tile" by rotating clockwise 90 degrees:
        rt[0], rt[4], rt[24], rt[20] = t[20], t[0], t[4], t[24]
        rt[1], rt[9], rt[23], rt[15] = t[15], t[1], t[9], t[23]
        rt[2], rt[14], rt[22], rt[10] = t[10], t[2], t[14], t[22]
        rt[3], rt[19], rt[21], rt[5] = t[5], t[3], t[19], t[21]

        rt[6], rt[8], rt[18], rt[16] = t[16], t[6], t[8], t[18]
        rt[7], rt[13], rt[17], rt[11] = t[11], t[7], t[13], t[17]

        rt[12] = t[12] # Center position doesn't rotate positions.

        # Rotate the individual block characters:
        for i in range(25):
            rt[i] = ROTATE_MAP[rt[i]]

        t = ''.join(rt)

    assert len(t) == 25
    return t


# Create a canvas to draw the tiles on:
canvas = pytc.Canvas(WIDTH, HEIGHT)
for x in range(0, WIDTH, 5):
    for y in range(0, HEIGHT, 5):
        # Choose a random tile, rotate it a random number of times:
        tile = rotateTile(random.choice(TILES), random.randint(0, 3))
        drawTile(tile, x, y, canvas)

canvas.print()

# Copy the canvas to the clipboard if pyperclip is installed:
try:
    import pyperclip
    pyperclip.copy(str(canvas))
except:
    pass # Do nothing if pyperclip is not installed.
