# PythonStdioGames

A collection of Python 3 source code for simple, text-based games & simulations to use as example programs.

INSTALL: `pip install --user gamesbyexample`

(Use `pip3` on macOS and Linux.)

RUN LAUNCHER: `python -m gamesbyexample`

I'm not accepting pull requests currently, but feel free to leave comments or send suggestions to al@inventwithpython.com

About this Collection
=====================

After beginners learn the syntax of Python and basic programming concepts (loops, branching, functions, etc.) they often hit a dead-end: "How do I become better at programming?" At this point, people will tell them to work on their own practice projects (which leaves them without guidance on what to make and how to make it) or to contribute to open source projects (which can be difficult to find, understand its code base, and get guidance on how to contribute).

What helped me learn to code was finding small projects whose source code I copied and then made small adjustments to. This gave me insight on how loops, branching, and functions combined together into actual programs.

To help others down the same path, I'm creating a collection of example programs aimed at being easy to copy and understand by beginners. These programs (mostly games) have the following constraints:

* They're short, with a limit of 256 lines of code. *This makes them easy to read and understand in one sitting. The shorter the better. The "256" number was arbitrarily selected, but this also means programs will fit on 4 or 5 printed pages.*
* They fit into a single source code file and have no installer. *This makes these games trivial to share by copy/pasting code to a pastebin site. Data/image/save files can be used, but the source should link to some examples in their comments.*
* They only use the Python standard library. *Fewer things to install means wider compatibility and less chance of failing during environment setup.*
* They only use stdio text; `print()` and `input()` in Python. *The output being in the same text medium as the text source code makes it less abstract, and easier to see the cause-effect relationship between code and output. This means there's no graphics or mouse input, but makes it simple to port these programs to other languages since they all support stdio text.*
* They're necessarily turn-based. *Relying on `input()` means the program must wait for the user to enter text, but this means we can't have real-time programs that respond to single key-presses.*
* They're well commented. *Comments should be aimed at beginners and will be more verbose. The 256-line limit includes comments and whitespace. If the program is too long to include abundant comments and sensible whitespace, the program should be simplified, not the comments.*
* They use as few programming concepts as possible. *If classes, list comprehensions, recursion, aren't necessary for the program, then they are't used.*
* **Elegant** and **efficient** code is worthless next to code that is **easy to understand** and **readable**. *These programs are for education, not production. Standard best practices, like not using global variables, can be ignored to make it easier to understand.*
* They do input validation and are bug free. *It should be impossible to crash a program with bad input or an edge case.*
* All functions have docstrings. *This is good documentation practice, but also enables the `help()` function to work in the interactive shell.*


Additional Guidelines
=====================

Additional guidelines include:

* Don't use f-strings. Raspberry Pis as of 2019 have Python 3.5 installed, and f-strings only came about in 3.6. One guideline for these programs is to be as widely compatible as possible.
* Some of these programs use the `bext` module, which adds curses-like features like color, clearing the screen, and moving the cursor
* Include a link to a run-through of the program on https://pythontutor.com so that the student can see how the program runs.
* Longer, more descriptive variable names are better than shorter ones. Avoid using single-letter variable names except for `i` and `j`, or `x` and `y`.
* Have comments marked as `# EXPERIMENT!` that describe minor changes that they can make (increasing health, changing difficulty, etc.)
* Use jsdifflib to create online diffs. *This is an easy way for students to find their own typos when copying the code. An example is here: https://inventwithpython.com/invent4thed/diff/*
* Use `assert` statements to catch common typos the student makes when typing in the code, especially for constants that they may modify.
* Use Python 3. *The only time Python 2 is appropriate to use is when there's a large existing codebase. But this is for new programmers working on greenfield projects.*
* Stick to characters in WGL4 character repertoire, which is basically CP 1252, code pages for Cyrillic/Greek/Turkish/Baltic characters, and the MS-DOS era CP437 "extended ASCII" encoding. *Windows' command line is the limiting factor here; it can't display all UTF-8 characters.*
* The source code must be typeable. *Don't put box-drawing or extended ascii characters directly into the source code, but rather make chr() calls instead to acquire these characters.*
* Time can be a factor, even if the programs aren't real-time. *You can check for time or add pauses in between calls to `input()`, but note that you'll never be able to interrupt when the user is typing.*
* The `pyperclip` module can be used to interact with the clipboard. *Large amounts of text can be input-ed into or output-ed from the program using the clipboard.*
* I use %s string interpolation instead of f-strings. *I love f-strings, but they were only introduced in Python 3.6 and I don't want to limit the versions that these programs are compatible with.*
* For all dictionaries, I have a short comment explaining what types the keys and values are. *For example, # Keys=places, values=strings of the suspect & item there.*
* Use the "DOS box-drawing" characters to draw complicated board games. *Though sticking to +, -, and | for lines is good too since it's simpler.*
* Player vs player games can often be simpler and shorter than player vs computer games. *This necessarily means that multiplayer games must be "perfect information" games since both players can view the screen.*
* Don't modify mutable objects (e.g. lists) in functions to pass information into/out of the function; only use parameters and return values. *This can make your program seem magical to someone not familiar with the Python Data Model.*
* Avoid insulting the player when they lose. *This is something I learned from instructing programming classes for kids. They respond poorly to messages like, "Game Over, Dummy!" even if they seem innocuous to adults.*

