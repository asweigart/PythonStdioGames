# How to Keep an Idiot Busy for Hours, by Al Sweigart al@inventwithpython.com

while True: # Main program loop.
    print('Would you like to know how to keep an idiot busy for hours?')
    response = input() # Get the user's response.
    if response.lower() == 'no' or response.lower() == 'n':
        break # If "no", break out of this loop.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue # If "yes", continue to the start of this loop.
    print('"%s" is not a valid yes/no response.' % (response))

print('Thank you. Have a nice day!')