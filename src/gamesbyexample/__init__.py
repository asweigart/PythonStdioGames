# Games By Example
# By Al Sweigart al@inventwithpython.com

# TODO - also check the support files to see if they've been changed.
# TODO - check for changes on startup

__version__ = '0.1.1'

"""
# This code reads in all the .py files to create the PROGRAMS list.
import os, pprint, zlib
PROGRAMS = []
for filename in os.listdir('.'):
    if not filename.endswith('.py') or filename.startswith('_'):
        continue

    with open(filename, encoding='utf-8') as fo:
        lines = fo.readlines()
        content = ''.join(lines)

        name, credit = lines[0][2:].split(',')
        desc = lines[1][2:].strip()
        hash = zlib.adler32(content.encode('utf-8'))

        entry = {'filename': filename, 'name':name, 'desc': desc, 'hash': hash}
        PROGRAMS.append(entry)

pprint.pprint(PROGRAMS, indent=4, width=120)
"""

PROGRAMS = [   {   'desc': 'A time-based quiz game to see how fast you can alphabetize letters.',
        'filename': 'alphabetizequiz.py',
        'hash': 3679101624,
        'name': 'Alphabetize Quiz'},
    {   'desc': 'A time-based quiz game to see how fast you can alphabetize words.',
        'filename': 'alphabetizewordquiz.py',
        'hash': 3810970832,
        'name': 'Alphabetize Word Quiz'},
    {'desc': 'An analog clock animation.', 'filename': 'analogclock.py', 'hash': 4162372886, 'name': 'Analog Clock'},
    {'desc': 'A deductive logic game.', 'filename': 'bagels.py', 'hash': 450863561, 'name': 'Bagels'},
    {   'desc': 'Explore the mathematics of the "Birthday Paradox".',
        'filename': 'birthdayparadox.py',
        'hash': 2263912927,
        'name': 'Birthday Paradox Simulation'},
    {'desc': 'A card game also known as 21.', 'filename': 'blackjack.py', 'hash': 3444948157, 'name': 'Blackjack'},
    {'desc': 'A bouncing ball animation.', 'filename': 'bouncingDots.py', 'hash': 2196805490, 'name': 'Bouncing Ball'},
    {   'desc': 'A bouncing line animation.',
        'filename': 'bouncingLines.py',
        'hash': 3195429384,
        'name': 'Bouncing Lines'},
    {   'desc': 'Create monthly calendars, saved to a text file and fit for printing.',
        'filename': 'calendarmaker.py',
        'hash': 1720434118,
        'name': 'Calendar Maker'},
    {   'desc': 'Checkers, but you can move 3 random checkers per turn.',
        'filename': 'chancecheckers.py',
        'hash': 2501267000,
        'name': 'Chance Checkers'},
    {   'desc': 'Try to get the robots to crash into each other.',
        'filename': 'chase.py',
        'hash': 3391338156,
        'name': 'Daleks'},
    {'desc': 'The classic checkers board game.', 'filename': 'checkers.py', 'hash': 1002543678, 'name': 'Checkers'},
    {'desc': 'A dangerously delicious logic game.', 'filename': 'chomp.py', 'hash': 1402302762, 'name': 'Chomp'},
    {   'desc': 'Simulate a large number of coin flips.',
        'filename': 'coinflipsimulator.py',
        'hash': 3091534593,
        'name': 'Coin Flip Simulator'},
    {   'desc': 'A board game to get four tiles in a row.',
        'filename': 'connectfour.py',
        'hash': 1264330418,
        'name': 'Connect Four'},
    {   'desc': 'The classic cellular automata simulation.',
        'filename': 'conwaysgameoflife1.py',
        'hash': 2401426095,
        'name': "Conway's Game of Life"},
    {   'desc': 'The classic cellular automata simulation.',
        'filename': 'conwaysgameoflife2.py',
        'hash': 1061912555,
        'name': "Conway's Game of Life (Terminal)"},
    {   'desc': 'Show a countdown timer animation using a seven-segment display.',
        'filename': 'countdown.py',
        'hash': 4038246353,
        'name': 'Countdown'},
    {   'desc': 'Prints out a random, diagonal maze.',
        'filename': 'diagonalmaze.py',
        'hash': 676041317,
        'name': 'Diagonal Maze'},
    {   'desc': 'Simulates dice rolls using the Dungeons & Dragons notation.',
        'filename': 'diceroller.py',
        'hash': 2858775506,
        'name': 'Dice Roller'},
    {   'desc': 'Display a digital clock of the current time with a seven-segment display.',
        'filename': 'digitalclock.py',
        'hash': 3254860983,
        'name': 'Digital Clock'},
    {'desc': 'A simple animation of a DNA double-helix.', 'filename': 'dna.py', 'hash': 1231544695, 'name': 'DNA'},
    {   'desc': 'An elimination game for multiple players.',
        'filename': 'eenymeeny.py',
        'hash': 3009437366,
        'name': 'Eeny-Meeny-Miny-Moe'},
    {   'desc': 'Draw a trailing line on the screen.',
        'filename': 'etchasketch.py',
        'hash': 2145033535,
        'name': 'Etch a Sketch'},
    {   'desc': 'Find all the factors of a number.',
        'filename': 'factorfinder.py',
        'hash': 2663323331,
        'name': 'Factorization'},
    {'desc': 'A beautiful animation of fireflies.', 'filename': 'fireflies.py', 'hash': 129555302, 'name': 'Fireflies'},
    {   'desc': 'A peaceful animation of a fish tank.',
        'filename': 'fishtank.py',
        'hash': 2835060774,
        'name': 'Fish Tank'},
    {   'desc': 'Calculates and prints the answers for the fizz buzz programming problem.',
        'filename': 'fizzbuzz.py',
        'hash': 16724279,
        'name': 'FizzBuzz Calculation'},
    {   'desc': 'A number game where you also race against the clock.',
        'filename': 'fizzbuzzgame.py',
        'hash': 3345288866,
        'name': 'FizzBuzz Game'},
    {   'desc': 'An example of a "flood fill" algorithm.',
        'filename': 'floodfill.py',
        'hash': 2836484034,
        'name': 'Flood Fill'},
    {   'desc': 'A colorful game where you try to fill the board with a single color.',
        'filename': 'floodit.py',
        'hash': 256561262,
        'name': 'Flood It!'},
    {   'desc': 'A simulation of fires spreading in a growing forest.',
        'filename': 'forestfiresim.py',
        'hash': 300907861,
        'name': 'Forest Fire Sim'},
    {   'desc': 'A sliding tile game to combine exponentially-increasing numbers.',
        'filename': 'game2048.py',
        'hash': 2816824104,
        'name': '2048 Game'},
    {   'desc': 'While given hints, try to guess the secret number.',
        'filename': 'guess.py',
        'hash': 2569765641,
        'name': 'Guess the Number'},
    {'desc': 'A variant of Hangman.', 'filename': 'guillotine.py', 'hash': 2878683704, 'name': 'Guillotine'},
    {   'desc': 'The hacking mini-game from "Fallout 3".',
        'filename': 'hacking.py',
        'hash': 2938342729,
        'name': 'Hacking'},
    {   'desc': 'The classic game Hamurabi.bas by Doug Dyment, popularized by David Ahl.',
        'filename': 'hammurabi.py',
        'hash': 4213103760,
        'name': 'Hammurabi'},
    {   'desc': 'A program for making silly pluralizations.',
        'filename': 'hamsburger.py',
        'hash': 1013097268,
        'name': 'Hamsburger'},
    {'desc': 'A word-guessing game.', 'filename': 'hangman.py', 'hash': 2131849199, 'name': 'Hangman'},
    {   'desc': 'An animation of an hour glass filled with falling sand.',
        'filename': 'hourglass.py',
        'hash': 939937483,
        'name': 'Hour Glass Animation'},
    {'desc': 'How to keep an idiot busy for hours.', 'filename': 'idiot.py', 'hash': 3536566686, 'name': 'Idiot'},
    {   'desc': 'A mystery game of intrigue and a missing cat.',
        'filename': 'jaccuse.py',
        'hash': 4034358414,
        'name': "J'ACCUSE!"},
    {   'desc': 'A cellular automata animation.',
        'filename': 'langtonsant.py',
        'hash': 221210395,
        'name': "Langton's Ant"},
    {'desc': 'Watch grass get cut and grow again.', 'filename': 'lawnmower.py', 'hash': 214423045, 'name': 'Lawnmower'},
    {   'desc': 'Translates English messages into l33t5p34]<.',
        'filename': 'leetspeak.py',
        'hash': 2309523406,
        'name': 'Leetspeak'},
    {   'desc': 'The mathematics behind credit card numbers.',
        'filename': 'luhn.py',
        'hash': 3961706895,
        'name': 'Luhn Checksum Algorithm'},
    {   'desc': 'Ask a question about your future.',
        'filename': 'magic8ball.py',
        'hash': 2541805654,
        'name': 'Magic Eight Ball'},
    {   'desc': 'Place numbers in a hexagon so each row adds up to 38.',
        'filename': 'magichexagon.py',
        'hash': 2324805318,
        'name': 'Magic Hexagon'},
    {'desc': 'The ancient seed-sowing board game.', 'filename': 'mancala.py', 'hash': 37936232, 'name': 'Mancala'},
    {   'desc': 'A parentheses/bracket/braces matching algorithm.',
        'filename': 'matchingparens.py',
        'hash': 1502912935,
        'name': 'Matching Parentheses'},
    {   'desc': 'Make mazes with the recursive backtracker algorithm.',
        'filename': 'mazemakerrec.py',
        'hash': 3920223107,
        'name': 'Maze Maker'},
    {   'desc': 'Move around a maze and try to escape.',
        'filename': 'mazerunner2d.py',
        'hash': 3714151337,
        'name': 'Maze Runner'},
    {   'desc': 'Move around a maze and try to escape... in 3D!',
        'filename': 'mazerunner3d.py',
        'hash': 404713790,
        'name': 'Maze 3D'},
    {   'desc': 'Move around a maze and try to escape... in 3D and IN YOUR WEB BROWSER!',
        'filename': 'mazerunnerhtml.py',
        'hash': 702122501,
        'name': 'Maze Runner HTML'},
    {   'desc': 'Scrambles the middle letters of words, but not the first and last letters.',
        'filename': 'middleletterscrambler.py',
        'hash': 1926094473,
        'name': 'Middle Letter Scrambler'},
    {   'desc': 'A simulation of one million dice rolls.',
        'filename': 'milliondicestats.py',
        'hash': 3778164340,
        'name': 'Million Dice Roll Stats'},
    {   'desc': 'Randomly generates Mondrian-style art.',
        'filename': 'mondrian.py',
        'hash': 3493552027,
        'name': 'Mondrian Art Generator'},
    {   'desc': 'A simulation of the Monty Hall game show problem.',
        'filename': 'montyhall.py',
        'hash': 2286064701,
        'name': 'Monty Hall Problem'},
    {   'desc': 'Translates between English and Morse Code.',
        'filename': 'morsecode.py',
        'hash': 1839644749,
        'name': 'Morse Code'},
    {   'desc': 'Print a multiplication table.',
        'filename': 'multiplicationtable.py',
        'hash': 3058432580,
        'name': 'Multiplication Table'},
    {   'desc': 'A fun math challenge.',
        'filename': 'multiplicativepersistence.py',
        'hash': 2252592739,
        'name': 'Multiplicative Persistence'},
    {   'desc': 'Print the full lyrics to one of the most longest songs ever!',
        'filename': 'ninetyninebottles.py',
        'hash': 3969475375,
        'name': '99 Bottles of Beer on the Wall'},
    {   'desc': 'A single-player, peg-jumping game to eliminate all the pegs.',
        'filename': 'pegsolitaire.py',
        'hash': 659635828,
        'name': 'Peg Solitaire'},
    {   'desc': 'Displays atomic information for all the elements.',
        'filename': 'periodictable.py',
        'hash': 1648500377,
        'name': 'Periodic Table of Elements'},
    {   'desc': 'Translates English messages into Igpay Atinlay.',
        'filename': 'piglatin.py',
        'hash': 1865459740,
        'name': 'Pig Latin'},
    {   'desc': 'A sample progress bar animation that can be used in other programs.',
        'filename': 'progressbar.py',
        'hash': 4207632425,
        'name': 'Progress Bar'},
    {   'desc': 'The "rail fence" cipher for encrypting text.',
        'filename': 'railfencecipher.py',
        'hash': 1704441160,
        'name': 'Rail Fence Cipher'},
    {'desc': 'Shows a simple rainbow animation.', 'filename': 'rainbow.py', 'hash': 763983654, 'name': 'Rainbow'},
    {   'desc': 'Shows a simple squiggle rainbow animation.',
        'filename': 'rainbow2.py',
        'hash': 1916422475,
        'name': 'Rainbow 2'},
    {   'desc': 'Generate splatter-art with the "random walk" algorithm.',
        'filename': 'random_walk.py',
        'hash': 1080932263,
        'name': 'Random Walk'},
    {   'desc': 'A tile flipping game, also called reversi.',
        'filename': 'reversi.py',
        'hash': 3249954277,
        'name': 'Reversi'},
    {   'desc': 'A hand game of luck.',
        'filename': 'rockpaperscissors.py',
        'hash': 2770193779,
        'name': 'Rock-Paper-Scissors'},
    {   'desc': 'A hand game of luck, except you cannot lose.',
        'filename': 'rockpaperscissorsalwayswin.py',
        'hash': 3868964975,
        'name': 'Rock-Paper-Scissors (Always Win)'},
    {   'desc': 'The simplest cipher for encrypting and decrypting text.',
        'filename': 'rot13.py',
        'hash': 2790846069,
        'name': 'ROT13 Cipher'},
    {'desc': 'A rotating cube animation.', 'filename': 'rotating_cube.py', 'hash': 2102537858, 'name': 'Rotating Cube'},
    {   'desc': 'A rotating cube animation.',
        'filename': 'rotating_cube_bext.py',
        'hash': 3717843260,
        'name': 'Rotating Cube (Bext Version)'},
    {   'desc': 'A rotating sphere animation.',
        'filename': 'rotating_sphere.py',
        'hash': 1438669314,
        'name': 'Rotating Sphere'},
    {   'desc': 'A sliding tile puzzle game to move cars out of the way.',
        'filename': 'rushhour.py',
        'hash': 725851724,
        'name': 'Rush Hour'},
    {'desc': 'A falling sand animation.', 'filename': 'sandfall.py', 'hash': 1878174128, 'name': 'Sand Fall'},
    {   'desc': 'A falling sand animation.',
        'filename': 'sandfall_bext.py',
        'hash': 1646136057,
        'name': 'Sand Fall (Bext Version)'},
    {'desc': 'A seven-segment display module.', 'filename': 'sevseg.py', 'hash': 3998880389, 'name': 'Sevseg'},
    {'desc': 'A random gambling game.', 'filename': 'shellgame.py', 'hash': 149648362, 'name': 'Shell Game'},
    {   'desc': 'Slide the numbered tiles into the correct order.',
        'filename': 'slidingpuzzle.py',
        'hash': 3065884899,
        'name': '15-Sliding Puzzle'},
    {'desc': 'The classic crate-pushing game.', 'filename': 'sokoban.py', 'hash': 2518098407, 'name': 'Sokoban clone'},
    {   'desc': 'Try to locate treasure chests hidden under the waves.',
        'filename': 'sonar.py',
        'hash': 3627883142,
        'name': 'Sonar Treasure Hunt'},
    {   'desc': 'A simulation of a Japanese abacus calculator tool.',
        'filename': 'soroban.py',
        'hash': 233040048,
        'name': 'Soroban'},
    {'desc': 'Draws a simple square spiral.', 'filename': 'spiral.py', 'hash': 4217272586, 'name': 'Spiral'},
    {   'desc': 'Translates English messages into sPOnGEtExT.',
        'filename': 'spongetext.py',
        'hash': 2691981097,
        'name': 'sPoNgEtExT'},
    {   'desc': 'A jewel-stealing, movement puzzle game.',
        'filename': 'stickyhands.py',
        'hash': 779399551,
        'name': 'Sticky Hands'},
    {   'desc': 'Find the Queen of Hearts after cards have been swapped around.',
        'filename': 'threecardmonte.py',
        'hash': 2299700193,
        'name': 'Three-Card Monte'},
    {'desc': 'The classic board game.', 'filename': 'tictactoe.py', 'hash': 1485160391, 'name': 'Tic Tac Toe'},
    {   'desc': 'The classic board game. (Object-oriented programming version.)',
        'filename': 'tictactoe_oop.py',
        'hash': 2945682246,
        'name': 'Tic Tac Toe (OOP)'},
    {   'desc': 'A puzzle where you must move the discs of one tower to another tower.',
        'filename': 'towersOfHanoi.py',
        'hash': 2378944880,
        'name': 'Towers of Hanoi puzzle'},
    {'desc': 'Draws pretty routes.', 'filename': 'tsuromapmaker.py', 'hash': 2150152118, 'name': 'Tsuro Map Maker'},
    {   'desc': 'A water pouring puzzle.',
        'filename': 'waterbucket.py',
        'hash': 1502345600,
        'name': 'Water Bucket Puzzle'},
    {   'desc': 'A water pouring puzzle.',
        'filename': 'waterbucket_oop.py',
        'hash': 4196290161,
        'name': 'Water Bucket Puzzle (OOP)'},
    {'desc': 'A simple zig zag animation.', 'filename': 'zigzag.py', 'hash': 922535460, 'name': 'Zigzag'}]


