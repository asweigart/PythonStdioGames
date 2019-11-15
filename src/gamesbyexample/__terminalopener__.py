# This file lets the gamesbyexample launcher run the Python script in a
# new terminal window, which will remain open after the Python script
# terminates. Though first, it runs __crashdetector__.py which runs the
# game, and can detect if the game crashes.

import subprocess, sys, os

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
CRASH_DETECTOR = os.path.join(FOLDER_OF_THIS_FILE, '__crashdetector__.py')

# First, this script runs the crash detector to run the Python script:
subprocess.call([sys.executable, CRASH_DETECTOR, sys.argv[1], sys.argv[2]])

# Second, this script runs a shell so that the terminal window stays open after
# the programToLaunch Python script terminates:
if 'SHELL' in os.environ:
    subprocess.call([os.environ['SHELL']])
else:
    # Let's just assume the user's shell is bash:
    subprocess.call(['bash'])
