# Sevseg, a seven-segment display, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Seven-segment_display

"""
A labeled seven-segment display:
 __A__
|     |
F     B
|__G__|
|     |
E     C
|__D__|

Each digit in a seven-segment display:
 __       __   __        __   __  __   __   __
|  |   |  __|  __| |__| |__  |__    | |__| |__|
|__|   | |__   __|    |  __| |__|   | |__|  __|

"""

def getSevSegStr(number, zeros=0):
    number = str(number).zfill(zeros) # Convert to string in case it's an int or float.

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            # Render the decimal point:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue # Skip the space in between digits.
        elif numeral == '-':
            # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':
            # Render the 0:
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            # Render the 1:
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':
            # Render the 2:
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':
            # Render the 3:
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':
            # Render the 4:
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            # Render the 5:
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':
            # Render the 6:
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':
            # Render the 7:
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':
            # Render the 8:
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            # Render the 9:
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        # Add a space if this isn't the last numeral:
        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

# Uncomment these lines to see a demo:
#for i in range(100):
#    print(getSevSegStr(i, 2))