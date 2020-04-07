"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, cryptography, math"""
__version__ = 0
print('''Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This programs hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.''')

# Let the user specify the message to hack:
print('Enter the message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):  # Loop through every possible key.
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in LETTERS:
            # Get the encrypted (or decrypted) number for this symbol.
            num = LETTERS.find(symbol) # Get the number of the symbol.
            num = num - key  # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(LETTERS)

            # Add decrypted number's symbol to translated:
            translated = translated + LETTERS[num]
        else:
            # Just add the symbol without encrypting/decrypting:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print('Key #%s: %s' % (key, translated))