import time, sys, os, subprocess, zlib, zipfile, webbrowser

from tkinter import *
from tkinter import font
from tkinter import ttk

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))

# Check for any missing files and reload them from the originalFiles.zip file:
for program in PROGRAMS:
    if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, program['filename'])):
        # Restore the file from the original one in the originalFiles.zip backup.
        originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, 'originalFiles.zip'), 'r')
        originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)


def _executable_exists(name):
    # Find out if an executable program named `name` is reachable:
    return subprocess.call(['which', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def programSelect(*args):
    global CURRENT_SELECTED_INDEX
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
    TERMINAL_OPENER = os.path.join(FOLDER_OF_THIS_FILE, '__terminalopener__.py')

    # Figure out which program to run to open a new terminal window and then run the .py file:
    if sys.platform == 'win32':
        os.system('start cmd /K ' + sys.executable + ' ' + filename)
    elif sys.platform == 'darwin':
        os.system('''osascript -e 'tell application "Terminal" to do script "''' + sys.executable + ' ' + filename + '"' + "'")
    elif _executable_exists('gnome-terminal'):
        # gnome-terminal is used on Ubuntu Linux:
        subprocess.call(['gnome-terminal', '--', sys.executable, TERMINAL_OPENER, filename])
    elif _executable_exists('lxterminal'):
        # LXTerminal is used on Raspberry Pis:
        subprocess.call(['lxterminal', '-e', sys.executable, TERMINAL_OPENER, filename])


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
    i = CURRENT_SELECTED_INDEX

    # Restore the file from the original one in the originalFiles.zip backup.
    originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, 'originalFiles.zip'), 'r')
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
