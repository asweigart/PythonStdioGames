/*
Hex Grid, by Al Sweigart al@inventwithpython.com
Displays a simple tessellation of a hexagon grid.
*/

'use strict';

// Set up the constants:
// (!) Try changing these values to other numbers:
const X_REPEAT = 19;  // How many times to tessellate horizontally.
const Y_REPEAT = 12;  // How many times to tessellate vertically.

for (var y = 0; y < Y_REPEAT; y++) {
    // Display the top half of the hexagon:
    for (var x = 0; x < X_REPEAT; x++) {
        process.stdout.write('/ \\_');
    }
    process.stdout.write('\n');

    // Display the bottom half of the hexagon:
    for (var x = 0; x < X_REPEAT; x++) {
        process.stdout.write('\\_/ ');
    }
    process.stdout.write('\n');
}
