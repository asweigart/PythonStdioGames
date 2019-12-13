# Games By Example
# By Al Sweigart al@inventwithpython.com

__version__ = '0.1.2'

# TODO - check if the support files have been changed and let the user undo changes.


PROGRAMS = [   {   'desc': 'A time-based quiz game to see how fast you can alphabetize letters.',
        'filename': 'alphabetizequiz.py',
        'hash': 307675784,
        'name': 'Alphabetize Quiz'},
    {   'desc': 'A time-based quiz game to see how fast you can alphabetize words.',
        'filename': 'alphabetizewordquiz.py',
        'hash': 1222634656,
        'name': 'Alphabetize Word Quiz'},
    {   'desc': 'An analog clock animation. Press Ctrl-C to stop.',
        'filename': 'analogclock.py',
        'hash': 1694305677,
        'name': 'Analog Clock'},
    {   'desc': 'A deductive logic game where you must guess a number based on clues.',
        'filename': 'bagels.py',
        'hash': 1404489787,
        'name': 'Bagels'},
    {   'desc': 'Explore the mathematics of the "Birthday Paradox". More info at '
                'https://en.wikipedia.org/wiki/Birthday_problem',
        'filename': 'birthdayparadox.py',
        'hash': 3339047095,
        'name': 'Birthday Paradox Simulation'},
    {   'desc': 'A card game also known as 21. More info at: https://en.wikipedia.org/wiki/Blackjack',
        'filename': 'blackjack.py',
        'hash': 3092141501,
        'name': 'Blackjack'},
    {   'desc': 'A bouncing ball animation. Press Ctrl-C to stop.',
        'filename': 'bouncingDots.py',
        'hash': 3149335062,
        'name': 'Bouncing Ball'},
    {   'desc': 'A bouncing line animation. Press Ctrl-C to stop.',
        'filename': 'bouncingLines.py',
        'hash': 2000350610,
        'name': 'Bouncing Lines'},
    {   'desc': 'Create monthly calendars, saved to a text file and fit for printing.',
        'filename': 'calendarmaker.py',
        'hash': 79367604,
        'name': 'Calendar Maker'},
    {   'desc': 'Checkers, but you can move 3 random checkers per turn. These checkers are randomly decided, and can '
                "be the player's own checkers or their opponents', but you can't move your opponents' promoted "
                'checkers. In this version, capturing is not mandatory.',
        'filename': 'chancecheckers.py',
        'hash': 217226431,
        'name': 'Chance Checkers'},
    {   'desc': 'Try to get the robots to crash into each other.',
        'filename': 'chase.py',
        'hash': 2506428124,
        'name': 'Daleks'},
    {   'desc': 'The classic checkers board game. In this version, capturing is not mandatory.',
        'filename': 'checkers.py',
        'hash': 3446663365,
        'name': 'Checkers'},
    {   'desc': 'A dangerously delicious logic game. Inspired by a Frederik Schuh and David Gale puzzle, published by '
                'Martin Gardner in Scientific American (January 1973) More info at: '
                'https://en.wikipedia.org/wiki/Chomp',
        'filename': 'chomp.py',
        'hash': 433695091,
        'name': 'Chomp'},
    {   'desc': 'A clickbait headline generator for your soulless content farm.',
        'filename': 'clickbait.py',
        'hash': 1805171330,
        'name': 'Clickbait Headline Generator'},
    {   'desc': 'Simulate a large number of coin flips.',
        'filename': 'coinflipsimulator.py',
        'hash': 289286594,
        'name': 'Coin Flip Simulator'},
    {   'desc': 'Generates numbers for the Collatz sequence, given a starting number.',
        'filename': 'collatz.py',
        'hash': 3350478253,
        'name': 'Collatz Sequence'},
    {   'desc': 'Finds out how long various Collatz Sequences are.',
        'filename': 'collatzstats.py',
        'hash': 217777193,
        'name': 'Collatz Sequence Stats'},
    {   'desc': 'A board game to get four tiles in a row.',
        'filename': 'connectfour.py',
        'hash': 871784039,
        'name': 'Connect Four'},
    {   'desc': 'The classic cellular automata simulation. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life',
        'filename': 'conwaysgameoflife1.py',
        'hash': 3041337216,
        'name': "Conway's Game of Life"},
    {   'desc': 'The classic cellular automata simulation. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life',
        'filename': 'conwaysgameoflife2.py',
        'hash': 4173968307,
        'name': "Conway's Game of Life (Terminal)"},
    {   'desc': 'Show a countdown timer animation using a seven-segment display. Press Ctrl-C to stop. More info at '
                'https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.',
        'filename': 'countdown.py',
        'hash': 1668872601,
        'name': 'Countdown'},
    {   'desc': 'Prints out a random, diagonal maze. Inspired by the 10 PRINT CHR$(205.5+RND(1)); : GOTO 10 program.',
        'filename': 'diagonalmaze.py',
        'hash': 4028274581,
        'name': 'Diagonal Maze'},
    {   'desc': 'Simulates dice rolls using the Dungeons & Dragons notation.',
        'filename': 'diceroller.py',
        'hash': 3491855660,
        'name': 'Dice Roller'},
    {   'desc': 'Display a digital clock of the current time with a seven-segment display. Press Ctrl-C to stop. More '
                'info at https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.',
        'filename': 'digitalclock.py',
        'hash': 3018689073,
        'name': 'Digital Clock'},
    {   'desc': 'A simple animation of a DNA double-helix. Press Ctrl-C to stop. Thanks to matoken for inspiration: '
                'https://asciinema.org/a/155441',
        'filename': 'dna.py',
        'hash': 3459975404,
        'name': 'DNA'},
    {   'desc': 'An elimination game for multiple players. Press Ctrl-C to stop. More info at '
                'https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe More info at '
                'https://en.wikipedia.org/wiki/Josephus_problem',
        'filename': 'eenymeeny.py',
        'hash': 2500902243,
        'name': 'Eeny-Meeny-Miny-Moe'},
    {   'desc': 'Draw a trailing line on the screen.',
        'filename': 'etchasketch.py',
        'hash': 3337598765,
        'name': 'Etch a Sketch'},
    {   'desc': 'Find all the factors of a number.',
        'filename': 'factorfinder.py',
        'hash': 2291806082,
        'name': 'Factorization'},
    {   'desc': 'A beautiful animation of fireflies. Press Ctrl-C to stop.',
        'filename': 'fireflies.py',
        'hash': 2485316294,
        'name': 'Fireflies'},
    {   'desc': 'A peaceful animation of a fish tank. Press Ctrl-C to stop.',
        'filename': 'fishtank.py',
        'hash': 1414251731,
        'name': 'Fish Tank'},
    {   'desc': 'Calculates the answers for the fizz buzz programming problem.',
        'filename': 'fizzbuzz.py',
        'hash': 1498107850,
        'name': 'FizzBuzz Calculation'},
    {   'desc': 'A number game where you also race against the clock.',
        'filename': 'fizzbuzzgame.py',
        'hash': 1743347055,
        'name': 'FizzBuzz Game'},
    {   'desc': 'An example of a "flood fill" algorithm. This is a basic demo of both the recursive and iterative '
                'floodfill algorithms. This algorithm is commonly used in "fill tools" in graphics programs like MS '
                'Paint or Photoshop. This algorithm is also used in the floodit.py game.',
        'filename': 'floodfill.py',
        'hash': 1656448832,
        'name': 'Flood Fill'},
    {   'desc': 'A colorful game where you try to fill the board with a single color.',
        'filename': 'floodit.py',
        'hash': 1790378754,
        'name': 'Flood It!'},
    {   'desc': "A simulation of fires spreading in a growing forest. Press Ctrl-C to stop. Inspired by Nicky Case's "
                'Emoji Sim http://ncase.me/simulating/model/',
        'filename': 'forestfiresim.py',
        'hash': 1564978639,
        'name': 'Forest Fire Sim'},
    {   'desc': 'Draws nonuniform fractal trees with turtle graphics.',
        'filename': 'fractalnonuniformtree.py',
        'hash': 3841218830,
        'name': 'Nonuniform Fractal Tree Drawer'},
    {   'desc': 'Draws fractal trees with turtle graphics.',
        'filename': 'fractaltree.py',
        'hash': 1667533298,
        'name': 'Fractal Tree Drawer'},
    {   'desc': "A sliding tile game to combine exponentially-increasing numbers. Inspired by Gabriele Cirulli's 2048, "
                "which is a clone of Veewo Studios' 1024, which in turn is a clone of the Threes! game. More info at "
                'https://en.wikipedia.org/wiki/2048_(video_game)',
        'filename': 'game2048.py',
        'hash': 1788641125,
        'name': '2048 Game'},
    {   'desc': 'Follow the trail to see who wins! More info at: https://en.wikipedia.org/wiki/Ghost_Leg',
        'filename': 'ghostleglottery.py',
        'hash': 3727009682,
        'name': 'Ghost Leg Lottery'},
    {   'desc': 'While given hints, try to guess the secret number.',
        'filename': 'guess.py',
        'hash': 1746502559,
        'name': 'Guess the Number'},
    {   'desc': 'A French variant of Hangman with different graphics. Ooh la la!',
        'filename': 'guillotine.py',
        'hash': 2136635378,
        'name': 'Guillotine'},
    {   'desc': 'The hacking mini-game from "Fallout 3".',
        'filename': 'hacking.py',
        'hash': 1817878266,
        'name': 'Hacking'},
    {   'desc': 'The classic game Hamurabi.bas by Doug Dyment, popularized by David Ahl.',
        'filename': 'hammurabi.py',
        'hash': 3792387059,
        'name': 'Hammurabi'},
    {   'desc': 'A program for making silly pluralizations. Press Ctrl-C to stop.',
        'filename': 'hamsburger.py',
        'hash': 592436006,
        'name': 'Hamsburger'},
    {'desc': 'A word-guessing game.', 'filename': 'hangman.py', 'hash': 3412092519, 'name': 'Hangman'},
    {   'desc': 'A completely unfair word-guessing game. (This is a joke program.)',
        'filename': 'hangmanunfair.py',
        'hash': 3984461757,
        'name': 'Hangman with Random Letters'},
    {   'desc': 'Play tic tac toe against the computer. Every possible move has been hard-coded into this program. The '
                "program is 5700 lines long. This is a joke program, don't actually write code like this.",
        'filename': 'hardcodedtictactoe.py',
        'hash': 1297968413,
        'name': 'Hard-coded Tic Tac Toe'},
    {   'desc': 'Draws the Hilbert Curve fractal with turtle graphics. More info at: '
                'https://en.wikipedia.org/wiki/hilbertCurve Good videos on space-filling curves: '
                'https://youtu.be/RU0wScIj36o and https://youtu.be/3s7h2MHQtxc',
        'filename': 'hilbertcurve.py',
        'hash': 3385678044,
        'name': 'Hilbert Curve'},
    {   'desc': 'An animation of an hour glass filled with falling sand. Press Ctrl-C to stop.',
        'filename': 'hourglass.py',
        'hash': 1701820225,
        'name': 'Hour Glass Animation'},
    {   'desc': 'How to keep an idiot busy for hours. (This is a joke program.)',
        'filename': 'idiot.py',
        'hash': 182378621,
        'name': 'Idiot'},
    {   'desc': 'A mystery game of intrigue and a missing cat. Inspired by Homestar Runner\'s "Where\'s an Egg?" game',
        'filename': 'jaccuse.py',
        'hash': 1153808863,
        'name': "J'ACCUSE!"},
    {   'desc': 'Draws a Koch snowflake fractal with turtle graphics.',
        'filename': 'kochsnowflake.py',
        'hash': 989009564,
        'name': 'Koch Snowflake'},
    {   'desc': 'A cellular automata animation. Press Ctrl-C to stop. More info: '
                'https://en.wikipedia.org/wiki/Langton%27s_ant',
        'filename': 'langtonsant.py',
        'hash': 1552587337,
        'name': "Langton's Ant"},
    {   'desc': 'Watch grass get cut and grow again. Press Ctrl-C to stop. Inspired by Tondeuse by Jules Villard, '
                'https://asciinema.org/a/21743 https://bitbucket.org/jvillard/tondeuse/src/default/',
        'filename': 'lawnmower.py',
        'hash': 2875948028,
        'name': 'Lawnmower'},
    {   'desc': 'Translates English messages into l33t5p34]<.',
        'filename': 'leetspeak.py',
        'hash': 2489424941,
        'name': 'Leetspeak'},
    {   'desc': 'The mathematics behind credit card numbers. More info at: '
                'https://en.wikipedia.org/wiki/Luhn_algorithm More info at: https://youtu.be/Erp8IAUouus',
        'filename': 'luhn.py',
        'hash': 1491860318,
        'name': 'Luhn Checksum Algorithm'},
    {   'desc': 'Ask a question about your future.',
        'filename': 'magic8ball.py',
        'hash': 4220249488,
        'name': 'Magic Eight Ball'},
    {   'desc': 'Place numbers in a hexagon so each row adds up to 38. More info at '
                'https://en.wikipedia.org/wiki/Magic_hexagon More info at https://www.youtube.com/watch?v=ZkVSRwFWjy0',
        'filename': 'magichexagon.py',
        'hash': 3501379836,
        'name': 'Magic Hexagon'},
    {   'desc': 'The ancient seed-sowing board game. Rules at http://www.mancalarules.com/ More info at '
                'https://en.wikipedia.org/wiki/Mancala',
        'filename': 'mancala.py',
        'hash': 4268751306,
        'name': 'Mancala'},
    {   'desc': 'A parentheses/bracket/braces matching algorithm.',
        'filename': 'matchingparens.py',
        'hash': 1733863137,
        'name': 'Matching Parentheses'},
    {   'desc': 'Make mazes with the recursive backtracker algorithm. More info at: '
                'https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker An animated demo: '
                'https://scratch.mit.edu/projects/17358777/',
        'filename': 'mazemakerrec.py',
        'hash': 1444274149,
        'name': 'Maze Maker'},
    {   'desc': 'Move around a maze and try to escape.',
        'filename': 'mazerunner2d.py',
        'hash': 2667385089,
        'name': 'Maze Runner'},
    {   'desc': 'Move around a maze and try to escape... in 3D!',
        'filename': 'mazerunner3d.py',
        'hash': 2785410806,
        'name': 'Maze 3D'},
    {   'desc': 'Move around a maze and try to escape... in 3D and IN YOUR WEB BROWSER!',
        'filename': 'mazerunnerhtml.py',
        'hash': 980857557,
        'name': 'Maze Runner HTML'},
    {   'desc': 'Scrambles the middle letters of words, but not the first and last letters.',
        'filename': 'middleletterscrambler.py',
        'hash': 731181800,
        'name': 'Middle Letter Scrambler'},
    {   'desc': 'A simulation of one million dice rolls.',
        'filename': 'milliondicestats.py',
        'hash': 4144516934,
        'name': 'Million Dice Roll Stats'},
    {   'desc': 'Draws an Andy Warhol-like drawing of the Mona Lisa with turtle graphics.',
        'filename': 'monalisa.py',
        'hash': 3205378818,
        'name': 'Mona Lisa'},
    {   'desc': 'Randomly generates Mondrian-style art.',
        'filename': 'mondrian.py',
        'hash': 1358656645,
        'name': 'Mondrian Art Generator'},
    {   'desc': 'A simulation of the Monty Hall game show problem. More info at '
                'https://en.wikipedia.org/wiki/Monty_Hall_problem',
        'filename': 'montyhall.py',
        'hash': 2135606057,
        'name': 'Monty Hall Problem'},
    {   'desc': 'Translates between English and Morse Code. More info at: https://en.wikipedia.org/wiki/Morse_code',
        'filename': 'morsecode.py',
        'hash': 4250784930,
        'name': 'Morse Code'},
    {   'desc': 'Print a multiplication table.',
        'filename': 'multiplicationtable.py',
        'hash': 2484928382,
        'name': 'Multiplication Table'},
    {   'desc': 'A fun math challenge. For more information about this topic, see https://youtu.be/Wim9WJeDTHQ',
        'filename': 'multiplicativepersistence.py',
        'hash': 3397130480,
        'name': 'Multiplicative Persistence'},
    {   'desc': 'Print the full lyrics to one of the most longest songs ever! Press Ctrl-C to stop.',
        'filename': 'ninetyninebottles.py',
        'hash': 182622512,
        'name': '99 Bottles of Beer on the Wall'},
    {   'desc': 'A single-player, peg-jumping game to eliminate all the pegs. More info at '
                'https://en.wikipedia.org/wiki/Peg_solitaire',
        'filename': 'pegsolitaire.py',
        'hash': 835016107,
        'name': 'Peg Solitaire'},
    {   'desc': 'Displays atomic information for all the elements.',
        'filename': 'periodictable.py',
        'hash': 2041198239,
        'name': 'Periodic Table of Elements'},
    {   'desc': 'Translates English messages into Igpay Atinlay.',
        'filename': 'piglatin.py',
        'hash': 4064984187,
        'name': 'Pig Latin'},
    {   'desc': 'A turtle program to draw polygons. Every line is the same length.',
        'filename': 'polygons.py',
        'hash': 584601590,
        'name': 'Polygons'},
    {   'desc': 'A sample progress bar animation that can be used in other programs.',
        'filename': 'progressbar.py',
        'hash': 3281085795,
        'name': 'Progress Bar'},
    {'desc': 'Drawing pythons with turtle graphics.', 'filename': 'pythons.py', 'hash': 3522936448, 'name': 'Pythons'},
    {   'desc': 'The "rail fence" cipher for encrypting text. More info at: '
                'https://en.wikipedia.org/wiki/Rail_fence_cipher',
        'filename': 'railfencecipher.py',
        'hash': 39302442,
        'name': 'Rail Fence Cipher'},
    {   'desc': 'Shows a simple rainbow animation. Press Ctrl-C to stop.',
        'filename': 'rainbow.py',
        'hash': 2195377487,
        'name': 'Rainbow'},
    {   'desc': 'Shows a simple squiggle rainbow animation. Press Ctrl-C to stop.',
        'filename': 'rainbow2.py',
        'hash': 3157761642,
        'name': 'Rainbow 2'},
    {   'desc': 'Generate splatter-art with the "random walk" algorithm. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Random_walk',
        'filename': 'randomwalk.py',
        'hash': 2696752006,
        'name': 'Random Walk'},
    {   'desc': 'A tile flipping game, also called reversi. More info https://en.wikipedia.org/wiki/Reversi',
        'filename': 'reversi.py',
        'hash': 1878561007,
        'name': 'Reversi'},
    {   'desc': 'A hand game of luck.',
        'filename': 'rockpaperscissors.py',
        'hash': 2975526873,
        'name': 'Rock-Paper-Scissors'},
    {   'desc': 'A hand game of luck, except you cannot lose.',
        'filename': 'rockpaperscissorsalwayswin.py',
        'hash': 3223900370,
        'name': 'Rock-Paper-Scissors (Always Win)'},
    {   'desc': 'The simplest cipher for encrypting and decrypting text. More info at '
                'https://en.wikipedia.org/wiki/ROT13',
        'filename': 'rot13.py',
        'hash': 857147918,
        'name': 'ROT13 Cipher'},
    {   'desc': 'A rotating cube animation. Press Ctrl-C to stop.',
        'filename': 'rotatingcube.py',
        'hash': 4068305284,
        'name': 'Rotating Cube'},
    {   'desc': 'A rotating cube animation. Press Ctrl-C to stop.',
        'filename': 'rotatingcubebext.py',
        'hash': 3244895651,
        'name': 'Rotating Cube (Bext Version)'},
    {   'desc': 'A rotating sphere animation. Press Ctrl-C to stop.',
        'filename': 'rotatingsphere.py',
        'hash': 509642564,
        'name': 'Rotating Sphere'},
    {   'desc': 'A sliding tile puzzle game to move cars out of the way. Original game by Nob Yoshihagara More info at '
                'https://www.michaelfogleman.com/rush/',
        'filename': 'rushhour.py',
        'hash': 1278069698,
        'name': 'Rush Hour'},
    {   'desc': 'A falling sand animation. Inspired by https://asciinema.org/a/6515',
        'filename': 'sandfall.py',
        'hash': 1584057420,
        'name': 'Sand Fall'},
    {   'desc': 'A falling sand animation. Inspired by https://asciinema.org/a/6515',
        'filename': 'sandfallbext.py',
        'hash': 2478780728,
        'name': 'Sand Fall (Bext Version)'},
    {   'desc': 'A seven-segment display module. More info at https://en.wikipedia.org/wiki/Seven-segment_display',
        'filename': 'sevseg.py',
        'hash': 351868863,
        'name': 'Sevseg'},
    {'desc': 'A random gambling game.', 'filename': 'shellgame.py', 'hash': 2667879344, 'name': 'Shell Game'},
    {   'desc': 'Sierpinkski\'s "game" is an algorithm that draws Sierpinski\'s Triangle with turtle graphics. More '
                'info at https://en.wikipedia.org/wiki/Chaos_game',
        'filename': 'sierpinskisgame.py',
        'hash': 1228340578,
        'name': "Sierpinkski's Game"},
    {   'desc': 'Draws the Sierpinski Square (also called Carpet) with turtle graphics. More info at: '
                'https://en.wikipedia.org/wiki/Sierpinski_carpet',
        'filename': 'sierpinskisquare.py',
        'hash': 1347541107,
        'name': 'Sierpinski Square'},
    {   'desc': 'Draws the Sierpinski Triangle fractal with turtle graphics.',
        'filename': 'sierpinskitriangle.py',
        'hash': 799027170,
        'name': 'Sierpinski Triangle'},
    {   'desc': 'Slide the numbered tiles into the correct order.',
        'filename': 'slidingpuzzle.py',
        'hash': 853392377,
        'name': '15-Sliding Puzzle'},
    {'desc': 'Fast-paced snail racing action!', 'filename': 'snailrace.py', 'hash': 2153561977, 'name': 'Snail Race'},
    {'desc': 'The classic crate-pushing game.', 'filename': 'sokoban.py', 'hash': 2408463409, 'name': 'Sokoban clone'},
    {   'desc': 'Try to locate treasure chests hidden under the waves.',
        'filename': 'sonar.py',
        'hash': 2882284494,
        'name': 'Sonar Treasure Hunt'},
    {   'desc': 'A simulation of a Japanese abacus calculator tool. More info at: '
                'https://en.wikipedia.org/wiki/Soroban',
        'filename': 'soroban.py',
        'hash': 4265544677,
        'name': 'Soroban'},
    {'desc': 'Draws a simple square spiral.', 'filename': 'spiral.py', 'hash': 3378282052, 'name': 'Spiral'},
    {   'desc': 'Translates English messages into sPOnGEtExT.',
        'filename': 'spongetext.py',
        'hash': 1477272675,
        'name': 'sPoNgEtExT'},
    {   'desc': 'A jewel-stealing, movement puzzle game.',
        'filename': 'stickyhands.py',
        'hash': 970116041,
        'name': 'Sticky Hands'},
    {   'desc': 'The classic 9x9 number placement puzzle. More info at https://en.wikipedia.org/wiki/Sudoku',
        'filename': 'sudoku.py',
        'hash': 2514734032,
        'name': 'Sudoku'},
    {   'desc': 'Find the Queen of Hearts after cards have been swapped around. (In the real-life version, the scammer '
                'palms the Queen of Hearts so you always lose.) More info at '
                'https://en.wikipedia.org/wiki/Three-card_Monte',
        'filename': 'threecardmonte.py',
        'hash': 2589316695,
        'name': 'Three-Card Monte'},
    {'desc': 'The classic board game.', 'filename': 'tictactoe.py', 'hash': 3678726451, 'name': 'Tic Tac Toe'},
    {   'desc': 'The classic board game. (Object-oriented programming version.)',
        'filename': 'tictactoeoop.py',
        'hash': 3504192674,
        'name': 'Tic Tac Toe (OOP)'},
    {   'desc': 'A puzzle where you must move the discs of one tower to another tower. More info at '
                'https://en.wikipedia.org/wiki/Tower_of_Hanoi',
        'filename': 'towersofhanoi.py',
        'hash': 1119871156,
        'name': 'Towers of Hanoi puzzle'},
    {   'desc': 'Part 1 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess1.py',
        'hash': 3883221959,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 2 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess2.py',
        'hash': 4260938038,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 3 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess3.py',
        'hash': 1710092025,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 4 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess4.py',
        'hash': 1533287551,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 5 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess5.py',
        'hash': 1419588263,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 6 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess6.py',
        'hash': 2374516065,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'Part 7 of a tutorial to make a "Guess the Number" game, bit by bit.',
        'filename': 'tutorialguess7.py',
        'hash': 3141556618,
        'name': 'Tutorial: Guess the Number'},
    {   'desc': 'The Ulam spiral is a mysterious mathematics pattern for prime numbers with turtle graphics. More info '
                'at https://en.wikipedia.org/wiki/Ulam_spiral',
        'filename': 'ulamspiral.py',
        'hash': 4022741212,
        'name': 'Ulam Spiral'},
    {   'desc': 'A water pouring puzzle. More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle',
        'filename': 'waterbucket.py',
        'hash': 3438733868,
        'name': 'Water Bucket Puzzle'},
    {   'desc': 'A simple zig zag animation. Press Ctrl-C to stop.',
        'filename': 'zigzag.py',
        'hash': 1447297864,
        'name': 'Zigzag'},
    {   'desc': '(Pygame) Play against the computer and try to flip their tiles.',
        'filename': 'pygame_games/flippy.py',
        'hash': 677788829,
        'name': 'Flippy (a Reversi clone)'},
    {   'desc': '(Pygame) Play against the computer, dropping tiles to connect four.',
        'filename': 'pygame_games/fourinarow.py',
        'hash': 608753110,
        'name': 'Four-In-A-Row'},
    {   'desc': '(Pygame) An addictive jewel matching game.',
        'filename': 'pygame_games/gemgem.py',
        'hash': 775522148,
        'name': 'Gemgem (a Bejeweled clone)'},
    {   'desc': '(Pygame) Try to make the entire field a single color.',
        'filename': 'pygame_games/inkspill.py',
        'hash': 4017926080,
        'name': 'Ink Spill (a Flood It clone)'},
    {   'desc': '(Pygame) A simple memory matching game.',
        'filename': 'pygame_games/memorypuzzle.py',
        'hash': 2802044137,
        'name': 'Memory Puzzle'},
    {   'desc': '(Pygame) Like Pygame, except with 5-box blocks.',
        'filename': 'pygame_games/pentomino.py',
        'hash': 1893593320,
        'name': 'Pentomino'},
    {   'desc': '(Pygame) Copy the pattern of flashing lights for as long as possible.',
        'filename': 'pygame_games/simulate.py',
        'hash': 3932677495,
        'name': 'Simulate (a Simon clone)'},
    {   'desc': '(Pygame) The classic 15-tile slide puzzle.',
        'filename': 'pygame_games/slidepuzzle.py',
        'hash': 4202430347,
        'name': 'Slide Puzzle'},
    {   'desc': '(Pygame) A game where squirrels eat each other and grow monstrously large.',
        'filename': 'pygame_games/squirrel.py',
        'hash': 54285070,
        'name': 'Squirrel Eat Squirrel'},
    {   'desc': '(Pygame) A puzzle game where you push the stars over their goals.',
        'filename': 'pygame_games/starpusher.py',
        'hash': 2972756940,
        'name': 'Star Pusher (a Sokoban clone)'},
    {   'desc': '(Pygame) The classic block falling puzzle from the Soviet Union.',
        'filename': 'pygame_games/tetromino.py',
        'hash': 2445993684,
        'name': 'Tetromino (a Tetris clone)'},
    {   'desc': '(Pygame) Tetris, but... simpler.',
        'filename': 'pygame_games/tetrominoforidiots.py',
        'hash': 1910250987,
        'name': 'Tetromino for Idiots'},
    {   'desc': '(Pygame) Lead the green snake around the screen eating red apples.',
        'filename': 'pygame_games/wormy.py',
        'hash': 3165165432,
        'name': 'Wormy'}]

