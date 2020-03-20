"""Eeny-Meeny-Miny-Moe, by Al Sweigart al@inventwithpython.com

An elimination game for multiple players. Press Ctrl-C to stop.
More info at https://en.wikipedia.org/wiki/Eeny,_meeny,_miny,_moe
More info at https://en.wikipedia.org/wiki/Josephus_problem
Tags: short, game, multiplayer"""
__version__ = 0

import random, time, sys

SCREEN_WIDTH = 60
RHYME = ['EENY', 'MEENY', 'MINY', 'MOE', 'CATCH A', 'TIGER', 'BY THE',
         'TOE', 'IF IT', 'HOLLERS', 'LET IT', 'GO', 'EENY', 'MEENY',
         'MINY', 'MOE']
NAMES = ['James', 'John', 'Robert', 'Michael', 'William', 'David',
         'Richard', 'Charles', 'Mary', 'Patricia', 'Linda', 'Barbara',
         'Elizabeth', 'Jennifer', 'Maria', 'Susan']
random.shuffle(NAMES)

print('Eeny, Meeny, Miny, Moe')
print('By Al Sweigart al@inventwithpython.com')
print()

# Get the players' names:
playerNames = []
while True:
    print('Enter a player\'s name, or enter nothing when finished:')
    playerName = input().upper()
    if playerName != '':  # Player can enter anything except a blank name.
        playerNames.append(playerName)
    else:
        break
    # At this point, go back to the start of the loop.

# Get the total number of participants:
while True:
    numPlayers = len(NAMES) + len(playerNames)
    print('How many participants total (2-' + str(numPlayers) + '):')
    try:
        numParticipants = int(input())
    except ValueError:
        continue  # Player entered non-integer; ask again.
    if 2 <= numParticipants <= len(NAMES) + len(playerNames):
        break
    # At this point, go back to the start of the loop.

# Get the position of the player:
participants = NAMES[: numParticipants - len(playerNames)]
for playerName in playerNames:
    while True:
        places = str(len(participants) + 1)
        print('Where does ' + playerName + ' go? (1-' + places + '):')
        try:
            position = int(input())
        except ValueError:
            continue  # Player entered non-integer; ask again.
        if 1 <= position <= len(participants) + 1:
            participants.insert(position - 1, playerName)
            break
        # At this point, go back to the start of the loop.

# Start the elimination process:
startPosition = 0
while len(participants) > 1:  # Main program loop.
    # Figure out how many names to put on each row:
    rows = ['']
    for name in participants:
        if len(rows[-1]) + len(name) > SCREEN_WIDTH:
            # Start a new row:
            rows.append('')

        rows[-1] += name + ' '

    # Run through one round of elimination:
    for rhymeWordIndex, rhymeWord in enumerate(RHYME):
        i = (rhymeWordIndex + startPosition) % len(participants)
        currentPerson = participants[i]
        for row in rows:
            # Include a space at the end, so we don't match names with
            # the same prefix, i.e. 'Doug' and 'Douglas':
            if currentPerson + ' ' in row:
                print(' ' * row.index(currentPerson) + rhymeWord)
            else:
                print()
            print(row)
        print('\n')
        time.sleep(0.5)
    startPosition = (rhymeWordIndex + startPosition) % len(participants)

    # Remove the eliminated person from the participants list:
    print(currentPerson.upper() + ' HAS BEEN ELIMINATED.')
    participants.remove(currentPerson)
    if currentPerson in playerNames:
        # If it's a player, remove them from playerNames:
        playerNames.remove(currentPerson)

    # If all players have been eliminated, end the game:
    if len(playerNames) == 0:
        print('ALL PLAYERS HAVE BEEN ELIMINATED.')
        print()
        print('Thanks for playing!')
        sys.exit()

    # Pause before starting the next elimination round.
    try:
        input('Press Enter to continue, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
    # At this point, go back to the start of the main program loop.

# Declare the winner:
print(participants[0] + ' IS THE WINNER!!!')
