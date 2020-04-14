"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
Tags: short, beginner, cryptography, math, pyperclip"""
__version__ = 0
try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')

# Let the user specify if they are encrypting or decrypting:
while True:  # Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user specify the key to use:
while True:  # Keep asking until the user enters a valid key.
    print('Please specify the key (1 to 26) to use.'.format(mode))
    response = input('> ').upper()
    if not response.isdecimal():
        print('This key is not a number.')
        continue
    if 1 <= int(response) <= 26:
        key = int(response)
        break

# Let the user specify the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Stores the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in LETTERS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = LETTERS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0:
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + LETTERS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.
