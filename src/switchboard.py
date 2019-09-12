# Switchboard, by Al Sweigart, al@inventwithpython.com

# TODO - needs more comments

import random, sys

NUMBER_OF_SWITCHES = 6
assert 2 <= NUMBER_OF_SWITCHES <= 10

print('SWITCHBOARD')
print('By Al Sweigart, al@inventwithpython.com')
print()
print('Flip a switch to toggle it from X to O. Try to get all the switches')
print('to O. However, each switch is linked to another switch that it also')
print('toggles.')
print()

# Set up the switches to the X state and figure out which other switches
# they're linked to.
switches = ['X'] * NUMBER_OF_SWITCHES
connections = list(range(NUMBER_OF_SWITCHES))

while True:
    random.shuffle(connections) # Randomize the links.

    # A loop is made of switches that link back to a starting switch.
    # Check for loops with an odd-number length.
    # Valid puzzles can only have loops with even-numbered lengths.
    validPuzzle = True
    for startingSwitch in range(NUMBER_OF_SWITCHES):
        currentSwitch = startingSwitch
        loopLength = 0
        while loopLength == 0 or currentSwitch != startingSwitch:
            currentSwitch = connections[currentSwitch]
            loopLength += 1
        if loopLength % 2 == 1:
            # This is an odd-numbered loop, so the puzzle is invalid
            validPuzzle = False
            break # Break out of the for loop.
    if validPuzzle:
        break # Break out of the while loop.

while True: # Main game loop.
    print(' '.join(switches)) # Print the switch XO states.
    for i in range(NUMBER_OF_SWITCHES):
        print(f'{i} ', end='')
    print()

    response = input(f'Switch to toggle (0-{NUMBER_OF_SWITCHES - 1} or QUIT): ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not response.isdecimal() or not (0 <= int(response) < NUMBER_OF_SWITCHES):
        continue

    switchToToggle = int(response)
    print()
    print(f'Toggling switch #{switchToToggle} also toggled switch #{connections[switchToToggle]}.')

    #switchToToggle = random.randint(0, NUMBER_OF_SWITCHES - 1)

    # Toggle the selected switch:
    if switches[switchToToggle] == 'X':
        switches[switchToToggle] = 'O'
    elif switches[switchToToggle] == 'O':
        switches[switchToToggle] = 'X'

    # Toggle the switch connected to the selected switch:
    if switches[connections[switchToToggle]] == 'X':
        switches[connections[switchToToggle]] = 'O'
    elif switches[connections[switchToToggle]] == 'O':
        switches[connections[switchToToggle]] = 'X'

    if switches == ['O'] * NUMBER_OF_SWITCHES:
        print(' '.join(['O'] * NUMBER_OF_SWITCHES))
        print('You solved the puzzle!')
        break
