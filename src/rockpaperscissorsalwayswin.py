# Rock, Paper, Scissors (except you always win), by Al Sweigart al@inventwithpython.com

import time

def runGame():
    wins = 0 # This variable keeps track of how many wins the player has.

    while True: # The main game loop.
        while True: # Keep asking until player enters R/P/S/Q.
            print('%s Wins, 0 Losses, 0 Ties' % (wins))
            print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
            playerMove = input().upper()
            if playerMove == 'Q':
                return # Leave the runGame() function.

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


# If the player runs this program (instead of importing it), run the game:
if __name__ == '__main__':
    runGame()
