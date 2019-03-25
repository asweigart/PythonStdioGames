# Switch Switch by Al Sweigart, al@inventwithpython.com
import random, sys

NUMBER_OF_SWITCHES = 6
assert 2 <= NUMBER_OF_SWITCHES <= 10

switches = ['X'] * NUMBER_OF_SWITCHES
connections = list(range(NUMBER_OF_SWITCHES))
while True:
    random.shuffle(connections)

    # Check for odd-numbered loops. Valid puzzles can only have even-numbered loops.
    validPuzzle = True
    for startingSwitch in range(NUMBER_OF_SWITCHES):
        currentSwitch = startingSwitch
        hops = 0
        while hops == 0 or currentSwitch != startingSwitch:
            currentSwitch = connections[currentSwitch]
            hops += 1
        if hops % 2 == 1:
            # This is an odd-numbered loop, so the puzzle is invalid
            validPuzzle = False
            break
    if validPuzzle:
        break

while True: # Main game loop.
    print(' '.join(switches))
    for i in range(NUMBER_OF_SWITCHES):
        print('%s ' % (i), end='')
    print()

    move = input('Switch to toggle (0-%s): ' % (NUMBER_OF_SWITCHES - 1))
    if move.lower() == 'quit':
        sys.exit()

    if not move.isdigit() or not (0 <= int(move) < NUMBER_OF_SWITCHES):
        continue

    move = int(move)
    print('  Toggling switch #%s also toggled switch #%s.' % (move, connections[move]))

    #move = random.randint(0, NUMBER_OF_SWITCHES - 1)

    if switches[move] == 'X':
        switches[move] = 'O'
    elif switches[move] == 'O':
        switches[move] = 'X'

    if switches[connections[move]] == 'X':
        switches[connections[move]] = 'O'
    elif switches[connections[move]] == 'O':
        switches[connections[move]] = 'X'

    if switches == ['O'] * NUMBER_OF_SWITCHES:
        print(' '.join(['O'] * NUMBER_OF_SWITCHES))
        print('You solved the puzzle!')
        break
