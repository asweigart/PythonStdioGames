# Rock, Paper, Scissors, by Al Sweigart al@inventwithpython.com

import random, time

def runGame():
    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0

    while True: # The main game loop.
        while True: # Keep asking until player enters R/P/S/Q.
            print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
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
            playerMove = 'ROCK'
        elif playerMove == 'P':
            print('PAPER versus...')
            playerMove = 'PAPER'
        elif playerMove == 'S':
            print('SCISSORS versus...')
            playerMove = 'SCISSORS'

        # Count to three with dramatic pauses:
        time.sleep(0.5)
        print('1...')
        time.sleep(0.25)
        print('2...')
        time.sleep(0.25)
        print('3...')
        time.sleep(0.25)

        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'ROCK'
        elif randomNumber == 2:
            computerMove = 'PAPER'
        elif randomNumber == 3:
            computerMove = 'SCISSORS'
        print(computerMove)
        time.sleep(0.5)

        # Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('It\'s a tie!')
            ties = ties + 1
        elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'PAPER' and computerMove == 'ROCK':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'ROCK' and computerMove == 'PAPER':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
            print('You lose!')
            losses = losses + 1


# If the player runs this program (instead of importing it), run the game:
if __name__ == '__main__':
    runGame()
