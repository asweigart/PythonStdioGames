"""Numeral System Counters, by Al Sweigart al@inventwithpython.com

Shows the equivalent numbers in decimal, hexadecimal, and binary."""

__version__ = 1

print('''Numeral System Counters
By Al Sweigart al@inventwithpython.com

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)

''')

while True:
    response = input('Enter the starting number> ')
    if response == '':
        response = '0' # Start at 0 by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
start = int(response)

while True:
    response = input('Enter how many numbers to display> ')
    if response == '':
        response = '1000' # Display 1000 numbers by default.
        break
    if response.isdecimal():
        break
    print('Please enter a number.')
amount = int(response)

for number in range(start, start + amount): # Main program loop.
    hexNumber = hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)
