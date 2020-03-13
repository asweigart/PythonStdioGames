"""Fast Draw, by Al Sweigart al@inventwithpython.com

Try to out-draw the computer in this gunfighter game."""

import random, sys, time

print('Fast Draw, by Al Sweigart al@inventwithpython.com')
print('When you see "DRAW", press Enter. You have 0.3 seconds to draw.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
print('Press Enter to begin...')
input()

while True:
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        print('You drew too soon! You lose.')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 2)
        print('You took', timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 2)
        print('You took', timeElapsed, 'seconds to draw.')
        print('You are the fastest gun in the west! You win!')

    print('Enter QUIT to stop, or just press Enter to play again.')
    response = input().upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()