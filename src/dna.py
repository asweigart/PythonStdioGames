# DNA Anmation Demo by Al Sweigart
# Thanks to matoken for inspiration: https://asciinema.org/a/155441

import random
import time

# These are the individual rows of the DNA animation:
rows = [
    '         ##', # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',    # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

print('Press Ctrl-C or Ctrl-D to quit...')
time.sleep(2)
rowIndex = 0

while True: # Main animation loop.
    # Increment rowIndex to draw next row:
    rowIndex += 1
    if rowIndex == len(rows):
        rowIndex = 0

    # Row indexs 0 and 9 don't have nucleotides:
    if rowIndex == 0 or rowIndex == 9:
        print(rows[rowIndex])
        continue

    # Draw rows with nucleotides:
    if random.randint(0, 1) == 0:
        # Half of the time, let's use A and T nucleotides:
        if random.randint(0, 1) == 0:
            print(rows[rowIndex].format('A', 'T'))
        else:
            print(rows[rowIndex].format('T', 'A'))
    else:
        # The other half of the time, let's use C and G nucleotides:
        if random.randint(0, 1) == 0:
            print(rows[rowIndex].format('C', 'G'))
        else:
            print(rows[rowIndex].format('G', 'C'))

    time.sleep(0.15) # Add a slight pause.