/*
niNety-nniinE BoOttels of Mlik On teh waLl
By Al Sweigart al@inventwithpython.com
Print the full lyrics to one of the longest songs ever! The song
gets sillier and with each verse. Press Ctrl-C to stop.
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// Set up the constants:
// (!) Try changing both of these to 0 to print all the lyrics at once.
const SPEED = 0.01;  // The pause in between printing letters.
const LINE_PAUSE = 1.5;  // The pause at the end of each line.


async function slowPrint(text, pauseAmount=0.1) {
    for (let i = 0; i < text.length; i++) {
        process.stdout.write(text[i]);
        await sleep(pauseAmount)  // Pause in between each character.
    }
    console.log()  // Print a newline.
}


function replaceAt(str, index, replacement) {
    return str.substr(0, index) + replacement + str.substr(index + replacement.length);
}


async function main() {
    console.log('niNety-nniinE BoOttels, by Al Sweigart al@inventwithpython.com');
    console.log();
    console.log('(Press Ctrl-C to quit.)');

    await sleep(2);

    let bottles = 99;  // This is the starting number of bottles.

    // This list holds the string used for the lyrics:
    let lines = [' bottles of milk on the wall,',
             ' bottles of milk,',
             'Take one down, pass it around,',
             ' bottles of milk on the wall!'];

    while (bottles > 0) {  // Keep looping and display the lyrics.
        await slowPrint(bottles.toString() + lines[0], SPEED)
        await sleep(LINE_PAUSE);
        await slowPrint(bottles.toString() + lines[1], SPEED)
        await sleep(LINE_PAUSE);
        await slowPrint(lines[2], SPEED)
        await sleep(LINE_PAUSE);
        bottles = bottles - 1 ; // Decrease the number of bottles by one.

        if (bottles > 0) {  // Print the last line of the current stanza.
            await slowPrint(bottles.toString() + lines[3], SPEED)
        } else {  // Print the last line of the entire song.
            await slowPrint('No more bottles of milk on the wall!', SPEED)
        }

        await sleep(LINE_PAUSE);
        console.log();  // Print a newline.

        // Choose a random line to make "sillier":
        let lineNum = Math.floor(Math.random() * 4);

        let line = lines[lineNum];
        let effect = Math.floor(Math.random() * 4);

        if (effect === 0) {  // Replace a character with a space.
            let charIndex = Math.floor(Math.random() * line.length);
            line = replaceAt(line, charIndex, ' ');
        } else if (effect === 1) {  // Change the casing of a character.
            let charIndex = Math.floor(Math.random() * line.length);
            if (line[charIndex].toUpperCase() == line[charIndex]) {
                line = replaceAt(line, charIndex, line[charIndex].toLowerCase());
            } else if (line[charIndex].toLowerCase() == line[charIndex]) {
                line = replaceAt(line, charIndex, line[charIndex].toUpperCase());
            }
        } else if (effect === 2) {  // Transpose two characters.
            let charIndex = Math.floor(Math.random() * (line.length - 1));
            let firstChar = line[charIndex]
            let secondChar = line[charIndex + 1]
            line = replaceAt(line, charIndex, secondChar);
            line = replaceAt(line, charIndex + 1, firstChar);
        } else if (effect === 3) {  // Double a character.
            let charIndex = Math.floor(Math.random() * (line.length - 1));
            line = line.substr(0, charIndex) + line[charIndex] + line.substr(charIndex);
        }

        lines[lineNum] = line;  // Update the strings in lines.
    }
}

main();
