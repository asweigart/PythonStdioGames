# 99 Bottles of Beer on the Wall
# By Al Sweigart al@inventwithpython.com

import time

bottles = 99
PAUSE = 1

while bottles > 1:
    print(bottles, 'of beer on the wall,')
    time.sleep(PAUSE)
    print(bottles, 'bottles of beer,')
    time.sleep(PAUSE)
    print('Take one down, pass it around,')
    time.sleep(PAUSE)
    bottles = bottles - 1
    print(bottles, 'bottles of beer on the wall!')
    time.sleep(PAUSE)
    print()

print('1 bottle of beer on the wall,')
time.sleep(PAUSE)
print('1 bottle of beer,')
time.sleep(PAUSE)
print('Take it down, pass it around,')
time.sleep(PAUSE)
print('No more bottles of beer on the wall!')
