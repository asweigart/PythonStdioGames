# Games By Example
# By Al Sweigart al@inventwithpython.com

__version__ = '0.1.2'

# TODO - check if the support files have been changed and let the user undo changes.




import sys, os, subprocess, zlib, zipfile, webbrowser, random

from .__programdata__ import PROGRAMS, SUPPORT_FILES

from tkinter import *
from tkinter import font
from tkinter import ttk

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))

# Sort the programs in "pygame_games/" without considering the folder name:
PROGRAMS.sort(key=lambda x: os.path.basename(x['filename']))

# TODO - add code that checks for a corrupted _originalFiles.zip file. Disable the "undo changes" button in that case.

# Check for any missing files and reload them from the _originalFiles.zip file:
for program in PROGRAMS:
    if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, program['filename'])):
        # Restore the file from the original one in the _originalFiles.zip backup.
        originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
        originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)

# TODO - unpack support files if they're missing
#for supportFiles in SUPPORT_FILES.values():
#    for supportFile in supportFiles:
#        if not os.path.exists(os.path.join(FOLDER_OF_THIS_FILE, supportFile)):
#            # Restore the file from the original one in the _originalFiles.zip backup.
#            originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
#            originalFilesZipFile.extract(program['filename'], FOLDER_OF_THIS_FILE)


def _executable_exists(name):
    # Find out if an executable program named `name` is reachable:
    return subprocess.call(['which', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def programSelect(*args):
    global CURRENT_SELECTED_INDEX, programListbox, descTextarea, undoChangesBtnSV, undoChangesButton
    # If, for some reason, nothing is currently selected in the listbox of programs, do nothing:
    if len(programListbox.curselection()) == 0:
        return

    i = CURRENT_SELECTED_INDEX = programListbox.curselection()[0]

    descTextarea.configure(state='normal')
    descTextarea.delete('1.0', END)
    filename = os.path.join(FOLDER_OF_THIS_FILE, PROGRAMS[i]['filename'])

    # Set the text in the text box to the program name and description:
    programNameInListbox = PROGRAMS[i]['name']
    if 'pygame_games/' in programNameInListbox:
        programNameInListbox = programNameInListbox[len('pygame_games/'):]
    text = programNameInListbox + '\n\n' + PROGRAMS[i]['desc'] + '\n'
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
    TERMINAL_OPENER_FILENAME = os.path.join(FOLDER_OF_THIS_FILE, '__terminalopener__.py')
    CRASH_DETECTOR_FILENAME = os.path.join(FOLDER_OF_THIS_FILE, '__crashdetector__.py')

    # Figure out which program to run to open a new terminal window and then run the .py file:
    if sys.platform == 'win32':
        # 'start cmd' opens a new Command Prompt terminal window
        # '/K' tells the Command Prompt to run this command:
        # We want to run the same Python executable that is running this __init__.py script.
        # That Python should run __crashdetector__.py, with __version__ and filename as arguments
        # Crash detector will run filename as a Python script, and __version__ is used in the debug output if that program crashes.

        #os.system('start cmd /K ' + sys.executable + ' ' + CRASH_DETECTOR_FILENAME + ' ' + __version__ + ' ' + filename)
        # If we run the following line instead of the previous, Ctrl-C will work on Windows but we don't get crash reporting.
        os.system('start cmd /K ' + sys.executable + ' ' + filename)
    elif sys.platform == 'darwin':
        os.system('''osascript -e 'tell application "Terminal" to do script "''' + sys.executable + ' ' + CRASH_DETECTOR_FILENAME + ' ' + __version__ + ' ' + filename + '"' + "'")
    elif _executable_exists('gnome-terminal'):
        # gnome-terminal is used on Ubuntu Linux:
        subprocess.call(['gnome-terminal', '--', sys.executable, TERMINAL_OPENER_FILENAME, __version__, filename])
    elif _executable_exists('lxterminal'):
        # LXTerminal is used on Raspberry Pis:
        subprocess.call(['lxterminal', '-e', sys.executable, TERMINAL_OPENER_FILENAME, __version__, filename])


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
    global undoChangesBtnSV, undoChangesButton
    i = CURRENT_SELECTED_INDEX

    # Restore the file from the original one in the _originalFiles.zip backup.
    originalFilesZipFile = zipfile.ZipFile(os.path.join(FOLDER_OF_THIS_FILE, '_originalFiles.zip'), 'r')
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
    global root
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

    # Remove the "pygame_games/" part of the filename for the purposes of listing games in the listbox.
    programNamesInListbox = [d['filename'][len('pygame_games/'):] if 'pygame_games/' in d['filename'] else d['filename'] for d in PROGRAMS]
    #programNamesInListbox.sort() # Re-alphabetize them.

    filenameSV = StringVar(value=programNamesInListbox)
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

    # Select a random item in the list box by default so that it's not
    # always the same program when it starts up, to encourage discoverability of various programs:
    #programListbox.focus()
    programListbox.select_set(random.randint(0, len(PROGRAMS) - 1))
    #programListbox.focus()
    programListbox.event_generate("<<ListboxSelect>>")

    root.bind('<Escape>', quitLauncher) # Bind Esc key to quit the program.
    root.mainloop()


if __name__ == '__main__':
    main()
