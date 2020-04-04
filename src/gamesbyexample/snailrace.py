"""Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
This and other games are available at https://nostarch.com/XX
Tags: short, artistic, game, multiplayer"""
__version__ = 0
import random, time, sys

# Set up the constants:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # (!) Try modifying this number.

print('''Snail Race, by Al Sweigart al@inventwithpython.com

    @v <-- snail

''')

# Ask how many snails to race:
while True:  # Keep asking until the player enters a number.
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)

# Enter the names of each snail:
snailNames = []  # List of the string snail names.
for i in range(1, numSnailsRacing + 1):
    while True:  # Keep asking until the player enters a valid name.
        print('Enter snail #' + str(i) + "'s name:")
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break  # The entered name is acceptable.
    snailNames.append(name)

# Display each snail at the start line.
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)  # The pause right before the race starts.

while True:  # Main program loop.
    # Pick random snails to move forward:
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        # Check if a snail has reached the finish line:
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    # (!) EXPERIMENT: Add a cheat here that increases a snail's progress
    # if it has your name.

    time.sleep(0.5)  # (!) EXPERIMENT: Try changing this value.

    # (!) EXPERIMENT: What happens if you comment this line out?
    print('\n' * 40)

    # Display the start and finish lines:
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    # Display the snails (with name tags):
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')