After making several of these programs, I've notice various "categories" of program complexity. Programs can be of zero or more of these categories:

* Absolute beginner level. *No functions, no nested data structures, avoid nested loops. Just uses simple branching and loops.*
* Choose-your-own-adventure level. *Programs don't model things with data structures, but rather mostly use flow control.*
* STDIO-only. *You can't undo things that have been previously printed (aside from "printing" backspace characters to erase characters on the current line). The output is like an append-only log file.*
* Curses-like. *Requires the `bext` module, but can clear/refresh the screen, draw at arbitrary places on the screen in color, etc.*
* Modify source code to run. *Instead of getting input from `input()`, the user edits variables at the top of the file to change the settings in the program.*


Additional modules I recommend using:

* `bext` for colorful text and controlling the positioning of the text cursor.
* `blessings` for a better version of curses.
* `pyperclip` for copying/psating text with the clipboard.
* `playsound` for playing sound files.
* `pyttsx3` for text to speech.
* `pytextcavas` for 2D strings you can draw on
* `pyrect` for rectangle data structure
* `pybresenham` for various line-drawing functions


Completed Programs in This Collection
=====================================

*Alphabetize Quiz* - A time-based quiz game to see how fast you can alphabetize letters.

*Alphabetize Word Quiz* - A time-based quiz game to see how fast you can alphabetize words.

*Analog Clock* - An analog clock animation. Press Ctrl-C to stop.

*Bagels* - A deductive logic game where you must guess a number based on clues.

*Birthday Paradox Simulation* - Explore the mathematics of the "Birthday Paradox". More info at https://en.wikipedia.org/wiki/Birthday_problem

*Blackjack* - A card game also known as 21. More info at: https://en.wikipedia.org/wiki/Blackjack

*Bouncing Ball* - A bouncing ball animation. Press Ctrl-C to stop.

*Bouncing Lines* - A bouncing line animation. Press Ctrl-C to stop.

*Calendar Maker* - Create monthly calendars, saved to a text file and fit for printing.

*Chance Checkers* - Checkers, but you can move 3 random checkers per turn. These checkers are randomly decided, and can be the player's own checkers or their opponents', but you can't move your opponents' promoted checkers. In this version, capturing is not mandatory.

*Daleks* - Try to get the robots to crash into each other.

*Checkers* - The classic checkers board game. In this version, capturing is not mandatory.

*Chomp* - A dangerously delicious logic game. Inspired by a Frederik Schuh and David Gale puzzle, published by Martin Gardner in Scientific American (January 1973) More info at: https://en.wikipedia.org/wiki/Chomp

*Clickbait Headline Generator* - A clickbait headline generator for your soulless content farm.

*Coin Flip Simulator* - Simulate a large number of coin flips.

*Collatz Sequence* - Generates numbers for the Collatz sequence, given a starting number.

*Collatz Sequence Stats* - Finds out how long various Collatz Sequences are.

*Connect Four* - A board game to get four tiles in a row.

*Conway's Game of Life* - The classic cellular automata simulation. Press Ctrl-C to stop. More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

*Conway's Game of Life (Terminal)* - The classic cellular automata simulation. Press Ctrl-C to stop. More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

*Countdown* - Show a countdown timer animation using a seven-segment display. Press Ctrl-C to stop. More info at https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.

*Diagonal Maze* - Prints out a random, diagonal maze. Inspired by the 10 PRINT CHR$(205.5+RND(1)); : GOTO 10 program.

*Dice Roller* - Simulates dice rolls using the Dungeons & Dragons notation.

*Digital Clock* - Display a digital clock of the current time with a seven-segment display. Press Ctrl-C to stop. More info at https://en.wikipedia.org/wiki/Seven-segment_display Requires our sevseg.py program.

