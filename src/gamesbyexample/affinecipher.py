"""Affine Cipher, by Al Sweigart al@inventwithpython.com
The affine cipher is a simple substitution cipher that uses addition and
multiplication to encrypt and decrypt symbols.
This and other games are available at https://nostarch.com/XX
Tags: large, cryptography, math, pyperclip"""
__version__ = 0
try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

import random

# Note the space at the front of the SYMBOLS string:
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF""" + \
          """GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main():
    print('''Affine Cipher, by Al Sweigart al@inventwithpython.com
The affine cipher is a simple substitution cipher that uses addition and
multiplication to encrypt and decrypt symbols.''')

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
        print('Please specify the key to use,')
        print('or RANDOM to have one generated for you:')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if not response.isdecimal():
                print('This key is not a number.')
                continue
            if checkKey(int(response), myMode):
                myKey = int(response)
                break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('%sed text:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # Do nothing if pyperclip wasn't installed.


def getKeyPartsFromKey(key):
    """Get the two key A and key B parts from the key."""
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKey(key, mode):
    """Return True if key is a valid encryption key for this mode.
    Otherwise return False."""
    keyA, keyB = getKeyPartsFromKey(key)
    if mode == 'encrypt' and keyA == 1 and keyB == 0:
        print('This key effectively does not do any encryption on the')
        print('message. Choose a different key.')
        return False
    elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        print('Key A must be greater than 0 and Key B must be between')
        print('0 and {}.'.format(len(SYMBOLS) - 1))
        return False
    elif gcd(keyA, len(SYMBOLS)) != 1:
        print('Key A ({}) and the symbol set'.format(keyA))
        print('size ({}) are not relatively prime.'.format(len(SYMBOLS)))
        print('Choose a different key.')
        return False
    return True

def encryptMessage(key, message):
    """Encrypt the message using the key."""
    checkKey(key, 'encrypt')
    keyA, keyB = getKeyPartsFromKey(key)
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            newIndex = (symIndex * keyA + keyB) % len(SYMBOLS)
            ciphertext += SYMBOLS[newIndex]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext


def decryptMessage(key, message):
    """Decrypt the message using the key."""
    checkKey(key, 'decrypt')
    keyA, keyB = getKeyPartsFromKey(key)
    plaintext = ''
    modInvOfKeyA = findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            newIndex = (symIndex - keyB) * modInvOfKeyA % len(SYMBOLS)
            plaintext += SYMBOLS[newIndex]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext


def generateRandomKey():
    """Generate and return a random encryption key."""
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


def gcd(a, b):
    """Return the Greatest Common Divisor of a and b using
    Euclid's Algorithm."""
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    """Return the modular inverse of a % m, which is the number x such
    that a*x % m = 1"""

    if gcd(a, m) != 1:
        # No mod inverse exists if a & m aren't relatively prime:
        return None

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # Note that // is the integer division operator
        v1, v2, v3, u1, u2, u3 = ((u1 - q * v1),
                                  (u2 - q * v2),
                                  (u3 - q * v3),
                                  v1, v2, v3)
    return u1 % m


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
