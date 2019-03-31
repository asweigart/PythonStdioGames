# PythonStdioGames

A compilation of text-based games written in Python 3.

About this Collection
=====================

After beginners learn the syntax of Python and basic programming concpets (loops, branching, functions, etc.) they often hit a dead-end: "How do I become better at programming?" At this point, people will tell them to work on their own practice projects (but this leaves them without guidance on what to make and how to make it) or to contribute to open source projects (but its difficult to find one, understand its code base, and get guidance on how to contribute).

What helped me learn to code was finding small projects whose source code I copied and then made small adjustments to. This gave me insight on how loops, branching, and functions combined together into actual programs.

To help others down the same path, I'm creating a collection of example programs aimed at being easy to copy and understand by beginners. These programs (mostly games) have the following constraints:

* They're short, with a limit of 256 lines of code. *This makes them easy to read and understand in one sitting. The shorter the better; plenty of fun programs can fit under 64 lines of code. The "power of 2" numbers for the limits are just for fun.*
* They fit into a single source code file and have no installer. *This makes these games trivial to share by copy/pasting code to a pastebin site. Though perhaps a data/image/save files can be included.*
* They only use the Python standard library. *Fewer things to install means less chance of failing during environment setup and wider compatibility.*
* They only use stdio text; `print()` and `input()` in Python. *The output being in the same text medium as the text source code makes it less abstract, and easier to see the cause-effect relationship between code and output. This means there's no graphics or mouse input, but makes it simple to port these programs to other languages since they all support stdio text.*
* They're necessarily turn-based. *Relying on `input()` means the program must wait for the user to enter text, but this means we can't have real-time programs that respond to single key-presses.*
* They're well commented. *Comments should be aimed at beginners; they don't explain programming concepts, but rather how they're being used in the program. The 256-line limit includes comments and whitespace. If the program is too long to include abundant comments and sensible whitespace, it should be simplified.*
* They use as few programming concepts as possible. *If classes, list comprehensions, recursion, aren't necessary for the program, then they are't used.*
* **Elegant** and **efficient** code is worthless next to code that is **easy to understand** and **readable**. *These programs are for education, not production. Standard best practices, like not using global variables, can be ignored to make it easier to understand.*
* They do input validation and are bug free. *It should be impossible to crash a program with bad input or an edge case.*
* All functions have docstrings. *This is good documentation practice, but also enables the `help()` function to work in the interactive shell.*


Additional Guidelines
=====================

Additional guidelines include:

* Some of these programs use the `bext` module, which adds curses-like features like color, clearing the screen, and moving the cursor
* Include a link to a run-through of the program on https://pythontutor.com so that the student can see how the program runs.
* Longer, more descriptive variable names are better than shorter ones. Avoid using single-letter variable names except for `i` and `j`, or `x` and `y`.
* Have comments marked as `# EXPERIMENT!` that describe minor changes that they can make (increasing health, changing difficulty, etc.)
* Use jsdifflib to create online diffs. *This is an easy way for students to find their own typos when copying the code. An example is here: https://inventwithpython.com/invent4thed/diff/*
* Use `assert` statements to catch common typos the student makes when typing in the code, especially for constants that they may modify.
* Use Python 3. *The only time Python 2 is appropriate to use is when there's a large existing codebase. But this is for new programmers working on greenfield projects.*
* Stick to characters in CP437 "extended ASCII" encoding. *Windows' command line is the limiting factor here; it can't display all UTF-8 characters.*
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
* `pyperclip` for copying/psating text with the clipboard.
* `playsound` for playing sound files.
* `pyttsx3` for text to speech.
* `pytextcavas` for 2D strings you can draw on
* `pyrect` for rectangle data structure
* `pybresenham` for various line-drawing functions



TODO NOTES
==========

(The rest of these are placeholder ideas and not officially a part of this README)

TODO - explain why I don't use cls/clear if it isn't necessary (it's to make programs compatible with non terminal environemnts, like idle or vscode or pycharm)

Games should:

* Have unit tests, which show how you can call the individual functions and see what they do with their input.
* Should I include type hints?
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


Note: I think we should avoid the "stub/skeleton" code format. The reader is put into a position of trying to read the original programmer's mind, instead of just creating a game they want to play. So this means we don't need extensive docstrings, unit tests, or assertions at the top of each function.

TODO tweet format:
Python programming tutorial for text-based games: <NAME> <DESC> <LINK>

Copyright 2019, Al Sweigart. All rights reserved.