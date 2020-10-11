/*
Shining Carpet, by Al Sweigart al@inventwithpython.com
Displays a tessellation of the carpet pattern from The Shining.
*/

'use strict';

// Set up the constants:
const X_REPEAT = 6;  // How many times to tessellate horizontally.
const Y_REPEAT = 4;  // How many times to tessellate vertically.

for (let y = 0; y < Y_REPEAT; y++) {
    console.log('_ \\ \\ \\_/ __'.repeat(X_REPEAT));
    console.log(' \\ \\ \\___/ _'.repeat(X_REPEAT));
    console.log('\\ \\ \\_____/ '.repeat(X_REPEAT));
    console.log('/ / / ___ \\_'.repeat(X_REPEAT));
    console.log('_/ / / _ \\__'.repeat(X_REPEAT));
    console.log('__/ / / \\___'.repeat(X_REPEAT));
}
