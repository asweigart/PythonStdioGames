"""Idiot, by Al Sweigart al@inventwithpython.com

How to keep an idiot busy for hours. (This is a joke program.)"""
__version__ = 1

while True: # Main program loop.
    print('Would you like to know how to keep an idiot busy for hours?')
    response = input() # Get the user's response.
    if response.lower() == 'no' or response.lower() == 'n':
        break # If "no", break out of this loop.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue # If "yes", continue to the start of this loop.
    print('"{}" is not a valid yes/no response.'.format(response))
    # At this point, go back to the start of the main program loop.

print('Thank you. Have a nice day!')
