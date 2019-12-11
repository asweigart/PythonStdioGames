# Soroban, by Al Sweigart al@inventwithpython.com
# A simulation of a Japanese abacus calculator tool.
# More info at: https://en.wikipedia.org/wiki/Soroban
__version__ = 1

def drawAbacus(number):
    numberList = list(str(number).zfill(10))

    hasBead = []

    # Top heaven row has a bead for digits 0, 1, 2, 3, and 4.
    for i in range(10):
        hasBead.append(numberList[i] in '01234')

    # Bottom heaven row has a bead for digits 5, 6, 7, 8, and 9.
    for i in range(10):
        hasBead.append(numberList[i] in '56789')

    # 1st (topmost) earth row has a bead for all digits except 0.
    for i in range(10):
        hasBead.append(numberList[i] in '12346789')

    # 2nd earth row has a bead for digits 2, 3, 4, 7, 8, and 9.
    for i in range(10):
        hasBead.append(numberList[i] in '234789')

    # 3rd earth row has a bead for digits 0, 3, 4, 5, 8, and 9.
    for i in range(10):
        hasBead.append(numberList[i] in '034589')

    # 4th earth row has a bead for digits 0, 1, 2, 4, 5, 6, and 9.
    for i in range(10):
        hasBead.append(numberList[i] in '014569')

    # 5th earth row has a bead for digits 0, 1, 2, 5, 6, and 7.
    for i in range(10):
        hasBead.append(numberList[i] in '012567')

    # 6th earth row has a bead for digits 0, 1, 2, 3, 5, 6, 7, and 8.
    for i in range(10):
        hasBead.append(numberList[i] in '01235678')

    # Convert these True or False values into O or | characters.
    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('O')
        else:
            abacusChar.append('|')

    # Draw the abacus with the O/| characters.
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*abacusChar + numberList))


def drawControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


def main():
    print('SOROBAN - The Japanese Abacus')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    abacusNumber = 0 # This is the number represented on the abacus.

    while True: # Main program loop.
        drawAbacus(abacusNumber)
        drawControls()

        commands = input()
        if commands == 'quit':
            # Quit the program:
            break
        elif commands.isdecimal():
            # Set the abacus number:
            abacusNumber = int(commands)
        else:
            # Handle increment/decrement commands:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # The abacus can't show negative numbers:
        if abacusNumber < 0:
            abacusNumber = 0 # Change any negative numbers to 0.
        # At this point, go back to the start of the main program loop.

if __name__ == '__main__':
    main()
