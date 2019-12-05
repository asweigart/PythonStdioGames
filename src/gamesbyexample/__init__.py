# Games By Example
# By Al Sweigart al@inventwithpython.com

__version__ = '0.1.2'

# TODO - check if the support files have been changed and let the user undo changes.


PROGRAMS = [
    {   'desc': 'A time-based quiz game to see how fast you can alphabetize letters.',
        'filename': 'alphabetizequiz.py',
        'hash': 491498882,
        'name': 'Alphabetize Quiz'},
    {   'desc': 'A time-based quiz game to see how fast you can alphabetize words.',
        'filename': 'alphabetizewordquiz.py',
        'hash': 2736248730,
        'name': 'Alphabetize Word Quiz'},
    {   'desc': 'An analog clock animation. Press Ctrl-C to stop.',
        'filename': 'analogclock.py',
        'hash': 2033121040,
        'name': 'Analog Clock'},
    {'desc': 'A deductive logic game.', 'filename': 'bagels.py', 'hash': 1027777705, 'name': 'Bagels'},
    {   'desc': 'Explore the mathematics of the "Birthday Paradox". More info at '
                'https://en.wikipedia.org/wiki/Birthday_problem',
        'filename': 'birthdayparadox.py',
        'hash': 58703664,
        'name': 'Birthday Paradox Simulation'},
    {   'desc': 'A card game also known as 21. More info at: https://en.wikipedia.org/wiki/Blackjack',
        'filename': 'blackjack.py',
        'hash': 849137676,
        'name': 'Blackjack'},
    {   'desc': 'A bouncing ball animation. Press Ctrl-C to stop.',
        'filename': 'bouncingDots.py',
        'hash': 3515347367,
        'name': 'Bouncing Ball'},
    {   'desc': 'A bouncing line animation. Press Ctrl-C to stop.',
        'filename': 'bouncingLines.py',
        'hash': 200398130,
        'name': 'Bouncing Lines'},
    {   'desc': 'Create monthly calendars, saved to a text file and fit for printing.',
        'filename': 'calendarmaker.py',
        'hash': 1645987771,
        'name': 'Calendar Maker'},
    {   'desc': 'Checkers, but you can move 3 random checkers per turn. These checkers are randomly decided, and can '
                "be the player's own checkers or their opponents', but you can't move your opponents' promoted "
                'checkers. In this version, capturing is not mandatory.',
        'filename': 'chancecheckers.py',
        'hash': 1612272488,
        'name': 'Chance Checkers'},
    {   'desc': 'Try to get the robots to crash into each other.',
        'filename': 'chase.py',
        'hash': 1462880234,
        'name': 'Daleks'},
    {   'desc': 'The classic checkers board game. In this version, capturing is not mandatory.',
        'filename': 'checkers.py',
        'hash': 179609454,
        'name': 'Checkers'},
    {   'desc': 'A dangerously delicious logic game. Inspired by a Frederik Schuh and David Gale puzzle, published by '
                'Martin Gardner in Scientific American (January 1973) More info at: '
                'https://en.wikipedia.org/wiki/Chomp',
        'filename': 'chomp.py',
        'hash': 366969446,
        'name': 'Chomp'},
    {   'desc': 'A clickbait headline generator for your soulless content farm.',
        'filename': 'clickbait.py',
        'hash': 643016827,
        'name': 'Clickbait Headline Generator'},
    {   'desc': 'Simulate a large number of coin flips.',
        'filename': 'coinflipsimulator.py',
        'hash': 3815118907,
        'name': 'Coin Flip Simulator'},
    {   'desc': 'A board game to get four tiles in a row.',
        'filename': 'connectfour.py',
        'hash': 1282552112,
        'name': 'Connect Four'},
    {   'desc': 'The classic cellular automata simulation. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life',
        'filename': 'conwaysgameoflife1.py',
        'hash': 1840580892,
        'name': "Conway's Game of Life"},
    {   'desc': 'The classic cellular automata simulation. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life',
        'filename': 'conwaysgameoflife2.py',
        'hash': 1439734991,
        'name': "Conway's Game of Life (Terminal)"},
    {   'desc': 'Show a countdown timer animation using a seven-segment display. Press Ctrl-C to stop. More info at '
                'https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.',
        'filename': 'countdown.py',
        'hash': 4089371915,
        'name': 'Countdown'},
    {   'desc': 'Prints out a random, diagonal maze. Inspired by the 10 PRINT CHR$(205.5+RND(1)); : GOTO 10 program.',
        'filename': 'diagonalmaze.py',
        'hash': 4028274581,
        'name': 'Diagonal Maze'},
    {   'desc': 'Simulates dice rolls using the Dungeons & Dragons notation.',
        'filename': 'diceroller.py',
        'hash': 800095226,
        'name': 'Dice Roller'},
    {   'desc': 'Display a digital clock of the current time with a seven-segment display. Press Ctrl-C to stop. More '
                'info at https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.',
        'filename': 'digitalclock.py',
        'hash': 499931592,
        'name': 'Digital Clock'},
    {   'desc': 'A simple animation of a DNA double-helix. Press Ctrl-C to stop. Thanks to matoken for inspiration: '
                'https://asciinema.org/a/155441',
        'filename': 'dna.py',
        'hash': 3925144257,
        'name': 'DNA'},
    {   'desc': 'An elimination game for multiple players. Press Ctrl-C to stop. More info at '
                'https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe More info at '
                'https://en.wikipedia.org/wiki/Josephus_problem',
        'filename': 'eenymeeny.py',
        'hash': 3815271138,
        'name': 'Eeny-Meeny-Miny-Moe'},
    {   'desc': 'Draw a trailing line on the screen.',
        'filename': 'etchasketch.py',
        'hash': 2872091257,
        'name': 'Etch a Sketch'},
    {   'desc': 'Find all the factors of a number.',
        'filename': 'factorfinder.py',
        'hash': 1692605437,
        'name': 'Factorization'},
    {   'desc': 'A beautiful animation of fireflies. Press Ctrl-C to stop.',
        'filename': 'fireflies.py',
        'hash': 2485316294,
        'name': 'Fireflies'},
    {   'desc': 'A peaceful animation of a fish tank. Press Ctrl-C to stop.',
        'filename': 'fishtank.py',
        'hash': 1893647541,
        'name': 'Fish Tank'},
    {   'desc': 'Calculates the answers for the fizz buzz programming problem.',
        'filename': 'fizzbuzz.py',
        'hash': 4039783006,
        'name': 'FizzBuzz Calculation'},
    {   'desc': 'A number game where you also race against the clock.',
        'filename': 'fizzbuzzgame.py',
        'hash': 1259487915,
        'name': 'FizzBuzz Game'},
    {   'desc': 'An example of a "flood fill" algorithm. This is a basic demo of both the recursive and iterative '
                'floodfill algorithms. This algorithm is commonly used in "fill tools" in graphics programs like MS '
                'Paint or Photoshop. This algorithm is also used in the floodit.py game.',
        'filename': 'floodfill.py',
        'hash': 1141200114,
        'name': 'Flood Fill'},
    {   'desc': 'A colorful game where you try to fill the board with a single color.',
        'filename': 'floodit.py',
        'hash': 3502757288,
        'name': 'Flood It!'},
    {   'desc': "A simulation of fires spreading in a growing forest. Press Ctrl-C to stop. Inspired by Nicky Case's "
                'Emoji Sim http://ncase.me/simulating/model/',
        'filename': 'forestfiresim.py',
        'hash': 2520944581,
        'name': 'Forest Fire Sim'},
    {   'desc': 'Draws nonuniform fractal trees with turtle graphics.',
        'filename': 'fractalnonuniformtree.py',
        'hash': 3841218830,
        'name': 'Nonuniform Fractal Tree Drawer'},
    {   'desc': 'Draws fractal trees with turtle graphics.',
        'filename': 'fractaltree.py',
        'hash': 661548038,
        'name': 'Fractal Tree Drawer'},
    {   'desc': "A sliding tile game to combine exponentially-increasing numbers. Inspired by Gabriele Cirulli's 2048, "
                "which is a clone of Veewo Studios' 1024, which in turn is a clone of the Threes! game. More info at "
                'https://en.wikipedia.org/wiki/2048_(video_game)',
        'filename': 'game2048.py',
        'hash': 1028413528,
        'name': '2048 Game'},
    {   'desc': 'While given hints, try to guess the secret number.',
        'filename': 'guess.py',
        'hash': 1015842893,
        'name': 'Guess the Number'},
    {   'desc': 'A French variant of Hangman with different graphics. Ooh la la!',
        'filename': 'guillotine.py',
        'hash': 1695305967,
        'name': 'Guillotine'},
    {   'desc': 'The hacking mini-game from "Fallout 3".',
        'filename': 'hacking.py',
        'hash': 1817878266,
        'name': 'Hacking'},
    {   'desc': 'The classic game Hamurabi.bas by Doug Dyment, popularized by David Ahl.',
        'filename': 'hammurabi.py',
        'hash': 4170522529,
        'name': 'Hammurabi'},
    {   'desc': 'A program for making silly pluralizations. Press Ctrl-C to stop.',
        'filename': 'hamsburger.py',
        'hash': 592436006,
        'name': 'Hamsburger'},
    {'desc': 'A word-guessing game.', 'filename': 'hangman.py', 'hash': 3995095403, 'name': 'Hangman'},
    {   'desc': 'A completely unfair word-guessing game. (This is a joke program.)',
        'filename': 'hangmanunfair.py',
        'hash': 2932603560,
        'name': 'Hangman with Random Letters'},
    {   'desc': 'Play tic tac toe against the computer. Every possible move has been hard-coded into this program. The '
                "program is 5700 lines long. This is a joke program, don't actually write code like this.",
        'filename': 'hardcodedtictactoe.py',
        'hash': 1563327787,
        'name': 'Hard-coded Tic Tac Toe'},
    {   'desc': 'Draws the Hilbert Curve fractal with turtle graphics. More info at: '
                'https://en.wikipedia.org/wiki/hilbertCurve Good videos on space-filling curves: '
                'https://youtu.be/RU0wScIj36o and https://youtu.be/3s7h2MHQtxc',
        'filename': 'hilbertcurve.py',
        'hash': 3385678044,
        'name': 'Hilbert Curve'},
    {   'desc': 'An animation of an hour glass filled with falling sand. Press Ctrl-C to stop.',
        'filename': 'hourglass.py',
        'hash': 2081844178,
        'name': 'Hour Glass Animation'},
    {   'desc': 'How to keep an idiot busy for hours. (This is a joke program.)',
        'filename': 'idiot.py',
        'hash': 1388628505,
        'name': 'Idiot'},
    {   'desc': 'A mystery game of intrigue and a missing cat. Inspired by Homestar Runner\'s "Where\'s an Egg?" game',
        'filename': 'jaccuse.py',
        'hash': 2286593251,
        'name': "J'ACCUSE!"},
    {   'desc': 'Draws a Koch snowflake fractal with turtle graphics.',
        'filename': 'kochsnowflake.py',
        'hash': 989009564,
        'name': 'Koch Snowflake'},
    {   'desc': 'A cellular automata animation. Press Ctrl-C to stop. More info: '
                'https://en.wikipedia.org/wiki/Langton%27s_ant',
        'filename': 'langtonsant.py',
        'hash': 1040545392,
        'name': "Langton's Ant"},
    {   'desc': 'Watch grass get cut and grow again. Press Ctrl-C to stop. Inspired by Tondeuse by Jules Villard, '
                'https://asciinema.org/a/21743 https://bitbucket.org/jvillard/tondeuse/src/default/',
        'filename': 'lawnmower.py',
        'hash': 2454478460,
        'name': 'Lawnmower'},
    {   'desc': 'Translates English messages into l33t5p34]<.',
        'filename': 'leetspeak.py',
        'hash': 2489424941,
        'name': 'Leetspeak'},
    {   'desc': 'The mathematics behind credit card numbers. More info at: '
                'https://en.wikipedia.org/wiki/Luhn_algorithm More info at: https://youtu.be/Erp8IAUouus',
        'filename': 'luhn.py',
        'hash': 3623937696,
        'name': 'Luhn Checksum Algorithm'},
    {   'desc': 'Ask a question about your future.',
        'filename': 'magic8ball.py',
        'hash': 4220249488,
        'name': 'Magic Eight Ball'},
    {   'desc': 'Place numbers in a hexagon so each row adds up to 38. More info at '
                'https://en.wikipedia.org/wiki/Magic_hexagon More info at https://www.youtube.com/watch?v=ZkVSRwFWjy0',
        'filename': 'magichexagon.py',
        'hash': 1286388736,
        'name': 'Magic Hexagon'},
    {   'desc': 'The ancient seed-sowing board game. Rules at http://www.mancalarules.com/ More info at '
                'https://en.wikipedia.org/wiki/Mancala',
        'filename': 'mancala.py',
        'hash': 358147140,
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
        'hash': 3177085905,
        'name': 'Maze Runner'},
    {   'desc': 'Move around a maze and try to escape... in 3D!',
        'filename': 'mazerunner3d.py',
        'hash': 2632678560,
        'name': 'Maze 3D'},
    {   'desc': 'Move around a maze and try to escape... in 3D and IN YOUR WEB BROWSER!',
        'filename': 'mazerunnerhtml.py',
        'hash': 1817226516,
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
        'hash': 737764565,
        'name': 'Mondrian Art Generator'},
    {   'desc': 'A simulation of the Monty Hall game show problem. More info at '
                'https://en.wikipedia.org/wiki/Monty_Hall_problem',
        'filename': 'montyhall.py',
        'hash': 3885147591,
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
        'hash': 425581469,
        'name': 'Multiplicative Persistence'},
    {   'desc': 'Print the full lyrics to one of the most longest songs ever! Press Ctrl-C to stop.',
        'filename': 'ninetyninebottles.py',
        'hash': 1906546982,
        'name': '99 Bottles of Beer on the Wall'},
    {   'desc': 'A single-player, peg-jumping game to eliminate all the pegs. More info at '
                'https://en.wikipedia.org/wiki/Peg_solitaire',
        'filename': 'pegsolitaire.py',
        'hash': 3170911140,
        'name': 'Peg Solitaire'},
    {   'desc': 'Displays atomic information for all the elements.',
        'filename': 'periodictable.py',
        'hash': 226631739,
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
        'hash': 3892358981,
        'name': 'Rainbow'},
    {   'desc': 'Shows a simple squiggle rainbow animation. Press Ctrl-C to stop.',
        'filename': 'rainbow2.py',
        'hash': 1981907040,
        'name': 'Rainbow 2'},
    {   'desc': 'Generate splatter-art with the "random walk" algorithm. Press Ctrl-C to stop. More info at: '
                'https://en.wikipedia.org/wiki/Random_walk',
        'filename': 'randomwalk.py',
        'hash': 130285096,
        'name': 'Random Walk'},
    {   'desc': 'A tile flipping game, also called reversi. More info https://en.wikipedia.org/wiki/Reversi',
        'filename': 'reversi.py',
        'hash': 122844257,
        'name': 'Reversi'},
    {   'desc': 'A hand game of luck.',
        'filename': 'rockpaperscissors.py',
        'hash': 1129567719,
        'name': 'Rock-Paper-Scissors'},
    {   'desc': 'A hand game of luck, except you cannot lose.',
        'filename': 'rockpaperscissorsalwayswin.py',
        'hash': 3122774091,
        'name': 'Rock-Paper-Scissors (Always Win)'},
    {   'desc': 'The simplest cipher for encrypting and decrypting text. More info at '
                'https://en.wikipedia.org/wiki/ROT13',
        'filename': 'rot13.py',
        'hash': 2777215909,
        'name': 'ROT13 Cipher'},
    {   'desc': 'A rotating cube animation. Press Ctrl-C to stop.',
        'filename': 'rotatingcube.py',
        'hash': 2404400610,
        'name': 'Rotating Cube'},
    {   'desc': 'A rotating cube animation. Press Ctrl-C to stop.',
        'filename': 'rotatingcubebext.py',
        'hash': 2279078710,
        'name': 'Rotating Cube (Bext Version)'},
    {   'desc': 'A rotating sphere animation. Press Ctrl-C to stop.',
        'filename': 'rotatingsphere.py',
        'hash': 4045695330,
        'name': 'Rotating Sphere'},
    {   'desc': 'A sliding tile puzzle game to move cars out of the way. Original game by Nob Yoshihagara More info at '
                'https://www.michaelfogleman.com/rush/',
        'filename': 'rushhour.py',
        'hash': 1278069698,
        'name': 'Rush Hour'},
    {   'desc': 'A falling sand animation. Inspired by https://asciinema.org/a/6515',
        'filename': 'sandfall.py',
        'hash': 2786701044,
        'name': 'Sand Fall'},
    {   'desc': 'A falling sand animation. Inspired by https://asciinema.org/a/6515',
        'filename': 'sandfallbext.py',
        'hash': 75371458,
        'name': 'Sand Fall (Bext Version)'},
    {   'desc': 'A seven-segment display module. More info at https://en.wikipedia.org/wiki/Seven-segment_display',
        'filename': 'sevseg.py',
        'hash': 351868863,
        'name': 'Sevseg'},
    {'desc': 'A random gambling game.', 'filename': 'shellgame.py', 'hash': 2457239818, 'name': 'Shell Game'},
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
    {'desc': 'The classic crate-pushing game.', 'filename': 'sokoban.py', 'hash': 3750242081, 'name': 'Sokoban clone'},
    {   'desc': 'Try to locate treasure chests hidden under the waves.',
        'filename': 'sonar.py',
        'hash': 2882284494,
        'name': 'Sonar Treasure Hunt'},
    {   'desc': 'A simulation of a Japanese abacus calculator tool. More info at: '
                'https://en.wikipedia.org/wiki/Soroban',
        'filename': 'soroban.py',
        'hash': 1348201962,
        'name': 'Soroban'},
    {'desc': 'Draws a simple square spiral.', 'filename': 'spiral.py', 'hash': 3378282052, 'name': 'Spiral'},
    {   'desc': 'Translates English messages into sPOnGEtExT.',
        'filename': 'spongetext.py',
        'hash': 1477272675,
        'name': 'sPoNgEtExT'},
    {   'desc': 'A jewel-stealing, movement puzzle game.',
        'filename': 'stickyhands.py',
        'hash': 960739011,
        'name': 'Sticky Hands'},
    {   'desc': 'Find the Queen of Hearts after cards have been swapped around. (In the real-life version, the scammer '
                'palms the Queen of Hearts so you always lose.) More info at '
                'https://en.wikipedia.org/wiki/Three-card_Monte',
        'filename': 'threecardmonte.py',
        'hash': 178106625,
        'name': 'Three-Card Monte'},
    {'desc': 'The classic board game.', 'filename': 'tictactoe.py', 'hash': 1030081701, 'name': 'Tic Tac Toe'},
    {   'desc': 'The classic board game. (Object-oriented programming version.)',
        'filename': 'tictactoeoop.py',
        'hash': 1780785172,
        'name': 'Tic Tac Toe (OOP)'},
    {   'desc': 'A puzzle where you must move the discs of one tower to another tower. More info at '
                'https://en.wikipedia.org/wiki/Tower_of_Hanoi',
        'filename': 'towersofhanoi.py',
        'hash': 806668752,
        'name': 'Towers of Hanoi puzzle'},
    {   'desc': 'The Ulam spiral is a mysterious mathematics pattern for prime numbers with turtle graphics. More info '
                'at https://en.wikipedia.org/wiki/Ulam_spiral',
        'filename': 'ulamspiral.py',
        'hash': 4022741212,
        'name': 'Ulam Spiral'},
    {   'desc': 'A water pouring puzzle. More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle',
        'filename': 'waterbucket.py',
        'hash': 3830377669,
        'name': 'Water Bucket Puzzle'},
    {   'desc': 'A water pouring puzzle. (Object-oriented programming style.) More info: '
                'https://en.wikipedia.org/wiki/Water_pouring_puzzle',
        'filename': 'waterbucketoop.py',
        'hash': 2504149627,
        'name': 'Water Bucket Puzzle (OOP)'},
    {   'desc': 'A simple zig zag animation. Press Ctrl-C to stop.',
        'filename': 'zigzag.py',
        'hash': 3543395541,
        'name': 'Zigzag'}]


import time, sys, os, subprocess, zlib, zipfile, webbrowser

from tkinter import *
from tkinter import font
from tkinter import ttk

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))


# TODO - add code that checks for a corrupted _originalFiles.zip file. Disable the "undo changes" button in that case.

# Check for any missing files and reload them from the _originalFiles.zip file:
for program in PROGRAMS:
    if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, program['filename'])):
        # Restore the file from the original one in the _originalFiles.zip backup.
        originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
        originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)


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
    text = PROGRAMS[i]['name'] + '\n\n' + PROGRAMS[i]['desc'] + '\n'
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

    filenameSV = StringVar(value=[d['filename'] for d in PROGRAMS])
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
