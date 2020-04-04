"""Powerball Lottery, by Al Sweigart al@inventwithpython.com
A simulation of the lottery so you can experience the thrill of
losing the lottery without wasting your money.
Tags: short, simulation, humor"""

import random

print('''Powerball Lottery
By Al Sweigart al@inventwithpython.com

Each powerball lottery ticket costs $2. The jackpot for this game
is $1.586 billion! It doesn't matter what the jackpot is though,
because the odds are 1 in 292,201,338, so you won't win.

This simulation gives you the thrill of playing without wasting money.
''')

# Let the player enter the first five numbers, 1 to 69:
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number.')
    response = input('> ')

    # Check that the player entered 5 things:
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue

    # Convert the strings into integers:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    # Check that the numbers are between 1 and 69:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    # Check that the numbers are unique:
    # (Create a set from number to remove duplicates.)
    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue

    break

# Let the player select the powerball, 1 to 26:
while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')

    # Convert the strings into integers:
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue

    # Check that the number is between 1 and 26:
    if not (1 <= powerball <= 26):
        print('The powerball number must be between 1 and 26.')
        continue

    break

# Enter the number of times you want to play:
while True:
    print('How many times do you want to play? (Max: 1000000)')
    response = input('> ')

    # Convert the strings into integers:
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    # Check that the number is between 1 and 1000000:
    if not (1 <= numPlays <= 1000000):
        print('You can play between 1 and 1000000 times.')
        continue

    break

# Run the simulation:
price = '$' + str(2 * numPlays)
print('It costs', price, 'to play', numPlays, 'times, but don\'t')
print('worry. I\'m sure you\'ll win it all back.')
input('Press Enter to start...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # Come up with lottery numbers:
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Display winning numbers:
    print('The winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and ' + str(winningPowerball)
    print(allWinningNums.ljust(21), end='')

    # NOTE: Sets are not ordered, so it doesn't matter what order the
    # integers in set(numbers) and set(winningNumbers) are.
    if set(numbers) == set(winningNumbers) and \
    powerball == winningPowerball:
        print()
        print('You have won the Powerball Lottery! Congratulations, you')
        print('would be a billionaire if this was real!')
        break
    else:
        print(' You lost.')

print('You have wasted', price)
print('Thanks for playing!')
