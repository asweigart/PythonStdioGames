# Guess the Number with Position Hints, version 1
# By Al Sweigart, al@inventwithpython.com

import random

indexToPlaceMapping = {0: '1st',
                       1: '2nd',
                       2: '3rd',
                       3: '4th',
                       4: '5th'}

guessesTaken = 0
secretNumber = ''
for i in range(5):
    secretNumber += str(random.randint(0, 9))

print('I am thinking of a 5-digit number.')
while True:
    selectedDigits = random.sample(range(5), 3)
    selectedDigits.sort()
    selectedDigitsTotal = int(secretNumber[selectedDigits[0]]) + int(secretNumber[selectedDigits[1]]) + int(secretNumber[selectedDigits[2]])

    print('The sum of the ' + indexToPlaceMapping[selectedDigits[0]] + ', ' + indexToPlaceMapping[selectedDigits[1]] + ', and ' + indexToPlaceMapping[selectedDigits[2]] + ' digits is ' + str(selectedDigitsTotal))

    print('Take a guess.')
    guess = input()

    if len(guess) != 5:
        print('That guess is not 5 digits.')
        continue
    if not guess.isdigit():
        print('That guess is not 5 digits.')
        continue

    guessesTaken += 1

    if guess == secretNumber:
        print('Hooray! You guessed the number in ' + str(guessesTaken) + ' guesses.')
        break

    if guess[0] == secretNumber[0]:
        print('Yes, the 1st digit ' + str(secretNumber[0]) + '.')
    if guess[1] == secretNumber[1]:
        print('Yes, the 2nd digit ' + str(secretNumber[1]) + '.')
    if guess[2] == secretNumber[2]:
        print('Yes, the 3rd digit ' + str(secretNumber[2]) + '.')
    if guess[3] == secretNumber[3]:
        print('Yes, the 4th digit ' + str(secretNumber[3]) + '.')
    if guess[4] == secretNumber[4]:
        print('Yes, the 5th digit ' + str(secretNumber[4]) + '.')
