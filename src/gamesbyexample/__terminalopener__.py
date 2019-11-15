# This file lets the gamesbyexample launcher run the Python script in a
# new terminal window, which will remain open after the Python script
# terminates. (In this example, it's named game.py.)

# For Ubuntu Linux, this Python script is called via:
#       gnome-terminal -- python3 __terminalopener__.py game.py
# For Raspberry Pi, this Python script is called via:
#       lxterminal -e python3 __terminalopener__.py game.py

import subprocess, sys, os

# First, this script runs the Python script that it's directed to ("game.py"):
subprocess.call(['python3', sys.argv[1]])

# Second, this script runs a shell so that the terminal window stays open after
# the "game.py" Python script terminates:
if 'SHELL' in os.environ:
    subprocess.call([os.environ['SHELL']])
else:
    # Let's just assume the user's shell is bash:
    subprocess.call(['bash'])