SUPPORT_FILES = {   'alphabetizewordquiz.py': ['commonenglishwords.txt'],
    'hamsburger.py': ['nounlist.txt'],
    'mazerunner2d.py': ['maze11x11s1.txt', 'maze51x17s42.txt'],
    'mazerunnerhtml.py': [   'maze11x11s1',
                             'maze_html_images',
                             'maze_html_images/A.jpg',
                             'maze_html_images/AB.jpg',
                             'maze_html_images/ABC.jpg',
                             'maze_html_images/ABCD.jpg',
                             'maze_html_images/ABCDE.jpg',
                             'maze_html_images/ABCDEF.jpg',
                             'maze_html_images/ABCDEF_exitback.jpg',
                             'maze_html_images/ABCDEF_exitleft.jpg',
                             'maze_html_images/ABCDEF_exitright.jpg',
                             'maze_html_images/ABCDE_exitback.jpg',
                             'maze_html_images/ABCDE_exitleft.jpg',
                             'maze_html_images/ABCDE_exitright.jpg',
                             'maze_html_images/ABCDF.jpg',
                             'maze_html_images/ABCDF_exitback.jpg',
                             'maze_html_images/ABCDF_exitleft.jpg',
                             'maze_html_images/ABCDF_exitright.jpg',
                             'maze_html_images/ABCD_exitback.jpg',
                             'maze_html_images/ABCD_exitleft.jpg',
                             'maze_html_images/ABCD_exitright.jpg',
                             'maze_html_images/ABCE.jpg',
                             'maze_html_images/ABCEF.jpg',
                             'maze_html_images/ABCEF_exitback.jpg',
                             'maze_html_images/ABCEF_exitleft.jpg',
                             'maze_html_images/ABCEF_exitright.jpg',
                             'maze_html_images/ABCE_exitback.jpg',
                             'maze_html_images/ABCE_exitleft.jpg',
                             'maze_html_images/ABCE_exitright.jpg',
                             'maze_html_images/ABCF.jpg',
                             'maze_html_images/ABCF_exitback.jpg',
                             'maze_html_images/ABCF_exitleft.jpg',
                             'maze_html_images/ABCF_exitright.jpg',
                             'maze_html_images/ABC_exitback.jpg',
                             'maze_html_images/ABC_exitleft.jpg',
                             'maze_html_images/ABC_exitright.jpg',
                             'maze_html_images/ABD.jpg',
                             'maze_html_images/ABDE.jpg',
                             'maze_html_images/ABDEF.jpg',
                             'maze_html_images/ABDEF_exitback.jpg',
                             'maze_html_images/ABDEF_exitleft.jpg',
                             'maze_html_images/ABDEF_exitright.jpg',
                             'maze_html_images/ABDE_exitback.jpg',
                             'maze_html_images/ABDE_exitleft.jpg',
                             'maze_html_images/ABDE_exitright.jpg',
                             'maze_html_images/ABDF.jpg',
                             'maze_html_images/ABDF_exitback.jpg',
                             'maze_html_images/ABDF_exitleft.jpg',
                             'maze_html_images/ABDF_exitright.jpg',
                             'maze_html_images/ABD_exitback.jpg',
                             'maze_html_images/ABD_exitleft.jpg',
                             'maze_html_images/ABD_exitright.jpg',
                             'maze_html_images/ABE.jpg',
                             'maze_html_images/ABEF.jpg',
                             'maze_html_images/ABEF_exitback.jpg',
                             'maze_html_images/ABEF_exitleft.jpg',
                             'maze_html_images/ABEF_exitright.jpg',
                             'maze_html_images/ABE_exitback.jpg',
                             'maze_html_images/ABE_exitleft.jpg',
                             'maze_html_images/ABE_exitright.jpg',
                             'maze_html_images/ABF.jpg',
                             'maze_html_images/ABF_exitback.jpg',
                             'maze_html_images/ABF_exitleft.jpg',
                             'maze_html_images/ABF_exitright.jpg',
                             'maze_html_images/AB_exitback.jpg',
                             'maze_html_images/AB_exitleft.jpg',
                             'maze_html_images/AB_exitright.jpg',
                             'maze_html_images/AC.jpg',
                             'maze_html_images/ACD.jpg',
                             'maze_html_images/ACDE.jpg',
                             'maze_html_images/ACDEF.jpg',
                             'maze_html_images/ACDEF_exitback.jpg',
                             'maze_html_images/ACDEF_exitleft.jpg',
                             'maze_html_images/ACDEF_exitright.jpg',
                             'maze_html_images/ACDE_exitback.jpg',
                             'maze_html_images/ACDE_exitleft.jpg',
                             'maze_html_images/ACDE_exitright.jpg',
                             'maze_html_images/ACDF.jpg',
                             'maze_html_images/ACDF_exitback.jpg',
                             'maze_html_images/ACDF_exitleft.jpg',
                             'maze_html_images/ACDF_exitright.jpg',
                             'maze_html_images/ACD_exitback.jpg',
                             'maze_html_images/ACD_exitleft.jpg',
                             'maze_html_images/ACD_exitright.jpg',
                             'maze_html_images/ACE.jpg',
                             'maze_html_images/ACEF.jpg',
                             'maze_html_images/ACEF_exitback.jpg',
                             'maze_html_images/ACEF_exitleft.jpg',
                             'maze_html_images/ACEF_exitright.jpg',
                             'maze_html_images/ACE_exitback.jpg',
                             'maze_html_images/ACE_exitleft.jpg',
                             'maze_html_images/ACE_exitright.jpg',
                             'maze_html_images/ACF.jpg',
                             'maze_html_images/ACF_exitback.jpg',
                             'maze_html_images/ACF_exitleft.jpg',
                             'maze_html_images/ACF_exitright.jpg',
                             'maze_html_images/AC_exitback.jpg',
                             'maze_html_images/AC_exitleft.jpg',
                             'maze_html_images/AC_exitright.jpg',
                             'maze_html_images/AD.jpg',
                             'maze_html_images/ADE.jpg',
                             'maze_html_images/ADEF.jpg',
                             'maze_html_images/ADEF_exitback.jpg',
                             'maze_html_images/ADEF_exitleft.jpg',
                             'maze_html_images/ADEF_exitright.jpg',
                             'maze_html_images/ADE_exitback.jpg',
                             'maze_html_images/ADE_exitleft.jpg',
                             'maze_html_images/ADE_exitright.jpg',
                             'maze_html_images/ADF.jpg',
                             'maze_html_images/ADF_exitback.jpg',
                             'maze_html_images/ADF_exitleft.jpg',
                             'maze_html_images/ADF_exitright.jpg',
                             'maze_html_images/AD_exitback.jpg',
                             'maze_html_images/AD_exitleft.jpg',
                             'maze_html_images/AD_exitright.jpg',
                             'maze_html_images/AE.jpg',
                             'maze_html_images/AEF.jpg',
                             'maze_html_images/AEF_exitback.jpg',
                             'maze_html_images/AEF_exitleft.jpg',
                             'maze_html_images/AEF_exitright.jpg',
                             'maze_html_images/AE_exitback.jpg',
                             'maze_html_images/AE_exitleft.jpg',
                             'maze_html_images/AE_exitright.jpg',
                             'maze_html_images/AF.jpg',
                             'maze_html_images/AF_exitback.jpg',
                             'maze_html_images/AF_exitleft.jpg',
                             'maze_html_images/AF_exitright.jpg',
                             'maze_html_images/A_exitback.jpg',
                             'maze_html_images/A_exitleft.jpg',
                             'maze_html_images/A_exitright.jpg',
                             'maze_html_images/B.jpg',
                             'maze_html_images/BC.jpg',
                             'maze_html_images/BCD.jpg',
                             'maze_html_images/BCDE.jpg',
                             'maze_html_images/BCDEF.jpg',
                             'maze_html_images/BCDEF_exitback.jpg',
                             'maze_html_images/BCDEF_exitleft.jpg',
                             'maze_html_images/BCDEF_exitright.jpg',
                             'maze_html_images/BCDE_exitback.jpg',
                             'maze_html_images/BCDE_exitleft.jpg',
                             'maze_html_images/BCDE_exitright.jpg',
                             'maze_html_images/BCDF.jpg',
                             'maze_html_images/BCDF_exitback.jpg',
                             'maze_html_images/BCDF_exitleft.jpg',
                             'maze_html_images/BCDF_exitright.jpg',
                             'maze_html_images/BCD_exitback.jpg',
                             'maze_html_images/BCD_exitleft.jpg',
                             'maze_html_images/BCD_exitright.jpg',
                             'maze_html_images/BCE.jpg',
                             'maze_html_images/BCEF.jpg',
                             'maze_html_images/BCEF_exitback.jpg',
                             'maze_html_images/BCEF_exitleft.jpg',
                             'maze_html_images/BCEF_exitright.jpg',
                             'maze_html_images/BCE_exitback.jpg',
                             'maze_html_images/BCE_exitleft.jpg',
                             'maze_html_images/BCE_exitright.jpg',
                             'maze_html_images/BCF.jpg',
                             'maze_html_images/BCF_exitback.jpg',
                             'maze_html_images/BCF_exitleft.jpg',
                             'maze_html_images/BCF_exitright.jpg',
                             'maze_html_images/BC_exitback.jpg',
                             'maze_html_images/BC_exitleft.jpg',
                             'maze_html_images/BC_exitright.jpg',
                             'maze_html_images/BD.jpg',
                             'maze_html_images/BDE.jpg',
                             'maze_html_images/BDEF.jpg',
                             'maze_html_images/BDEF_exitback.jpg',
                             'maze_html_images/BDEF_exitleft.jpg',
                             'maze_html_images/BDEF_exitright.jpg',
                             'maze_html_images/BDE_exitback.jpg',
                             'maze_html_images/BDE_exitleft.jpg',
                             'maze_html_images/BDE_exitright.jpg',
                             'maze_html_images/BDF.jpg',
                             'maze_html_images/BDF_exitback.jpg',
                             'maze_html_images/BDF_exitleft.jpg',
                             'maze_html_images/BDF_exitright.jpg',
                             'maze_html_images/BD_exitback.jpg',
                             'maze_html_images/BD_exitleft.jpg',
                             'maze_html_images/BD_exitright.jpg',
                             'maze_html_images/BE.jpg',
                             'maze_html_images/BEF.jpg',
                             'maze_html_images/BEF_exitback.jpg',
                             'maze_html_images/BEF_exitleft.jpg',
                             'maze_html_images/BEF_exitright.jpg',
                             'maze_html_images/BE_exitback.jpg',
                             'maze_html_images/BE_exitleft.jpg',
                             'maze_html_images/BE_exitright.jpg',
                             'maze_html_images/BF.jpg',
                             'maze_html_images/BF_exitback.jpg',
                             'maze_html_images/BF_exitleft.jpg',
                             'maze_html_images/BF_exitright.jpg',
                             'maze_html_images/B_exitback.jpg',
                             'maze_html_images/B_exitleft.jpg',
                             'maze_html_images/B_exitright.jpg',
                             'maze_html_images/C.jpg',
                             'maze_html_images/CD.jpg',
                             'maze_html_images/CDE.jpg',
                             'maze_html_images/CDEF.jpg',
                             'maze_html_images/CDEF_exitback.jpg',
                             'maze_html_images/CDEF_exitleft.jpg',
                             'maze_html_images/CDEF_exitright.jpg',
                             'maze_html_images/CDE_exitback.jpg',
                             'maze_html_images/CDE_exitleft.jpg',
                             'maze_html_images/CDE_exitright.jpg',
                             'maze_html_images/CDF.jpg',
                             'maze_html_images/CDF_exitback.jpg',
                             'maze_html_images/CDF_exitleft.jpg',
                             'maze_html_images/CDF_exitright.jpg',
                             'maze_html_images/CD_exitback.jpg',
                             'maze_html_images/CD_exitleft.jpg',
                             'maze_html_images/CD_exitright.jpg',
                             'maze_html_images/CE.jpg',
                             'maze_html_images/CEF.jpg',
                             'maze_html_images/CEF_exitback.jpg',
                             'maze_html_images/CEF_exitleft.jpg',
                             'maze_html_images/CEF_exitright.jpg',
                             'maze_html_images/CE_exitback.jpg',
                             'maze_html_images/CE_exitleft.jpg',
                             'maze_html_images/CE_exitright.jpg',
                             'maze_html_images/CF.jpg',
                             'maze_html_images/CF_exitback.jpg',
                             'maze_html_images/CF_exitleft.jpg',
                             'maze_html_images/CF_exitright.jpg',
                             'maze_html_images/C_exitback.jpg',
                             'maze_html_images/C_exitleft.jpg',
                             'maze_html_images/C_exitright.jpg',
                             'maze_html_images/D.jpg',
                             'maze_html_images/DE.jpg',
                             'maze_html_images/DEF.jpg',
                             'maze_html_images/DEF_exitback.jpg',
                             'maze_html_images/DEF_exitleft.jpg',
                             'maze_html_images/DEF_exitright.jpg',
                             'maze_html_images/DE_exitback.jpg',
                             'maze_html_images/DE_exitleft.jpg',
                             'maze_html_images/DE_exitright.jpg',
                             'maze_html_images/DF.jpg',
                             'maze_html_images/DF_exitback.jpg',
                             'maze_html_images/DF_exitleft.jpg',
                             'maze_html_images/DF_exitright.jpg',
                             'maze_html_images/D_exitback.jpg',
                             'maze_html_images/D_exitleft.jpg',
                             'maze_html_images/D_exitright.jpg',
                             'maze_html_images/E.jpg',
                             'maze_html_images/EF.jpg',
                             'maze_html_images/EF_exitback.jpg',
                             'maze_html_images/EF_exitleft.jpg',
                             'maze_html_images/EF_exitright.jpg',
                             'maze_html_images/E_exitback.jpg',
                             'maze_html_images/E_exitleft.jpg',
                             'maze_html_images/E_exitright.jpg',
                             'maze_html_images/F.jpg',
                             'maze_html_images/forward.png',
                             'maze_html_images/F_exitback.jpg',
                             'maze_html_images/F_exitleft.jpg',
                             'maze_html_images/F_exitright.jpg',
                             'maze_html_images/OPEN.jpg',
                             'maze_html_images/OPEN_exitback.jpg',
                             'maze_html_images/OPEN_exitleft.jpg',
                             'maze_html_images/OPEN_exitright.jpg',
                             'maze_html_images/turn_left.png',
                             'maze_html_images/turn_right.png'],
    'periodictable.py': ['elements.csv'],
    'pygame_games/flippy.py': [   'pygame_games',
                                  'pygame_games/freesansbold.ttf',
                                  'pygame_games/flippyboard.png',
                                  'pygame_games/flippybackground.png'],
    'pygame_games/fourinarow.py': [   'pygame_games/4row_red.png',
                                      'pygame_games/4row_black.png',
                                      'pygame_games/4row_humanwinner.png',
                                      'pygame_games/4row_computerwinner.png',
                                      'pygame_games/4row_tie.png',
                                      'pygame_games/4row_arrow.png'],
    'pygame_games/gemgem.py': [   'pygame_games/freesansbold.ttf',
                                  'pygame_games/badswap.wav',
                                  'pygame_games/match0.wav',
                                  'pygame_games/match1.wav',
                                  'pygame_games/match2.wav',
                                  'pygame_games/match3.wav',
                                  'pygame_games/match4.wav',
                                  'pygame_games/match5.wav',
                                  'pygame_games/gem1.png',
                                  'pygame_games/gem2.png',
                                  'pygame_games/gem3.png',
                                  'pygame_games/gem4.png',
                                  'pygame_games/gem5.png',
                                  'pygame_games/gem6.png',
                                  'pygame_games/gem7.png'],
    'pygame_games/inkspill.py': [   'pygame_games/inkspilllogo.png',
                                    'pygame_games/inkspillspot.png',
                                    'pygame_games/inkspillsettings.png',
                                    'pygame_games/inkspillsettingsbutton.png',
                                    'pygame_games/inkspillresetbutton.png'],
    'pygame_games/pentomino.py': [   'pygame_games/freesansbold.ttf',
                                     'pygame_games/tetrisb.mid',
                                     'pygame_games/tetrisc.mid'],
    'pygame_games/simulate.py': [   'pygame_games/freesansbold.ttf',
                                    'pygame_games/beep1.ogg',
                                    'pygame_games/beep2.ogg',
                                    'pygame_games/beep3.ogg',
                                    'pygame_games/beep4.ogg'],
    'pygame_games/slidepuzzle.py': ['pygame_games/freesansbold.ttf'],
    'pygame_games/squirrel.py': [   'pygame_games/freesansbold.ttf',
                                    'pygame_games/gameicon.png',
                                    'pygame_games/squirrel.png',
                                    'pygame_games/grass1.png',
                                    'pygame_games/grass2.png',
                                    'pygame_games/grass3.png',
                                    'pygame_games/grass4.png'],
    'pygame_games/starpusher.py': [   'pygame_games/RedSelector.png',
                                      'pygame_games/Selector.png',
                                      'pygame_games/Star.png',
                                      'pygame_games/Wall_Block_Tall.png',
                                      'pygame_games/Wood_Block_Tall.png',
                                      'pygame_games/Plain_Block.png',
                                      'pygame_games/Grass_Block.png',
                                      'pygame_games/star_title.png',
                                      'pygame_games/star_solved.png',
                                      'pygame_games/princess.png',
                                      'pygame_games/boy.png',
                                      'pygame_games/catgirl.png',
                                      'pygame_games/horngirl.png',
                                      'pygame_games/pinkgirl.png',
                                      'pygame_games/Rock.png',
                                      'pygame_games/Tree_Short.png',
                                      'pygame_games/Tree_Tall.png',
                                      'pygame_games/Tree_Ugly.png',
                                      'pygame_games/starPusherLevels.txt'],
    'pygame_games/tetromino.py': [   'pygame_games/freesansbold.ttf',
                                     'pygame_games/tetrisb.mid',
                                     'pygame_games/tetrisc.mid'],
    'pygame_games/tetrominoforidiots.py': [   'pygame_games/freesansbold.ttf',
                                              'pygame_games/tetrisb.mid',
                                              'pygame_games/tetrisc.mid'],
    'pygame_games/wormy.py': ['pygame_games/freesansbold.ttf'],
    'rushhour.py': ['rushhourpuzzles.txt'],
    'sokoban.py': ['sokobanlevels.txt'],
    'stickyhands.py': ['stickyhandslevels.txt'],
    'sudoku.py': ['sudokupuzzles.txt']}


