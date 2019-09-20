# Luhn Checksum Algorithm, by Al Sweigart al@inventwithpython.com
# More info at: https://en.wikipedia.org/wiki/Luhn_algorithm
# More info at: https://youtu.be/Erp8IAUouus

import time, sys

print('''LUHN Algorithm
By Al Sweigart al@inventwithpython.com

Would you like to see a description of the Luhn algorithm? Y/N''')

# Display information about the Luhn algorithm if the user wants it:
if input().upper().startswith('Y'):
    print('''The Luhn algorithm is a checksum algorithm to make sure a serial number is
correct. It used by credit cards and other ID cards' numbers.

More info at: https://en.wikipedia.org/wiki/Luhn_algorithm

You can't just use any number for a valid credit card number. A checksum
algorithm helps detect that there are no mistakes in the number.

The Luhn algorithm is as follows:
    - The checksum digit is the rightmost digit.
    - From right to left, not including the checksum digit, double every other
      digit. If this is greater than 9, subtract 9 from it.
    - Add up all the doubled and not-doubled numbers.
    - Multiply this by 9.
    - The units place is the checksum digit.

Example: 7992739871x (x is the checksum digit)
Double every other digit:     7|18|9|4|7|6|9|16|7|2|x
Subtract 9 if greater than 9: 7| 9|9|4|7|6|9| 7|7|2|x
Add them all up:              7+9+9+4+7+6+9+7+7+2 = 67
Multiply by 9:                67 * 9 = 603
The units place is the checksum digit: 60[3] = 3
Final number: 79927398713

Press Enter to continue...
''')
    input() # Pause to let the user press Enter.


while True: # Main application loop.
    print('Enter a number to check its checksum (or QUIT):')
    originalNumber = input()

    if originalNumber.upper().startswith('Q'):
        sys.exit()

    if not originalNumber.isdecimal():
        print('Please enter a number.')
        continue
    if len(originalNumber) < 2:
        print('The number must have at least two digits.')
        continue

    # Display each step of the Luhn algorithm:
    print('1) Get the non-checksum digits of the number:')
    nonChecksumDigits = list(originalNumber)[:-1]
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(1)

    print('2) Double every other digit, from right to left:')
    for i in range(len(nonChecksumDigits) - 1, -1, -2):
        nonChecksumDigits[i] = str(int(nonChecksumDigits[i]) * 2)
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(1)

    print('3) If greater than 9, subtract 9:')
    for i, number in enumerate(nonChecksumDigits):
        if int(number) > 9:
            nonChecksumDigits[i] = str(int(number) - 9)
    print('   ', ' '.join(nonChecksumDigits))
    time.sleep(1)

    print('4) Add up all the numbers:')
    print('    ', end='')
    for i, number in enumerate(nonChecksumDigits):
        print(number, end=' ')
        nonChecksumDigits[i] = int(number) # Convert str to int.
    digitSum = sum(nonChecksumDigits)
    print('=', digitSum)
    time.sleep(1)

    print('5) Multiply by 9:')
    digitSumTimesNine = digitSum * 9
    print(f'    {digitSum} * 9 = {digitSumTimesNine}')
    time.sleep(1)

    print('6) The checksum digit is the units digit:')
    checksumDigit = str(digitSumTimesNine)[-1]
    print(f'    {str(digitSumTimesNine)[:-1]}[{checksumDigit}]')
    time.sleep(1)

    print('7) Append the checksum digit for the complete, valid number:')
    numberWithValidChecksum = originalNumber[:-1] + str(checksumDigit)
    print(f'    {numberWithValidChecksum}')
    time.sleep(1)

    if numberWithValidChecksum == originalNumber:
        print('You entered a VALID NUMBER.')
    else:
        print('You entered a number with an INVALID CHECKSUM.')
        print(f'The checksum should be {checksumDigit} not {originalNumber[-1]}')

    input('Press Enter to continue...')
    print() # Print some newlines for space.
    print()
    print()
