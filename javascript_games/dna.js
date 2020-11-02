/*
DNA, by Al Sweigart al@inventwithpython.com
A simple animation of a DNA double-helix. Press Ctrl-C to stop.
Inspired by matoken https://asciinema.org/a/155441
This and other games are available at https://nostarch.com/XX
Tags: short, artistic, scrolling, science
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

const PAUSE = 0.15  // (!) Try changing this to 0.5 or 0.0.

// These are the individual rows of the DNA animation:
const ROWS = [
    //123456789 <- Use this to measure the number of spaces:
     '         ##',  // Index 0 has no {}.
     '        #{a}-{b}#',
     '       #{a}---{b}#',
     '      #{a}-----{b}#',
     '     #{a}------{b}#',
     '    #{a}------{b}#',
     '    #{a}-----{b}#',
     '     #{a}---{b}#',
     '     #{a}-{b}#',
     '      ##',  // Index 9 has no {}.
     '     #{a}-{b}#',
     '     #{a}---{b}#',
     '    #{a}-----{b}#',
     '    #{a}------{b}#',
     '     #{a}------{b}#',
     '      #{a}-----{b}#',
     '       #{a}---{b}#',
     '        #{a}-{b}#'];
    //123456789 <- Use this to measure the number of spaces:

async function main() {
    console.log('DNA Animation, by Al Sweigart al@inventwithpython.com');
    console.log('Press Ctrl-C to quit...');
    await sleep(2);
    let rowIndex = 0;

    while (true) { // Main program loop.
        // Increment rowIndex to draw next row:
        rowIndex = rowIndex + 1;
        if (rowIndex == ROWS.length) {
            rowIndex = 0;
        }

        // Row indexes 0 and 9 don't have nucleotides:
        if (rowIndex == 0 || rowIndex == 9) {
            console.log(ROWS[rowIndex]);
            continue;
        }

        // Select random nucleotide pairs, guanine-cytosine and
        // adenine-thymine:
        let randomSelection = Math.floor(Math.random() * 4) + 1;
        let leftNucleotide, rightNucleotide;
        if (randomSelection == 1) {
            leftNucleotide = 'A', rightNucleotide = 'T';
        } else if (randomSelection == 2) {
            leftNucleotide = 'T', rightNucleotide = 'A';
        } else if (randomSelection == 3) {
            leftNucleotide = 'C', rightNucleotide = 'G';
        } else if (randomSelection == 4) {
            leftNucleotide = 'G', rightNucleotide = 'C';
        }

        // Print the row.
        console.log(ROWS[rowIndex].replace('{a}', leftNucleotide).replace('{b}', rightNucleotide));
        await sleep(PAUSE)  // Add a slight pause.
    }
}

main();
