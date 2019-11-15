import sys, os, datetime

launcherVersion = sys.argv[1]
programToLaunch = sys.argv[2]

exitCode = os.system(sys.executable + ' ' + programToLaunch)

if exitCode != 0:
    print('''

* * * * * CRASH DETECTED! * * * * *

You can help fix this by reporting it. Go to this website:
  https://github.com/asweigart/pythonstdiogames/issues

...and click the "New Issue" button. (You need a GitHub account to do this.
It is free to sign up. Or, you can email me at al@inventwithpython.com)

In your issue report, copy/paste the above "Traceback" along with this text:
           Program: {}
  Launcher Version: {}
          Platform: {}
    Python Version: {}
        Executable: {}
         Timestamp: {}
'''.format(programToLaunch, launcherVersion, sys.platform, sys.version, sys.executable, datetime.datetime.now()))