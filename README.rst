# PythonStdioGames
A compilation of text-based games written in Python that only use "standard i/o".



TODO NOTES:

Games should:

* Be under 256 lines long.
* Use only the standard library (or perhaps Colorama or PyTextCanvas)
* Only use print() and input() stdio text for input/output. (No graphics or mouse input.)
* Be well-commented.
* Have comments pointing out what lines can be changed.
* Have comments explaining their data structures.
* Have links to pythontutor.net to view run throughs.
* Have unit tests, which show how you can call the individual functions and see what they do with their input.
* Should I include type hints?
* Functions should only call functions that have already been defined (to aide a top-to-bottom reading of the code)
* Get rid of any functions that modify things in-place. Use tuples.
* Maybe include a barebones version of games, with stub functions that specify what their input/output, and hint at what other functions in the program they'll call? And the data structures used?
* I should focus on games that don't require data structures (this removes most board games).
* Games can use anything from CP437 encoding (Windows is the limiting feature here, otherwise we could use utf-8), but the source code must be typeable, i.e. use chr(9608) instead of █.


TODO types:
* No data structure games (i.e. guess the number)
* Simple data structures, no OOP (i.e. most of the board games)
* Color games, that use color and block characters.
* Canvas games, that can write to arbitrary places on the screen (maze)



TODO polishing process
* Create unit tests for each game.
* Test inputs. It should be impossible to crash a game with user input.
* Add comments liberally.
* Each function needs a docstring.
* Add assert statements. These should never arise during the game. (Test!)
* Create the "skeletons" of each game, which has just the function stubs and docstring, plus list of functions that this function calls. Unit tests can help them with filling out their skeletons.
* Write up a description for each game, which includes a sample play session text.
* Description should have a link to pythontutor.com.
* Describe data structures used, including examples.



TODO entry outline (what a single program looks like on its page or book)
- Name
- Brief description and credits (This plus name and link should be able to fit into a tweet.)
- Three screenshots. (To include in the tweet)
- Longer description.
- Sample play text.
- Data structure examples.
- Pythontutor link
- Skeleton source code
- Unit tests (not utterly comprehensive or 100 % code coverage, but enough to convey the idea of the game's functions)
- Full source code (and github link)


TODO tweet format:
Python programming tutorial for text-based games: <NAME> <DESC> <LINK>

Copyright 2018, Al Sweigart. All rights reserved.