/*
Magic Fortune Ball, by Al Sweigart al@inventwithpython.com
Ask a yes/no question about your future. Inspired by the Magic 8 Ball.
*/

'use strict';

const readlineSync = require('readline-sync');

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

async function slowSpacePrint(text, interval=0.1) {
    for (var i = 0; i < text.length; i++) {
        if (text[i] === 'I') {
            // I's are displayed in lowercase for style:
            process.stdout.write('i ');
        }
        else {
            // All other characters are displayed normally:
            process.stdout.write(text[i] + ' ');
        }
        await sleep(interval);
    }
    console.log('\n');  // Print two newlines at the end.
}


async function main() {
    // Prompt for a question:
    await slowSpacePrint('MAGIC FORTUNE BALL, BY AL SWEIGART');
    await sleep(0.5);
    await slowSpacePrint('ASK ME YOUR YES/NO QUESTION.');
    readlineSync.question('> ');

    // Display a brief reply:
    var replies = [
        'LET ME THINK ON THIS...',
        'AN INTERESTING QUESTION...',
        'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
        'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
        'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
        'YES... NO... MAYBE... I WILL THINK ON IT...',
        'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
        'I SHALL CONSULT MY VISIONS...',
        'YOU MAY WANT TO SIT DOWN FOR THIS...',
    ];
    await slowSpacePrint('.'.repeat(Math.floor(Math.random(8) + 4)), 0.7);

    // Dramatic pause:
    await slowSpacePrint('I HAVE AN ANSWER...', 0.2);
    await sleep(1);
    var answers = [
        'YES, FOR SURE',
        'MY ANSWER IS NO',
        'ASK ME LATER',
        'I AM PROGRAMMED TO SAY YES',
        'THE STARS SAY YES, BUT I SAY NO',
        'I DUNNO MAYBE',
        'FOCUS AND ASK ONCE MORE',
        'DOUBTFUL, VERY DOUBTFUL',
        'AFFIRMATIVE',
        'YES, THOUGH YOU MAY NOT LIKE IT',
        'NO, BUT YOU MAY WISH IT WAS SO',
    ]
    await slowSpacePrint(answers[Math.floor(Math.random() * answers.length)], 0.05);
}

await main();
