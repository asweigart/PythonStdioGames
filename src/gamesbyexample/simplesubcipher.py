"""Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
This and other games are available at https://nostarch.com/XX
Tags: short, cryptography, math"""
__version__ = 0
import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Simple Substitution Cipher, by Al Sweigart
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.''')

    # Let the user specify if they are encrypting or decrypting:
    while True:  # Keep asking until the user enters e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        print('Please specify the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Perform the encryption/decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    # Display the results:
    print('The %sed message is:' % (myMode))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def checkKey(key):
    """Return True if key is valid. Otherwise return False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encryptMessage(key, message):
    """Encrypt the message using the key."""
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    """Decrypt the message using the key."""
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    """Encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # The symbol is not in LETTERS, just add it unchanged.
            translated += symbol

    return translated


def generateRandomKey():
    """Generate and return a random encryption key."""
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
