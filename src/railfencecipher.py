# Rail Fence Cipher, by Al Sweigart al@inventwithpython.com
# Implements a simple encryption system. https://en.wikipedia.org/wiki/Rail_fence_cipher

try:
    import pyperclip # Try to import pyperclip to copy the text to the clipboard.
except:
    pass # If pyperclip cannot be found, do nothing. It's not a big deal.


def getNewBoard(message, key):
    # Create a data structure for the rows of blank spaces that we will fill in.
    board = [] # railRows[x][y] represents the letter at the place.
    for i in range(len(message)):
        board.append([' '] * key)
    return board


def displayBoard(board):
    for y in range(len(board[0])):
        for x in range(len(board)):
            print(board[x][y], end='')
        print()


def getRailCoordinates(message, key):
    # Get the x, y coordinates of the rail in order as it zig zags across the rows.
    railCoordinates = []
    y = 0
    direction = 'DOWN'
    for x in range(len(message)):
        railCoordinates.append((x, y))
        if direction == 'DOWN':
            y += 1
            if y == key:
                direction = 'UP'
                y -= 2
        elif direction == 'UP':
            y -= 1
            if y == -1:
                direction = 'DOWN'
                y += 2
    return railCoordinates


def copyIfPossible(text):
    try:
        pyperclip.copy(text) # Copy the text to the clipboard.
    except:
        pass # If pyperclip wasn't imported, do nothing.


def encryptMessage(message, key):
    board = getNewBoard(message, key)
    railCoordinates = getRailCoordinates(message, key)

    # Lay out the letters in the `board`:
    messageIndex = 0
    for x, y in railCoordinates:
        board[x][y] = message[messageIndex]
        messageIndex += 1

    # Read the letters in row order:
    encryptedText = ''
    for rowNum in range(key):
        for x, y in railCoordinates:
            if y == rowNum:
                encryptedText += board[x][y]

    # Show the encrypted message to the user:
    displayBoard(board)
    print('The encrypted message is:')
    print(encryptedText)
    copyIfPossible(encryptedText)


def decryptMessage(message, key):
    board = getNewBoard(message, key)
    railCoordinates = getRailCoordinates(message, key)

    # Lay out the letters on the `board`:
    messageIndex = 0
    for rowNum in range(key):
        for x, y in railCoordinates:
            if y == rowNum:
                board[x][y] = message[messageIndex]
                messageIndex += 1

    # Read the letters in rail order:
    decryptedText = ''
    for x, y in railCoordinates:
        decryptedText += board[x][y]

    # Show the decrypted message to the user:
    displayBoard(board)
    print('The decrypted message is:')
    print(decryptedText)
    copyIfPossible(decryptedText)


def main():
    print('RAIL FENCE CIPHER')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    while True:
        print('Do you want to (E)ncrypt or (D)ecrypt?')
        mode = input().upper()
        if mode == 'E' or mode == 'D':
            break

    # Have the user enter the message to encrypt or decrypt.
    while True:
        print('Enter a message up to 79 characters long:')
        print('|' + ('-' * 77) + '|')
        message = input()
        if len(message) <= 79:
            break

    # Have the user enter the key number.
    while True:
        print('Enter the key number 2 to 12:')
        key = input()
        try:
            key = int(key)
        except:
            print('You must enter a number.')
        if 2 <= key <= 12:
            break


    if mode == 'E':
        encryptMessage(message, key)
    elif mode == 'D':
        decryptMessage(message, key)




if __name__ == '__main__':
    main()