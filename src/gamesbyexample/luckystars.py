"""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice to gather as many stars
as possible. You can roll as many times as you want, but if you roll
three skulls you lose all your stars.

Inspired by the Zombie Dice game from Steve Jackson games.
Tags: game, multiplayer"""

# TODO - add more comments
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

playerNames = []
playerScores = {}
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

turn = 0
# (!) Uncomment to let a player named 'Al' start with three points:
#playerScores['Al'] = 3
endGameWith = None
while True:  # Main game loop.
    # Display everyone's score:
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + '=' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            print(', ', end='')  # Print a comma except for the last player.
    print()

    stars = 0
    skulls = 0
    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True:  # Each iteration of this loop is rolling the dice.
        print()

        # Check that there's enough dice left in the cup:
        if (3 - len(hand)) > len(cup):
            # End this turn because there are not enough dice:
            print('There aren\'t enough dice left in the cup to continue ' + playerNames[turn] + '\'s turn.')
            break

        # Pull 3 dice and random from the cup:
        random.shuffle(cup)
        while len(hand) < 3:
            hand.append(cup.pop())

        # Roll the dice:
        rollResults = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                if 1 <= roll <= 3:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == SILVER:
                if 1 <= roll <= 2:
                    rollResults.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    rollResults.append(QUESTION_FACE)
                else:
                    rollResults.append(SKULL_FACE)
                    skulls += 1
            if dice == BRONZE:
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

        print('Do you want to roll again? Y/N')
        while True:  # Keep asking the player until they enter Y or N:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Please enter Yes or No.')

        if response.startswith('N'):
            # Add stars to this player's point total:
            playerScores[playerNames[turn]] += stars

            # Check if they've reached 13 or more points:
            if endGameWith == None and playerScores[playerNames[turn]] >= 13:
                # Play one more round until it's this player's turn again:
                print('\n\n' + ('!' * 60))
                print(playerNames[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                endGameWith = playerNames[turn]
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
print('SCORES: ', end='')
for i, name in enumerate(playerNames):
    print(name + '=' + str(playerScores[name]), end='')
    if i != len(playerNames) - 1:
        print(', ', end='')  # Print a comma except for the last player.
print()

# Find out who is the winner:
highestScore = 0
winners = []
for name, score in playerScores.items():
    if score > highestScore:
        highestScore = score
        winners = [name]
    elif score == highestScore:
        winners.append(name)

if len(winners) == 1:
    # There is only one winner:
    print('The winner is ' + winners[0] + '!!!')
else:
    # There are multiple tied winners:
    print('The winners are: ' + ', '.join(winners))

print('Thanks for playing!')
