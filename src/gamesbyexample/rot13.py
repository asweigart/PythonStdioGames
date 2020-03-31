"""ROT13 Cipher, by Al Sweigart al@inventwithpython.com

The simplest cipher for encrypting and decrypting text.
More info at https://en.wikipedia.org/wiki/ROT13
Tags: tiny, cryptography, pyperclip"""
__version__ = 0
try:
    import pyperclip
except ImportError:
    pass  # Don't do anything if pyperclip fails to import.

# Set up the constants:
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('ROT 13 CIPHER')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:  # Main program loop.
    print('Enter a message to encrypt or decrypt (or QUIT to quit):')
    message = input('> ')

    if message.upper() == 'QUIT':
        break  # Break out of the main program loop.

    # Rotate the letters in message by 13 characters.
    translated = ''
    for character in message:
        if character.isupper():
            # Concatenate uppercase translated character.
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]
        elif character.islower():
            # Concatenate lowercase translated character.
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]
        else:
            # Concatenate the character untranslated.
            translated += character

    # Display the translation:
    print('The translated message is:')
    print(translated)
    print()

    try:
        # Copy the translation to the clipboard:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except:
        pass
    # At this point, go back to the start of the main program loop.
