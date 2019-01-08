# Rainbow 2, by Al Sweigart al@inventwithpython.com
# Shows a simple squiggle rainbow animation.

from colorama import init, Fore
import time
import random

init() # Intialize the color system.

indent = 10 # How many spaces to indent.


while True:
    print(' ' * indent + Fore.RED + '##' + Fore.YELLOW + '##' + Fore.GREEN + '##' + Fore.BLUE + '##' + Fore.CYAN + '##' + Fore.MAGENTA + '##') # Display the rainbow.

    if random.randint(0, 1) == 0:
        # Increase the number of spaces:
        indent = indent + 1
        if indent > 20:
            indent = 20
    else:
        # Decrease the number of spaces:
        indent = indent - 1
        if indent < 0:
            indent = 0

    time.sleep(0.05) # Add a slight pause.
