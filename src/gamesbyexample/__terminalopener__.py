# This file lets the gamesbyexample launcher run the Python game script
# in a new terminal window, which will remain open after the Python
# script terminates. Though first, it runs __crashdetector__.py which
# runs the game, and can detect if the game crashes.

import subprocess, sys, os

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
CRASH_DETECTOR = os.path.join(FOLDER_OF_THIS_FILE, '__crashdetector__.py')

# First, this script runs the crash detector to run the Python script:
try:
    exitCode = subprocess.call([sys.executable, CRASH_DETECTOR, sys.argv[1], sys.argv[2]])
except KeyboardInterrupt, EOFError:
    exitCode = 0 # Do nothing if Ctrl-C was pressed to exit the game.



# Pygame games only leave the terminal window open if there was no crash.
if 'pygame_games/' in programToLaunch and exitCode == 0:
    sys.exit()

# Second, this script runs a shell so that the terminal window stays open
# after the programToLaunch Python script terminates. (Otherwise, any
# output that the game printed just before terminating will be lost when
# the terminal window closes.)
if 'SHELL' in os.environ:
    subprocess.call([os.environ['SHELL']])
else:
    # Let's just assume the user's shell is bash:
    subprocess.call(['bash'])