import sys, os, subprocess, zlib, zipfile, webbrowser

from tkinter import *
from tkinter import font
from tkinter import ttk

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))

# Sort the programs in "pygame_games/" without considering the folder name:
PROGRAMS.sort(key=lambda x: os.path.basename(x['filename']))

# TODO - add code that checks for a corrupted _originalFiles.zip file. Disable the "undo changes" button in that case.

# Check for any missing files and reload them from the _originalFiles.zip file:
for program in PROGRAMS:
    if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, program['filename'])):
        # Restore the file from the original one in the _originalFiles.zip backup.
        originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
        originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)

# TODO - unpack support files if they're missing
#for supportFiles in SUPPORT_FILES.values():
#    for supportFile in supportFiles:
#        if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, supportFile)):
#            # Restore the file from the original one in the _originalFiles.zip backup.
#            originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
#            originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)


def _executable_exists(name):
    # Find out if an executable program named `name` is reachable:
    return subprocess.call(['which', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def programSelect(*args):
    global CURRENT_SELECTED_INDEX, programListbox, descTextarea, undoChangesBtnSV, undoChangesButton
    # If, for some reason, nothing is currently selected in the listbox of programs, do nothing:
    if len(programListbox.curselection()) == 0:
        return

    i = CURRENT_SELECTED_INDEX = programListbox.curselection()[0]

    descTextarea.configure(state='normal')
    descTextarea.delete('1.0', END)
    filename = os.path.join(FOLDER_OF_THIS_FILE, PROGRAMS[i]['filename'])

    # Set the text in the text box to the program name and description:
    programNameInListbox = PROGRAMS[i]['name']
    if 'pygame_games/' in programNameInListbox:
        programNameInListbox = programNameInListbox[len('pygame_games/'):]
    text = programNameInListbox + '\n\n' + PROGRAMS[i]['desc'] + '\n'
    descTextarea.insert(INSERT, text)
    descTextarea.configure(state='disabled')

    # Get the adler32 hash of the .py file:
    fileObj = open(filename, encoding='utf-8')
    fileHash = zlib.adler32(fileObj.read().encode('utf-8'))
    fileObj.close()

    # Check if the .py file on disk is different from the original file (based on the hash):
    sourceFileIsChanged = fileHash != PROGRAMS[i]['hash']
    if sourceFileIsChanged:
        undoChangesBtnSV.set('Undo Changes')
        undoChangesButton.config(state='normal')
    else:
        undoChangesBtnSV.set('File is Unchanged')
        undoChangesButton.config(state='disabled')


def runClick(*args):
    i = CURRENT_SELECTED_INDEX
    filename = os.path.join(FOLDER_OF_THIS_FILE, PROGRAMS[i]['filename'])
    TERMINAL_OPENER_FILENAME = os.path.join(FOLDER_OF_THIS_FILE, '__terminalopener__.py')
    CRASH_DETECTOR_FILENAME = os.path.join(FOLDER_OF_THIS_FILE, '__crashdetector__.py')

    # Figure out which program to run to open a new terminal window and then run the .py file:
    if sys.platform == 'win32':
        # 'start cmd' opens a new Command Prompt terminal window
        # '/K' tells the Command Prompt to run this command:
        # We want to run the same Python executable that is running this __init__.py script.
        # That Python should run __crashdetector__.py, with __version__ and filename as arguments
        # Crash detector will run filename as a Python script, and __version__ is used in the debug output if that program crashes.
        os.system('start cmd /K ' + sys.executable + ' ' + CRASH_DETECTOR_FILENAME + ' ' + __version__ + ' ' + filename)
    elif sys.platform == 'darwin':
        os.system('''osascript -e 'tell application "Terminal" to do script "''' + sys.executable + ' ' + CRASH_DETECTOR_FILENAME + ' ' + __version__ + ' ' + filename + '"' + "'")
    elif _executable_exists('gnome-terminal'):
        # gnome-terminal is used on Ubuntu Linux:
        subprocess.call(['gnome-terminal', '--', sys.executable, TERMINAL_OPENER_FILENAME, __version__, filename])
    elif _executable_exists('lxterminal'):
        # LXTerminal is used on Raspberry Pis:
        subprocess.call(['lxterminal', '-e', sys.executable, TERMINAL_OPENER_FILENAME, __version__, filename])


def viewSourceClick(*args):
    i = CURRENT_SELECTED_INDEX
    filename = os.path.join(FOLDER_OF_THIS_FILE, PROGRAMS[i]['filename'])

    # Figure out which program to run to open the .py file:
    if sys.platform == 'win32':
        os.system('start ' + filename)
    elif sys.platform == 'darwin':
        os.system('open ' + filename)
    elif _executable_exists('xdg-open'):
        # LXTerminal is used on Raspberry Pis, though this closes the window as soon as the Python program quits:
        os.system('xdg-open ' + filename)
    elif _executable_exists('see'):
        os.system('see ' + filename)


def undoChangesClick(*args):
    global undoChangesBtnSV, undoChangesButton
    i = CURRENT_SELECTED_INDEX

    # Restore the file from the original one in the _originalFiles.zip backup.
    originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
    originalFilesZipFile.extract(PROGRAMS[i]['filename'], FOLDER_OF_THIS_FILE)

    # Disable the undo button now that there are no changes.
    undoChangesBtnSV.set('File is Unchanged')
    undoChangesButton.config(state='disabled')


def openInventWithPythonWebpage(*args):
    webbrowser.open('https://inventwithpython.com')


def openFolderClick(*args):
    i = CURRENT_SELECTED_INDEX
    fullFilePath = os.path.join(FOLDER_OF_THIS_FILE, PROGRAMS[i]['filename'])

    if sys.platform == 'win32':
        os.system('explorer /select,"' + fullFilePath + '"') # TODO - this doesn't open the right folder
    elif sys.platform == 'darwin':
        subprocess.Popen(["open", "-R", fullFilePath])
    elif _executable_exists('nautilus'):
        subprocess.Popen(['nautilus', '-s', fullFilePath])
    elif _executable_exists('pcmanfm'):
        subprocess.Popen(['pcmanfm', FOLDER_OF_THIS_FILE])
    else:
        pass # TODO - Figure out support for other file managers (dolphin, konqueror, etc.)


def quitLauncher(*args):
    global root
    root.destroy()
    sys.exit()


def main():
    global root, descTextarea, programListbox, undoChangesBtnSV, undoChangesButton
    root = Tk()
    root.title('Python Games by Example ' + __version__)

    mainframe = ttk.Frame(root, padding='5 5 12 12')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    scrollbar = Scrollbar(mainframe, orient="vertical")

    # Remove the "pygame_games/" part of the filename for the purposes of listing games in the listbox.
    programNamesInListbox = [d['filename'][len('pygame_games/'):] if 'pygame_games/' in d['filename'] else d['filename'] for d in PROGRAMS]
    #programNamesInListbox.sort() # Re-alphabetize them.

    filenameSV = StringVar(value=programNamesInListbox)
    programListbox = Listbox(mainframe, listvariable=filenameSV, yscrollcommand=scrollbar.set)
    programListbox.grid(column=0, row=0, sticky=(N, S, E, W))
    programListbox.bind('<<ListboxSelect>>', programSelect)

    scrollbar.config(command=programListbox.yview)
    scrollbar.grid(column=1, row=0, sticky=(N, S, E, W))

    openFolderButton = ttk.Button(mainframe, text='Open Folder', command=openFolderClick)
    openFolderButton.grid(column=0, row=1, stick=(N, S, E, W))

    descTextarea = Text(mainframe, width=50, height=6)
    descTextarea.grid(column=2, row=0, columnspan=3, sticky=(N, S, E, W))
    descTextarea.configure(font=('Arial', 12))
    descTextarea.configure(state='disabled')

    runButton = ttk.Button(mainframe, text='Run', command=runClick)
    runButton.grid(column=2, row=1, sticky=(E, W))

    viewSourceButton = ttk.Button(mainframe, text='View Source', command=viewSourceClick)
    viewSourceButton.grid(column=3, row=1, sticky=(E, W))

    undoChangesBtnSV = StringVar(value='Undo Changes')
    undoChangesButton = ttk.Button(mainframe, textvariable=undoChangesBtnSV, command=undoChangesClick)
    undoChangesButton.grid(column=4, row=1, sticky=(E, W))

    blueUnderlineFont = font.Font(family='Helvetica', size=12, underline=True)
    linkLabel = ttk.Label(mainframe, text='Learn to program at https://inventwithpython.com', font=blueUnderlineFont)
    linkLabel.configure(foreground='blue', font=blueUnderlineFont)
    linkLabel.grid(column=0, row=2, columnspan=4, sticky=(E, W))
    linkLabel.bind("<Button-1>", openInventWithPythonWebpage)

    # Add the padding around the widgets:
    for child in mainframe.winfo_children():
        if child in (programListbox, scrollbar):
            child.grid_configure(padx=0, pady=5)
        elif child in (linkLabel,):
            child.grid_configure(padx=5, pady=0)
        else:
            child.grid_configure(padx=5, pady=5)

    # Select the first item in the list box by default:
    programListbox.focus()
    programListbox.select_set(0)
    programListbox.event_generate("<<ListboxSelect>>")

    root.bind('<Escape>', quitLauncher) # Bind Esc key to quit the program.
    root.mainloop()


if __name__ == '__main__':
    main()
