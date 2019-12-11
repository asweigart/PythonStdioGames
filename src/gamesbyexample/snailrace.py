# Snail Race, by Al Sweigart al@inventwithpython.com
# Fast-paced snail racing action!
__version__ = 1

# TODO finish

import random, time, sys

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 12
FINISH_LINE = 40 # (!) Try modifying this number.

print('''SNAIL RACE
By Al Sweigart al@inventwithpython.com
''')

# Ask how many snails to race:
while True: # Keep asking until the player enters a number.
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input()
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)

# Enter the names of each snail:
snailNames = [] # List of the string snail names.
print('(Names must be at most', MAX_NAME_LENGTH, 'characters.)')
for i in range(1, numSnailsRacing + 1):
    while True: # Keep asking until the player enters a valid name.
        print('Enter snail #' + str(i) + "'s name:")
        name = input()
        if len(name) == 0:
            print('Please enter a name.')
        elif len(name) > MAX_NAME_LENGTH:
            print('Choose a shorter name.')
        elif name in snailNames:
            print('Choose a name that has not already been used.')
        else:
            break # The entered name is acceptable.

    snailNames.append(name)

print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - 1) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName)
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5)

while True:

    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    time.sleep(0.5)
    print('\n' * 40)
    print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName)

        print(('.' * snailProgress[snailName]) + '@v')