*DNA* - A simple animation of a DNA double-helix. Press Ctrl-C to stop. Thanks to matoken for inspiration: https://asciinema.org/a/155441

*Eeny-Meeny-Miny-Moe* - An elimination game for multiple players. Press Ctrl-C to stop. More info at https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe More info at https://en.wikipedia.org/wiki/Josephus_problem

*Etch a Sketch* - Draw a trailing line on the screen.

*Factorization* - Find all the factors of a number.

*Fireflies* - A beautiful animation of fireflies. Press Ctrl-C to stop.

*Fish Tank* - A peaceful animation of a fish tank. Press Ctrl-C to stop.

*FizzBuzz Calculation* - Calculates the answers for the fizz buzz programming problem.

*FizzBuzz Game* - A number game where you also race against the clock.

*Flippy (a Reversi clone)* - (Requires Pygame) Play against the computer and try to flip their tiles.

*Flood Fill* - An example of a "flood fill" algorithm. This is a basic demo of both the recursive and iterative floodfill algorithms. This algorithm is commonly used in "fill tools" in graphics programs like MS Paint or Photoshop. This algorithm is also used in the floodit.py game.

*Flood It!* - A colorful game where you try to fill the board with a single color.

*Forest Fire Sim* - A simulation of fires spreading in a growing forest. Press Ctrl-C to stop. Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/

*Four-In-A-Row* - (Requires Pygame) Play against the computer, dropping tiles to connect four.

*Nonuniform Fractal Tree Drawer* - Draws nonuniform fractal trees with turtle graphics.

*Fractal Tree Drawer* - Draws fractal trees with turtle graphics.

*2048 Game* - A sliding tile game to combine exponentially-increasing numbers. Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios' 1024, which in turn is a clone of the Threes! game. More info at https://en.wikipedia.org/wiki/2048_(video_game)

*Gemgem (a Bejeweled clone)* - (Requires Pygame) An addictive jewel matching game.

*Ghost Leg Lottery* - Follow the trail to see who wins! More info at: https://en.wikipedia.org/wiki/Ghost_Leg

*Guess the Number* - While given hints, try to guess the secret number.

*Guillotine* - A French variant of Hangman with different graphics. Ooh la la!

*Hacking* - The hacking mini-game from "Fallout 3".

*Hammurabi* - The classic game Hamurabi.bas by Doug Dyment, popularized by David Ahl.

*Hamsburger* - A program for making silly pluralizations. Press Ctrl-C to stop.

*Hangman* - A word-guessing game.

*Hangman with Random Letters* - A completely unfair word-guessing game. (This is a joke program.)

*Hard-coded Tic Tac Toe* - Play tic tac toe against the computer. Every possible move has been hard-coded into this program. The program is 5700 lines long. This is a joke program, don't actually write code like this.

*Hilbert Curve* - Draws the Hilbert Curve fractal with turtle graphics. More info at: https://en.wikipedia.org/wiki/hilbertCurve Good videos on space-filling curves: https://youtu.be/RU0wScIj36o and https://youtu.be/3s7h2MHQtxc

*Hour Glass Animation* - An animation of an hour glass filled with falling sand. Press Ctrl-C to stop.

*Idiot* - How to keep an idiot busy for hours. (This is a joke program.)

*Ink Spill (a Flood It clone)* - (Requires Pygame) Try to make the entire field a single color.

*J'ACCUSE!* - A mystery game of intrigue and a missing cat. Inspired by Homestar Runner's "Where's an Egg?" game

*Koch Snowflake* - Draws a Koch snowflake fractal with turtle graphics.

*Langton's Ant* - A cellular automata animation. Press Ctrl-C to stop. More info: https://en.wikipedia.org/wiki/Langton%27s_ant

*Lawnmower* - Watch grass get cut and grow again. Press Ctrl-C to stop. Inspired by Tondeuse by Jules Villard, https://asciinema.org/a/21743 https://bitbucket.org/jvillard/tondeuse/src/default/

*Leetspeak* - Translates English messages into l33t5p34]<.

*Luhn Checksum Algorithm* - The mathematics behind credit card numbers. More info at: https://en.wikipedia.org/wiki/Luhn_algorithm More info at: https://youtu.be/Erp8IAUouus

*Magic Eight Ball* - Ask a question about your future.

*Magic Hexagon* - Place numbers in a hexagon so each row adds up to 38. More info at https://en.wikipedia.org/wiki/Magic_hexagon More info at https://www.youtube.com/watch?v=ZkVSRwFWjy0

