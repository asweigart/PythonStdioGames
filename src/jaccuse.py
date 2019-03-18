# J'ACCUSE!, by Al Sweigart al@inventwithpython.com

import time, random, sys

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'MEREDITH J. COFFERS', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'ANIME TAPE', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['OLD BARN', 'DUCK POND', 'CITY HALL', 'COAT CHECK', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300 # 300 seconds (5 minutes) to solve the game.

assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
assert len(SUSPECTS) == len(ITEMS) == len(PLACES)

knownSuspects = []
knownItems = []
position = 'TAXI' # Start at the taxi.
accusedSuspects = []

liars = random.sample(SUSPECTS, random.randint(3, 4))
knowsWhereZophieIs = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)

random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {} # Keys are the suspects being asked for a clue, value is a "clue dictionary".

# Figure out what clues the truth-tellers give about each item and suspect:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue # We'll handle the liars' clues later.

    clues[interviewee] = {} # This "clue dictionary" has keys of items & suspects, value is the clue given.
    clues[interviewee]['liar'] = False
    for item in ITEMS: # Figure out what clue this person gives about each item.
        if random.randint(0, 1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(item)] # Tells where the item is.
        else:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)] # Tells who has the item.
    for suspect in SUSPECTS: # Figure out what clue this person gives about each suspect.
        if random.randint(0, 1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)] # Tells where the suspect is.
        else:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)] # Tells what item the suspect has.

# Figure out what clues the liars give about each item and suspect:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue # We've already handles the clues for truth-tellers.

    clues[interviewee] = {} # This "clue dictionary" has keys of items & suspects, value is the clue given.
    clues[interviewee]['liar'] = True
    for item in ITEMS: # Figure out what clue this person gives about each item.
        if random.randint(0, 1) == 0:
            while True:
                # Keep randomly selecting a place until a wrong place is selected.
                clues[interviewee][item] = random.choice(PLACES) # Lies about where the item is.
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                     break # Break out of the loop if wrong info was selected.
        else:
            while True:
                # Keep randomly selecting a suspect until a wrong suspect is selected.
                clues[interviewee][item] = random.choice(SUSPECTS) # Lies about who has the item is.
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                     break # Break out of the loop if wrong info was selected.
    for suspect in SUSPECTS: # Figure out what clue this person gives about each suspect.
        # This interviewee is a liar and gives wrong info.
        if random.randint(0, 1) == 0:
            while True:
                # Keep randomly selecting a place until a wrong place is selected.
                clues[interviewee][suspect] = random.choice(PLACES) # Lies about where the suspect is.
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                     break # Break out of the loop if wrong info was selected.
        else:
            while True:
                # Keep randomly selecting a suspect until a wrong suspect is selected.
                clues[interviewee][suspect] = random.choice(ITEMS) # Lies about what item the suspect has.
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                     break # Break out of the loop if wrong info was selected.


print("J'ACCUSE! (a mystery game)")
print()
print('You are world famous detective, Mathilde Camus.')
print('ZOPHIE THE CAT has gone missing, and you must sift')
print('through the clues and liars to find her.')
print('Will you find ZOPHIE THE CAT in time, and accuse')
print('the guilty party?')
print()
print('Press Enter to begin...')
input()

endTime = time.time() + TIME_TO_SOLVE

while True: # Main game loop.
    if time.time() > endTime or accusationsLeft == 0:
        # Handle "game over" condition:
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print('%s at %s with the %s had her!' % (culprit, PLACES[culpritIndex], ITEMS[culpritIndex]))
        print('Better luck next time, Detective.')
        sys.exit()

    print('You have %s seconds left to find ZOPHIE THE CAT.' % (int(endTime - time.time())))

    if position == 'TAXI':
        print('You are in your TAXI. Where do you want to go?')
        for i, place in enumerate(PLACES):
            print('%s. %s' % (i + 1, place))
        while True: # Keep asking until a valid response is given.
            response = input()
            if response.isdigit() and 0 < int(response) <= len(PLACES):
                break
        position = PLACES[int(response) - 1]
        continue # Go back to the start of the main game loop.

    # At a place; player can ask for clues.
    print('You are at the %s.' % position)
    positionIndex = PLACES.index(position)
    print('%s with the %s is here.' % (SUSPECTS[positionIndex], ITEMS[positionIndex]))

    # Add the suspect and item at this place to our list of known suspects and items.
    if SUSPECTS[positionIndex] not in knownSuspects:
        knownSuspects.append(SUSPECTS[positionIndex])
    if ITEMS[positionIndex] not in knownItems:
        knownItems.append(ITEMS[positionIndex])

    # Display menu of known suspects & items to ask about:
    print('J. "J\'ACCUSE!" (%s accusations left)' % (accusationsLeft))
    print('Z. Ask if they know where ZOPHIE THE CAT is.')
    print('T. Go back to the TAXI.')
    for i, knownSuspect in enumerate(knownSuspects):
        print('%s. Ask about %s' % (i + 1, knownSuspect))
    for i, knownItem in enumerate(knownItems):
        print('%s. Ask about the %s' % (i + 1 + len(knownSuspects), knownItem))

    while True: # Keep asking until a valid response is given.
        response = input()
        if response in 'JZT' or (response.isdigit() and 0 <= int(response) <= len(knownSuspects) + len(knownItems)):
            break

    if response == 'J':
        accusationsLeft -= 1
        if SUSPECTS[positionIndex] == culprit:
            # You've accused the correct suspect.
            print('You\'ve cracked the case, Detective!')
            print('It was %s who had catnapped ZOPHIE THE CAT.' % (culprit))
            print('Good job!')
            sys.exit()
        else:
            # You've accused the wrong suspect.
            pass # TODO

    elif response == 'Z':
        pass # TODO
    elif response == 'T':
        position = 'TAXI'
        continue # Go back to the start of the main game loop.




