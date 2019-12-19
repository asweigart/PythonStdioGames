import sys, os, datetime, re

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

# Change the cwd to the folder that contains the program.
os.chdir(os.path.dirname(programToLaunch))

if 'pygame_games/' in programToLaunch:
    print('(On Raspberry Pis, close this window to shut down the game.')

# Technically, any Ctrl-C should be caught here, making catching it
# unnecessary for the .py files unless they aren't run from this launcher.
try:
    exitCode = os.system(sys.executable + ' ' + programToLaunch)
except KeyboardInterrupt, EOFError:
    exitCode = 0 # Do nothing if Ctrl-C was pressed to exit the game.

if exitCode != 0 and sys.platform != 'darwin': # NOTE: We are currently disabling this on macOS because it keeps reporting keyboard interrupts, etc.

    # Get the program's __version__ variable:
    with open(programToLaunch) as fo:
        content = fo.read()
        mo = re.search(r'__version__ = (\d)+', content)
        if mo is None:
            programVersion = 'N/A'
        else:
            programVersion = mo.group(1)

    sys.stderr.write('''

* * * * * CRASH DETECTED! * * * * *

You can help fix this by reporting it. Go to this website:
  https://github.com/asweigart/pythonstdiogames/issues

...and click the "New Issue" button. (You need a GitHub account to do this.
It is free to sign up. Or, you can email me at al@inventwithpython.com)

NOTE!!! If the error is KeyboardInterrupt, EOFError, or ModuleNotFoundError,
you don't need to report it. Just disregard this message.

In your issue report, copy/paste the above "Traceback" along with this text:
           Program: {}
   Program Version: {}
  Launcher Version: {}
          Platform: {}
    Python Version: {}
        Executable: {}
         Timestamp: {}

'''.format(programToLaunch, programVersion, launcherVersion, sys.platform, sys.version, sys.executable, datetime.datetime.now()))
    sys.exit(1) # Exit code of 1 signals to __terminalopener__.py to leave it open even if we were running a Pygame game.