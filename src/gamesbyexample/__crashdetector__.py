import sys, os, datetime, re

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

try:
  exitCode = os.system(sys.executable + ' ' + programToLaunch)
except KeyboardInterrupt:
  exitCode = 0 # Do nothing if Ctrl-C was pressed to exit the game.

if exitCode != 0:

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

In your issue report, copy/paste the above "Traceback" along with this text:
           Program: {}
   Program Version: {}
  Launcher Version: {}
          Platform: {}
    Python Version: {}
        Executable: {}
         Timestamp: {}

'''.format(programToLaunch, programVersion, launcherVersion, sys.platform, sys.version, sys.executable, datetime.datetime.now()))