*Mancala* - The ancient seed-sowing board game. Rules at http://www.mancalarules.com/ More info at https://en.wikipedia.org/wiki/Mancala

*Matching Parentheses* - A parentheses/bracket/braces matching algorithm.

*Maze Maker* - Make mazes with the recursive backtracker algorithm. More info at: https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker An animated demo: https://scratch.mit.edu/projects/17358777/

*Maze Runner* - Move around a maze and try to escape.

*Maze 3D* - Move around a maze and try to escape... in 3D!

*Maze Runner HTML* - Move around a maze and try to escape... in 3D and IN YOUR WEB BROWSER!

*Memory Puzzle* - (Requires Pygame) A simple memory matching game.

*Middle Letter Scrambler* - Scrambles the middle letters of words, but not the first and last letters.

*Million Dice Roll Stats* - A simulation of one million dice rolls.

*Mona Lisa* - Draws an Andy Warhol-like drawing of the Mona Lisa with turtle graphics.

*Mondrian Art Generator* - Randomly generates Mondrian-style art.

*Monty Hall Problem* - A simulation of the Monty Hall game show problem. More info at https://en.wikipedia.org/wiki/Monty_Hall_problem

*Morse Code* - Translates between English and Morse Code. More info at: https://en.wikipedia.org/wiki/Morse_code

*Multiplication Table* - Print a multiplication table.

*Multiplicative Persistence* - A fun math challenge. For more information about this topic, see https://youtu.be/Wim9WJeDTHQ

*99 Bottles of Beer on the Wall* - Print the full lyrics to one of the most longest songs ever! Press Ctrl-C to stop.

*Peg Solitaire* - A single-player, peg-jumping game to eliminate all the pegs. More info at https://en.wikipedia.org/wiki/Peg_solitaire

*Pentomino* - (Requires Pygame) Like Pygame, except with 5-box blocks.

*Periodic Table of Elements* - Displays atomic information for all the elements.

*Pig Latin* - Translates English messages into Igpay Atinlay.

*Polygons* - A turtle program to draw polygons. Every line is the same length.

*Progress Bar* - A sample progress bar animation that can be used in other programs.

*Pythons* - Drawing pythons with turtle graphics.

*Rail Fence Cipher* - The "rail fence" cipher for encrypting text. More info at: https://en.wikipedia.org/wiki/Rail_fence_cipher

*Rainbow* - Shows a simple rainbow animation. Press Ctrl-C to stop.

*Rainbow 2* - Shows a simple squiggle rainbow animation. Press Ctrl-C to stop.

*Random Walk* - Generate splatter-art with the "random walk" algorithm. Press Ctrl-C to stop. More info at: https://en.wikipedia.org/wiki/Random_walk

*Reversi* - A tile flipping game, also called reversi. More info https://en.wikipedia.org/wiki/Reversi

*Rock-Paper-Scissors* - A hand game of luck.

*Rock-Paper-Scissors (Always Win)* - A hand game of luck, except you cannot lose.

*ROT13 Cipher* - The simplest cipher for encrypting and decrypting text. More info at https://en.wikipedia.org/wiki/ROT13

*Rotating Cube* - A rotating cube animation. Press Ctrl-C to stop.

*Rotating Cube (Bext Version)* - A rotating cube animation. Press Ctrl-C to stop.

*Rotating Sphere* - A rotating sphere animation. Press Ctrl-C to stop.

*Rush Hour* - A sliding tile puzzle game to move cars out of the way. Original game by Nob Yoshihagara More info at https://www.michaelfogleman.com/rush/

*Sand Fall* - A falling sand animation. Inspired by https://asciinema.org/a/6515

*Sand Fall (Bext Version)* - A falling sand animation. Inspired by https://asciinema.org/a/6515

*Sevseg* - A seven-segment display module. More info at https://en.wikipedia.org/wiki/Seven-segment_display

*Shell Game* - A random gambling game.

*Sierpinkski's Game* - Sierpinkski's "game" is an algorithm that draws Sierpinski's Triangle with turtle graphics. More info at https://en.wikipedia.org/wiki/Chaos_game

*Sierpinski Square* - Draws the Sierpinski Square (also called Carpet) with turtle graphics. More info at: https://en.wikipedia.org/wiki/Sierpinski_carpet

*Sierpinski Triangle* - Draws the Sierpinski Triangle fractal with turtle graphics.

*Simulate (a Simon clone)* - (Requires Pygame) Copy the pattern of flashing lights for as long as possible.

*Slide Puzzle* - (Requires Pygame) The classic 15-tile slide puzzle.

