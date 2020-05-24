"""Rail Fence Cipher, by Al Sweigart al@inventwithpython.com
The "rail fence" cipher for encrypting text.
More info at: https://en.wikipedia.org/wiki/Rail_fence_cipher
This and other games are available at https://nostarch.com/XX
Tags: large, cryptography"""
__version__ = 0
try:
    import pyperclip  # pyperclip copies text to the clipboard.
except:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    print('Rail Fence Cipher, by Al Sweigart al@inventwithpython.com')

    # Ask the user if they want to encrypt or decrypt:
    while True:
        print('Do you want to (E)ncrypt or (D)ecrypt?')
        mode = input('> ').upper()
        if mode == 'E' or mode == 'D':
            break

    # Ask the user for the message to encrypt or decrypt:
    while True:
        print('Enter a message up to 79 characters long:')
        print('|' + ('-' * 77) + '|')
        message = input('> ')
        if len(message) <= 79:
            break

    # Ask the user for the key number.
    while True:
        print('Enter the key number 2 to 12:')
        response = input('> ')
        try:
            key = int(response)
        except:
            print('You must enter a number.')
        if 2 <= key <= 12:
            break

    # Encrypt or decrypt the message:
    if mode == 'E':
        encryptMessage(message, key)
    elif mode == 'D':
        decryptMessage(message, key)


def putMessageOnRails(message, key):
    """Lay out the letters in message on key number of rails."""
    rails = []  # A list of lists, where each list is a rail of letters.
    for i in range(len(message)):
        rails.append([' '] * key)
    return rails


def displayRails(rails):
    """Display the letters in the rails."""
    for y in range(len(rails[0])):
        for x in range(len(rails)):
            print(rails[x][y], end='')
        print()


def getRailCoordinates(message, key):
    """Return a list of x, y coordinates of the zig zag order rail."""
    railCoordinates = []
    y = 0
    direction = 'DOWN'
    for x in range(len(message)):
        railCoordinates.append((x, y))
        if direction == 'DOWN':
            y += 1
            if y == key:  # Reached the bottom rail, now go up.
                direction = 'UP'
                y -= 2
        elif direction == 'UP':
            y -= 1
            if y == -1:  # Reached the top rail, now go down.
                direction = 'DOWN'
                y += 2
    return railCoordinates


def copyIfPossible(text):
    """Copy text to the clipboard if pyperclip is installed."""
    try:
        print('Copied to clipboard.')
        pyperclip.copy(text)  # Copy the text to the clipboard.
    except:
        pass  # If pyperclip wasn't imported, do nothing.


def encryptMessage(message, key):
    rails = putMessageOnRails(message, key)
    railCoordinates = getRailCoordinates(message, key)

    # Lay out the letters in rails:
    messageIndex = 0
    for x, y in railCoordinates:
        rails[x][y] = message[messageIndex]
        messageIndex += 1

    # Read the letters going across the rails:
    encryptedText = ''
    for railNumber in range(key):
        for x, y in railCoordinates:
            if y == railNumber:
                encryptedText += rails[x][y]

    # Show the encrypted message to the user:
    displayRails(rails)
    print('The encrypted message (not including the right-side bar) is:')
    print(encryptedText + '|')
    copyIfPossible(encryptedText)


def decryptMessage(message, key):
    rails = putMessageOnRails(message, key)
    railCoordinates = getRailCoordinates(message, key)

    # Lay out the letters on the rails:
    messageIndex = 0
    for railNumber in range(key):
        for x, y in railCoordinates:
            if y == railNumber:
                rails[x][y] = message[messageIndex]
                messageIndex += 1

    # Read the letters in rail order:
    decryptedText = ''
    for x, y in railCoordinates:
        decryptedText += rails[x][y]

    # Show the decrypted message to the user:
    displayRails(rails)
    print('The decrypted message is:')
    print(decryptedText)
    copyIfPossible(decryptedText)


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
