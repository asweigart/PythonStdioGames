"""Lucky Stars, by Al Sweigart al@inventwithpython.com
A "press your luck" game where you roll dice to gather as many stars
as possible. You can roll as many times as you want, but if you roll
three skulls you lose all your stars.

Inspired by the Zombie Dice game from Steve Jackson Games.
This and other games are available at https://nostarch.com/XX
Tags: large, game, multiplayer"""

import random

# Set up the constants:
GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
even.
""")

print('How many players are there?')
while True:  # Loop until the user enters a number.
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Please enter a number larger than 1.')

playerNames = []  # List of strings of player names.
playerScores = {}  # Keys are player names, values are integer scores.
for i in range(numPlayers):
    while True:  # Keep looping until a name is entered.
        print('What is player #' + str(i + 1) + '\'s name?')
        response = input('> ')
        if response != '' and response not in playerNames:
            playerNames.append(response)
            playerScores[response] = 0
            break
        print('Please enter a name.')
print()

turn = 0  # The player at playerNames[0] will go first.
# (!) Uncomment to let a player named 'Al' start with three points:
#playerScores['Al'] = 3
endGameWith = None
while True:  # Main game loop.
    # Display everyone's score:
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # All but the last player have commas separating their names.
            print(', ', end='')
    print('\n')

    # Start the number of collected stars and skulls at 0.
    stars = 0
    skulls = 0
    # A cup has 6 gold, 4 silver, and 3 bronze dice:
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []  # Your hand starts with no dice.
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True:  # Each iteration of this loop is rolling the dice.
        print()

        # Check that there's enough dice left in the cup:
        if (3 - len(hand)) > len(cup):
            # End this turn because there are not enough dice:
            print('There aren\'t enough dice left in the cup to '
                + 'continue ' + playerNames[turn] + '\'s turn.')
            break

        # Pull dice from the cup until you have 3 in your hand:
        random.shuffle(cup)  # Shuffle the dice in the cup.
        while len(hand) < 3:
            hand.append(cup.pop())

        # Roll the dice:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                # Roll a gold die (3 stars, 2 questions, 1 skull):
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
                # Roll a silver die (2 stars, 2 questions, 2 skulls):
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
                # Roll a bronze die (1 star, 2 questions, 3 skulls):
                if roll == 1:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1

        # Display roll results:
        for lineNum in range(FACE_HEIGHT):
            for diceNum in range(3):
                print(rollResults[diceNum][lineNum] + ' ', end='')
            print()  # Print a newline.

        # Display the type of dice each one is (gold, silver, bronze):
        for diceType in hand:
            print(diceType.center(FACE_WIDTH) + ' ', end='')
        print()  # Print a newline.

        print('Stars collected:', stars, '  Skulls collected:', skulls)

        # Check if they've collected 3 or more skulls:
        if skulls >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(playerNames[turn] + ', do you want to roll again? Y/N')
        while True:  # Keep asking the player until they enter Y or N:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response.startswith('N'):
            print(playerNames[turn], 'got', stars, 'stars!')
            # Add stars to this player's point total:
            playerScores[playerNames[turn]] += stars

            # Check if they've reached 13 or more points:
            if (endGameWith == None
                and playerScores[playerNames[turn]] >= 13):
                # Since this player reached 13 points, play one more
                # round for all other players:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
            input('Press Enter to continue...')
            break

        # Discard the stars and skulls, but keep the question marks:
        nextHand = []
        for i in range(3):
            if rollResults[i] == QUESTION_FACE:
                nextHand.append(hand[i])  # Keep the question marks.
        hand = nextHand

    # Move on to the next player's turn:
    turn = (turn + 1) % numPlayers

    # If the game has ended, break out of this loop:
    if endGameWith == playerNames[turn]:
        break  # End the game.

print('The game has ended...')

# Display everyone's score:
print()
print('SCORES: ', end='')
for i, name in enumerate(playerNames):
    print(name + ' = ' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        # All but the last player have commas separating their names.
        print(', ', end='')
print('\n')

# Find out who the winners are:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        # This player has the highest score:
        highestScore = score
        winners = [name]  # Overwrite any previous winners.
    elif score == highestScore:
        # This player is tied with the highest score.
        winners.append(name)

if len(winners) == 1:
    # There is only one winner:
    print('The winner is ' + winners[0] + '!!!')
else:
    # There are multiple tied winners:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