*15-Sliding Puzzle* - Slide the numbered tiles into the correct order.

*Snail Race* - Fast-paced snail racing action!

*Sokoban clone* - The classic crate-pushing game.

*Sonar Treasure Hunt* - Try to locate treasure chests hidden under the waves.

*Soroban* - A simulation of a Japanese abacus calculator tool. More info at: https://en.wikipedia.org/wiki/Soroban

*Spiral* - Draws a simple square spiral.

*sPoNgEtExT* - Translates English messages into sPOnGEtExT.

*Squirrel Eat Squirrel* - (Requires Pygame) A game where squirrels eat each other and grow monstrously large.

*Star Pusher (a Sokoban clone)* - (Requires Pygame) A puzzle game where you push the stars over their goals.

*Sticky Hands* - A jewel-stealing, movement puzzle game.

*Sudoku* - The classic 9x9 number placement puzzle. More info at https://en.wikipedia.org/wiki/Sudoku

*Tetromino (a Tetris clone)* - (Requires Pygame) The classic block falling puzzle from the Soviet Union.

*Tetromino for Idiots* - (Requires Pygame) Tetris, but... simpler.

*Three-Card Monte* - Find the Queen of Hearts after cards have been swapped around. (In the real-life version, the scammer palms the Queen of Hearts so you always lose.) More info at https://en.wikipedia.org/wiki/Three-card_Monte

*Tic Tac Toe* - The classic board game.

*Tic Tac Toe (OOP)* - The classic board game. (Object-oriented programming version.)

*Towers of Hanoi puzzle* - A puzzle where you must move the discs of one tower to another tower. More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi

*Ulam Spiral* - The Ulam spiral is a mysterious mathematics pattern for prime numbers with turtle graphics. More info at https://en.wikipedia.org/wiki/Ulam_spiral

*Water Bucket Puzzle* - A water pouring puzzle. More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle

*Wormy* - (Requires Pygame) Lead the green snake around the screen eating red apples.

*Zigzag* - A simple zig zag animation. Press Ctrl-C to stop.


TODO NOTES
==========

(The rest of these are placeholder ideas and not officially a part of this README)

TODO - explain why I don't use cls/clear if it isn't necessary (it's to make programs compatible with non terminal environemnts, like idle or vscode or pycharm)

Games should:

* Have unit tests, which show how you can call the individual functions and see what they do with their input.
* Should I include type hints? (Decision: nah. They're often not needed and I feel like their occassional presence would be more distracting than illuminating.)
* Maybe include a barebones version of games, with stub functions that specify what their input/output, and hint at what other functions in the program they'll call? And the data structures used?
* I should focus on games that don't require data structures (this removes most board games).
* Games should have logging messages that can be enabled?


TODO polishing process
* Create unit tests for each game.
* Test inputs. It should be impossible to crash a game with user input.
* Add comments liberally.
* Add assert statements. These should never arise during the game. (Test!)
* Create the "skeletons" of each game, which has just the function stubs and docstring, plus list of functions that this function calls. Unit tests can help them with filling out their skeletons.
* Write up a description for each game, which includes a sample play session text.
* Description should have a link to pythontutor.com.
* Describe data structures used, including examples.


Game Ideas:
- Nonograms https://en.wikipedia.org/wiki/Nonogram

Class protocol:
* Copy the source code by typing it.
* Run the program and test it.
* Run it under a debugger, answer questions about variable values.
* Make the changes suggested for this project.
* Try to remake the game without looking at the source, read the list of objectives.


TODO entry outline (what a single program looks like on its page or book)
- Name
- Brief description and credits (This plus name and link should be able to fit into a tweet.)
- Three screenshots. (To include in the tweet)
- Longer description.
- Sample play text.
- Data structure examples.
- Pythontutor link
- SKIP THIS: Skeleton source code
- SKIP THIS: Unit tests (not utterly comprehensive or 100 % code coverage, but enough to convey the idea of the game's functions)
- Full source code (and github link)
- List of questions that probe if the reader knows how the code works.
- List of experiments to try out.

Note: Remind readers that they can hit Ctrl-C to quit a program. Also remind them to run the programs under a debugger.

Note: I think we should avoid the "stub/skeleton" code format. The reader is put into a position of trying to read the original programmer's mind, instead of just creating a game they want to play. So this means we don't need extensive docstrings, unit tests, or assertions at the top of each function.

TODO tweet format:
Python programming tutorial for text-based games: <NAME> <DESC> <LINK>

Copyright 2019, Al Sweigart. All rights reserved.