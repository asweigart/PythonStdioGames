// TODO fix this, something is wrong with the class.

/*
Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.

>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^

This and other games are available at https://nostarch.com/XX
Tags: large, artistic, object-oriented, scrolling
*/

'use strict';

function sleep(seconds) {
  return new Promise(resolve => setTimeout(resolve, seconds * 1000));
}

// Set up the constants:
const PAUSE = 0.2;  // (!) Try changing this to 1.0 or 0.0.
const DENSITY = 0.10;  // (!) Try changing this to anything from 0.0 to 1.0.

const DUCKLING_WIDTH = 5;
const LEFT = 'left';
const RIGHT = 'right';
const BEADY = 'beady';
const WIDE = 'wide';
const HAPPY = 'happy';
const ALOOF = 'aloof';
const CHUBBY = 'chubby';
const VERY_CHUBBY = 'very chubby';
const OPEN = 'open';
const CLOSED = 'closed';
const OUT = 'out';
const DOWN = 'down';
const UP = 'up';
const HEAD = 'head';
const BODY = 'body';
const FEET = 'feet';

// Get the size of the terminal window:
// We can't print to the last column on Windows without it adding a
// newline automatically, so reduce the width by one:
const WIDTH = process.stdout.columns - 1;

async function main() {
    console.log('Duckling Screensaver, by Al Sweigart');
    console.log('Press Ctrl-C to quit...');
    await sleep(2);

    let ducklingLanes = [];
    for (let i = 0; i < Math.floor(WIDTH / DUCKLING_WIDTH); i++) {
        ducklingLanes.push(null);
    }

    while (true) {  // Main program loop.
        for (let laneNum = 0; laneNum < ducklingLanes.length; laneNum++) {
            let ducklingObj = ducklingLanes[laneNum];

            // See if we should create a duckling in this lane:
            if (ducklingObj === null && Math.random() < DENSITY) {
                // Place a duckling in this lane:
                ducklingObj = new Duckling();
                ducklingLanes[laneNum] = ducklingObj;
            }

            if (ducklingObj != null) {
                // Draw a duckling if there is one in this lane:
                process.stdout.write(ducklingObj.getNextBodyPart());
                // Delete the duckling if we've finished drawing it:
                if (ducklingObj.partToDisplayNext == null) {
                    ducklingLanes[laneNum] = null;
                }
            } else {
                // Draw five spaces since there is no duckling here.
                process.stdout.write(' '.repeat(DUCKLING_WIDTH));
            }
        }
        console.log();  // Print a newline.
        await sleep(PAUSE);
    }
}

class Duckling {
    constructor() {
        // Create a new duckling with random body features.
        this.direction = [LEFT, RIGHT][Math.floor(Math.random() * 2)];
        this.body = [CHUBBY, VERY_CHUBBY][Math.floor(Math.random() * 2)];
        this.mouth = [OPEN, CLOSED][Math.floor(Math.random() * 2)];
        this.wing = [OUT, UP, DOWN][Math.floor(Math.random() * 3)];

        if (this.body === CHUBBY) {
            // Chubby ducklings can only have beady eyes.
            this.eyes = BEADY;
        } else {
            this.eyes = [BEADY, WIDE, HAPPY, ALOOF][Math.floor(Math.random() * 4)];
        }

        this.partToDisplayNext = HEAD;
    }

    getHeadStr() {
        // Returns the string of the duckling's head.
        let headStr = '';
        if (this.direction === LEFT) {
            // Get the mouth:
            if (this.mouth === OPEN) {
                headStr += '>';
            } else if (this.mouth === CLOSED) {
                headStr += '=';
            }

            // Get the eyes:
            if (this.eyes === BEADY && this.body === CHUBBY) {
                headStr += '"';
            } else if (this.eyes === BEADY && this.body === VERY_CHUBBY) {
                headStr += '" ';
            } else if (this.eyes === WIDE) {
                headStr += "''";
            } else if (this.eyes === HAPPY) {
                headStr += '^^';
            } else if (this.eyes === ALOOF) {
                headStr += '``';
            }

            headStr += ') ';  // Get the back of the head.
        }

        if (this.direction === RIGHT) {
            headStr += ' (';  // Get the back of the head.

            // Get the eyes:
            if (this.eyes === BEADY && this.body === CHUBBY) {
                headStr += '"';
            } else if (this.eyes === BEADY && this.body === VERY_CHUBBY) {
                headStr += ' "';
            } else if (this.eyes === WIDE) {
                headStr += "''";
            } else if (this.eyes === HAPPY) {
                headStr += '^^';
            } else if (this.eyes === ALOOF) {
                headStr += '``';
            }

            // Get the mouth:
            if (this.mouth === OPEN) {
                headStr += '<';
            } else if (this.mouth === CLOSED) {
                headStr += '=';
            }
        }

        if (this.body === CHUBBY) {
            // Get an extra space so chubby ducklings are the same
            // width as very chubby ducklings.
            headStr += ' ';
        }

        return headStr;
    }

    getBodyStr() {
        // Returns the string of the duckling's body.
        let bodyStr = '(';  // Get the left side of the body.
        if (this.direction === LEFT) {
            // Get the interior body space:
            if (this.body === CHUBBY) {
                bodyStr += ' ';
            } else if (this.body === VERY_CHUBBY) {
                bodyStr += '  ';
            }

            // Get the wing:
            if (this.wing === OUT) {
                bodyStr += '>';
            } else if (this.wing === UP) {
                bodyStr += '^';
            } else if (this.wing === DOWN) {
                bodyStr += 'v';
            }
        }

        if (this.direction === RIGHT) {
            // Get the wing:
            if (this.wing === OUT) {
                bodyStr += '<';
            } else if (this.wing === UP) {
                bodyStr += '^';
            } else if (this.wing === DOWN) {
                bodyStr += 'v';
            }

            // Get the interior body space:
            if (this.body === CHUBBY) {
                bodyStr += ' ';
            } else if (this.body === VERY_CHUBBY) {
                bodyStr += '  ';
            }
        }

        bodyStr += ')';  // Get the right side of the body.

        if (this.body === CHUBBY) {
            // Get an extra space so chubby ducklings are the same
            // width as very chubby ducklings.
            bodyStr += ' ';
        }

        return bodyStr;
    }

    getFeetStr() {
        // Returns the string of the duckling's feet.
        if (this.body === CHUBBY) {
            return ' ^^  ';
        } else if (this.body === VERY_CHUBBY) {
            return ' ^ ^ ';
        }
    }

    getNextBodyPart() {
        // Calls the appropriate display method for the next body
        // part that needs to be displayed. Sets partToDisplayNext to
        // null when finished.
        if (this.partToDisplayNext === HEAD) {
            this.partToDisplayNext = BODY;
            return this.getHeadStr();
        } else if (this.partToDisplayNext === BODY) {
            this.partToDisplayNext = FEET;
            return this.getBodyStr();
        } else if (this.partToDisplayNext === FEET) {
            this.partToDisplayNext = null;
            return this.getFeetStr();
        }
    }
}


main();
