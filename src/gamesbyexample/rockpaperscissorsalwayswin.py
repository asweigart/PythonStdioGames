"""Rock-Paper-Scissors (Always Win), by Al Sweigart al@inventwithpython.com
A hand game of luck, except you cannot lose.
Tags: tiny, game, humor"""
__version__ = 0
import time, sys

print('''ROCK, PAPER, SCISSORS
By Al Sweigart al@inventwithpython.com

- Rock beats scissors.
- Paper beats rocks.
- Scissors beats paper.
''')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # Main game loop.
    while True:  # Keep asking until player enters R, P, S, or Q.
        print('{} Wins, 0 Losses, 0 Ties'.format(wins))
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            sys.exit()

        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        else:
            print('Type one of R, P, S, or Q.')

    # Display what the player chose:
    if playerMove == 'R':
        print('ROCK versus...')
    elif playerMove == 'P':
        print('PAPER versus...')
    elif playerMove == 'S':
        print('SCISSORS versus...')

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    if playerMove == 'R':
        print('SCISSORS')
    elif playerMove == 'P':
        print('ROCK')
    elif playerMove == 'S':
        print('PAPER')

    time.sleep(0.5)

    print('You win!')
    wins = wins + 1
    # At this point, go back to the start of the main game loop.
