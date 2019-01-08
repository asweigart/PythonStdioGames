# Rainbow, by Al Sweigart al@inventwithpython.com
# Shows a simple rainbow animation.

from colorama import init, Fore
import time

init() # Intialize the color system.

indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

while True:
    print(' ' * indent + Fore.RED + '##' + Fore.YELLOW + '##' + Fore.GREEN + '##' + Fore.BLUE + '##' + Fore.CYAN + '##' + Fore.MAGENTA + '##') # Display the rainbow.

    if indentIncreasing:
        # Increase the number of spaces:
        indent = indent + 1
        if indent == 20:
            # Change direction:
            indentIncreasing = False
    else:
        # Decrease the number of spaces:
        indent = indent - 1
        if indent == 0:
            # Change direction:
            indentIncreasing = True

    time.sleep(0.05) # Add a slight pause.
