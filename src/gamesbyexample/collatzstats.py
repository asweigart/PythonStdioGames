"""Collatz Sequence Stats, by Al Sweigart al@inventwithpython.com
Finds out how long various Collatz Sequences are.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
Tags: short, math"""
__version__ = 0
print('''Collatz Sequence Stats, by Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a
starting number, following two rules:

1) If the current number N is even, the next number is N / 2.
2) If the current Number N is odd, the next number is N * 3 + 1.

The sequence terminates when N becomes 1. It is generally thought,
but so far not mathematically proven, that every starting number
eventually terminates.

(Run the collatz.py program to see the actual numbers in the sequence.)
''')


while True: # Ask for a starting number range.
    print('Enter a starting number range (like 1-1000):')
    response = input('> ')

    rangeOfNums = response.split('-')
    if len(rangeOfNums) == 2:
        if rangeOfNums[0].isdecimal() and rangeOfNums[1].isdecimal():
            beginRange = int(rangeOfNums[0])
            endRange = int(rangeOfNums[1])
            if beginRange > 0 and endRange > 0 and beginRange < endRange:
                break
    print('Enter a number range, with two numbers separated by a dash.')
    # At this point, go back to the start of the loop.

# Keep track of stats:
shortestLength = None
shortestLengthStartingNumber = None
longestLength = None
longestLengthStartingNumber = None

for startingNum in range(beginRange, endRange + 1):
    n = startingNum
    length = 1

    # Run through the sequence:
    while n != 1:
        if n % 2 == 0:  # If n is even...
            n = n // 2
        else: # Otherwise, n is odd...
            n = 3 * n + 1
        length += 1

    if shortestLength == None or length < shortestLength:
        shortestLength = length
        shortestLengthStartingNumber = startingNum
    if longestLength == None or length > longestLength:
        longestLength = length
        longestLengthStartingNumber = startingNum

    print('Starting number:', startingNum, 'Sequence length:', length)

print('Shortest sequence started from', shortestLengthStartingNumber)
print('and produced a sequence with', shortestLength, 'numbers.')

print('Longest sequence started from', longestLengthStartingNumber)
print('and produced a sequence with', longestLength, 'numbers.')
