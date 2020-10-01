/*
Diamonds, by Al Sweigart al@inventwithpython.com
Draws diamonds of various sizes.
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
*/

function main() {
    console.log('Diamonds, by Al Sweigart al@inventwithpython.com');

    // Display diamonds of sizes 0 through 6:
    for (var diamondSize = 0; diamondSize < 6; diamondSize++) {
        displayOutlineDiamond(diamondSize);
        console.log();  // Print a newline.
        displayFilledDiamond(diamondSize);
        console.log();  // Print a newline.
    }
}


function displayOutlineDiamond(size) {
    // Display the top half of the diamond:
    for (var i = 0; i < size; i++) {
        process.stdout.write(' '.repeat(size - i - 1));  // Left side space.
        process.stdout.write('/');  // Left side of diamond.
        process.stdout.write(' '.repeat(i * 2));  // Interior of diamond.
        process.stdout.write('\\');  // Right side of diamond.
        console.log();
    }

    // Display the bottom half of the diamond:
    for (var i = 0; i < size; i++) {
        process.stdout.write(' '.repeat(i));  // Left side space.
        process.stdout.write('\\');  // Left side of diamond.
        process.stdout.write(' '.repeat((size - i - 1) * 2));  // Interior of diamond.
        process.stdout.write('/');  // Right side of diamond.
        console.log();
    }
}

function displayFilledDiamond(size) {
    // Display the top half of the diamond:
    for (var i = 0; i < size; i++) {
        process.stdout.write(' '.repeat(size - i - 1));  // Left side space.
        process.stdout.write('/'.repeat(i + 1));  // Left half of diamond.
        process.stdout.write('\\'.repeat(i + 1));  // Right half of diamond.
        console.log();
    }

    // Display the bottom half of the diamond:
    for (var i = 0; i < size; i++) {
        process.stdout.write(' '.repeat(i));  // Left side space.
        process.stdout.write('\\'.repeat(size - i));  // Left side of diamond.
        process.stdout.write('/'.repeat(size - i));  // Right side of diamond.
        console.log();
    }
}

main();