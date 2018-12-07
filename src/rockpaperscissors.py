import random
import time

def runGame():
    wins = 0
    losses = 0
    ties = 0

    while True:
        while True:
            print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            print('Enter your move: (R)ock (P)aper (S)cissors')
            playerMove = input().upper()
            if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
                break

        if playerMove == 'R':
            print('ROCK versus...')
            playerMove = 'ROCK'
        elif playerMove == 'P':
            print('PAPER versus...')
            playerMove = 'PAPER'
        elif playerMove == 'S':
            print('SCISSORS versus...')
            playerMove = 'SCISSORS'

        time.sleep(0.5)
        print('1...')
        time.sleep(0.25)
        print('2...')
        time.sleep(0.25)
        print('3...')
        time.sleep(0.25)

        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'ROCK'
        elif randomNumber == 2:
            computerMove = 'PAPER'
        elif randomNumber == 3:
            computerMove = 'SCISSORS'
        print(computerMove)
        time.sleep(0.5)

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

        print('Press Enter to play again, or enter "quit" to stop.')
        response = input()
        if response == 'quit':
            return

if __name__ == '__main__':
    runGame()


