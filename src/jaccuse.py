# J'ACCUSE!, by Al Sweigart al@inventwithpython.com
# Inspired by Homestar Runner's "Where's an Egg?" game
# Play the original Flash game at:
# https://homestarrunner.com/videlectrix/wheresanegg.html
# More info at: http://www.hrwiki.org/wiki/Where's_an_Egg%3F

import time, random, sys

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300 # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
assert len(set(PLACE_FIRST_LETTERS.keys())) == len(PLACES) # First letters must be unique.
assert len(SUSPECTS) == len(ITEMS) == len(PLACES)

knownSuspectsAndItems = []
visitedPlaces = {} # Keys=places, values=strings of the suspect & item there.
currentLocation = 'TAXI' # Start the game at the taxi.
accusedSuspects = [] # Accused suspects won't offer clues.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3 # You can accuse up to 3 people.
culprit = random.choice(SUSPECTS)

# Common indexes link these; e.g. SUSPECTS[0] and ITEMS[0] are at PLACES[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# Create data structures for clues the truth-tellers give about each item and suspect:
clues = {} # Keys=suspects being asked for a clue, value="clue dictionary".
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue # Skip the liars for now.

    clues[interviewee] = {} # This "clue dictionary" has keys=items & suspects, value=the clue given.
    clues[interviewee]['debug_liar'] = False # Useful for debugging.
    for item in ITEMS: # Select clue about each item.
        if random.randint(0, 1) == 0: # Tells where the item is:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else: # Tells who has the item:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS: # Select clue about each suspect.
        if random.randint(0, 1) == 0: # Tells where the suspect is:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else: # Tells what item the suspect has:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

# Create data structures for clues the liars give about each item and suspect:
for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue # We've already handled the truth-tellers.

    clues[interviewee] = {} # This "clue dictionary" has keys=items & suspects, value=the clue given.
    clues[interviewee]['debug_liar'] = True # Useful for debugging.

    # This interviewee is a liar and gives wrong clues:
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True: # Select a random (wrong) place clue.
                clues[interviewee][item] = random.choice(PLACES) # Lies about where the item is.
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                     break # Break out of the loop once a wrong clue is selected.
        else:
            while True: # Select a random (wrong) suspect clue.
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                     break # Break out of the loop if wrong info was selected.
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True: # Select a random (wrong) place clue.
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                     break # Break out of the loop once a wrong clue is selected.
        else:
            while True: # Select a random (wrong) item clue.
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                     break # Break out of the loop once a wrong clue is selected.

# Create the data structures for clues given when asked about Zophie:
zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            # They tell you who has Zophie.
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                # Select a (wrong) suspect clue.
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                     break # Break out of the loop if wrong info was selected.

    elif kindOfClue == 2:
        if interviewee not in liars:
            # They tell you where Zophie is.
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Select a (wrong) place clue.
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                     break # Break out of the loop if wrong info was selected.
    elif kindOfClue == 3:
        if interviewee not in liars:
            # They tell you what item Zophie is near.
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                # Select a (wrong) item clue.
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                     break # Break out of the loop if wrong info was selected.

# EXPERIMENT: Uncomment this code to view the clue data structures:
#import pprint
#pprint.pprint(clues)
#pprint.pprint(zophieClues)
#print(f'culprit={culprit}')

# START OF THE GAME
print("J'ACCUSE! (a mystery game)")
print('By Al Sweigart al@inventwithpython.com')
print('Inspired by Homestar Runner\'s "Where\'s an Egg?" game')
print()
print('You are the world-famous detective, Mathilde Camus.')
print('ZOPHIE THE CAT has gone missing, and you must sift through the clues.')
print('Suspects either always tell lies, or always tell the truth. Will you')
print('find ZOPHIE THE CAT in time and accuse the guilty party?')
print()
input('Press Enter to begin...')



startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True: # Main game loop.
    if time.time() > endTime or accusationsLeft == 0:
        # Handle "game over" condition:
        if time.time() > endTime:
            print('You have run out of time!')
        elif accusationsLeft == 0:
            print('You have accused too many innocent people!')
        culpritIndex = SUSPECTS.index(culprit)
        print(f'It was {culprit} at the {PLACES[culpritIndex]} with the {ITEMS[culpritIndex]} who catnapped her!')
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print(f'Time left: {minutesLeft} min, {secondsLeft} sec')

    if currentLocation == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = ''
            if place in visitedPlaces:
                placeInfo = visitedPlaces[place]
            print(f'({place[0]}){place[1:]} {" " * (LONGEST_PLACE_NAME_LENGTH - len(place))}{placeInfo}')
        while True: # Keep asking until a valid response is given.
            response = input('> ').upper()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue # Go back to the start of the main game loop.

    # At a place; player can ask for clues.
    print(f'  You are at the {currentLocation}.')
    currentLocationIndex = PLACES.index(currentLocation)
    thePersonHere = SUSPECTS[currentLocationIndex]
    theItemHere = ITEMS[currentLocationIndex]
    print(f'  {thePersonHere} with the {theItemHere} is here.')

    # Add the suspect and item at this place to our list of known suspects and items.
    if thePersonHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(thePersonHere)
    if ITEMS[currentLocationIndex] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIndex])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = f'({thePersonHere.lower()}, {theItemHere.lower()})'

    # If the player has accused this person wrongly before, they won't give clues.
    if thePersonHere in accusedSuspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue # Go back to the start of the main game loop.

    # Display menu of known suspects & items to ask about:
    print()
    print(f'(J) "J\'ACCUSE!" ({accusationsLeft} accusations left)')
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspectOrItem in enumerate(knownSuspectsAndItems):
        print(f'({i + 1}) Ask about {suspectOrItem}')

    while True: # Keep asking until a valid response is given.
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <= len(knownSuspectsAndItems)):
            break

    if response == 'J': # Player accuses this suspect.
        accusationsLeft -= 1 # Use up an accusation.
        if thePersonHere == culprit:
            # You've accused the correct suspect.
            print('You\'ve cracked the case, Detective!')
            print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print(f'Good job! You solved it in {minutesTaken} min, {secondsTaken} sec.')
            sys.exit()
        else:
            # You've accused the wrong suspect.
            accusedSuspects.append(thePersonHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z': # Player asks about Zophie.
        if thePersonHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif thePersonHere in zophieClues:
            print(f'  They give you this clue: "{zophieClues[thePersonHere]}"')
            # Add non-place clues to the list of known things:
            if zophieClues[thePersonHere] not in knownSuspectsAndItems and zophieClues[thePersonHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[thePersonHere])

    elif response == 'T': # Player goes back to the taxi.
        currentLocation = 'TAXI'
        continue # Go back to the start of the main game loop.

    else: # Player asks about a suspect or item.
        thingBeingAskedAbout = knownSuspectsAndItems[int(response) - 1]
        if thingBeingAskedAbout in (thePersonHere, theItemHere):
            print('  They give you this clue: "No comment."')
        else:
            print(f'  They give you this clue: "{clues[thePersonHere][thingBeingAskedAbout]}"')
            # Add non-place clues to the list of known things:
            if clues[thePersonHere][thingBeingAskedAbout] not in knownSuspectsAndItems and clues[thePersonHere][thingBeingAskedAbout] not in PLACES:
                knownSuspectsAndItems.append(clues[thePersonHere][thingBeingAskedAbout])

    input('Press Enter to continue...')
