import random

GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/\\'

# Load the words.
with open('sevenletterwords.txt') as dictionaryFile:
    WORDS = dictionaryFile.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()


def getBoard(words):
    assert len(words) == 12
    linesWithWords = random.sample(range(16 * 2), 12)
    memoryAddress = 16 * random.randint(0, 4000)

    board = []
    nextWord = 0
    for i in range(16):
        leftLine = ''
        rightLine = ''
        for j in range(16):
            leftLine += random.choice(GARBAGE_CHARS)
            rightLine += random.choice(GARBAGE_CHARS)

        if i in linesWithWords:
            insertionIndex = random.randint(0, 9)
            leftLine = leftLine[:insertionIndex] + words[nextWord] + leftLine[insertionIndex + 7:]
            nextWord += 1
        if i + 16 in linesWithWords:
            insertionIndex = random.randint(0, 9)
            rightLine = rightLine[:insertionIndex] + words[nextWord] + rightLine[insertionIndex + 7:]
            nextWord += 1

        board.append('0x' + hex(memoryAddress)[2:].zfill(4)           + '  ' + leftLine + '    ' +
                     '0x' + hex(memoryAddress + (16*16))[2:].zfill(4) + '  ' + rightLine)

        memoryAddress += 16

    return '\n'.join(board)


def getPlayerMove(words, tries):
    print('Enter password: (%s tries remaining)' % (tries))
    while True:
        move = input().upper()
        if move in words:
            return move


def getNumberOfMatchingLetters(word1, word2):
    matches = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            matches += 1
    return matches


def runGame():
    gameWords = random.sample(WORDS, 12)
    gameBoard = getBoard(gameWords)
    secretPassword = random.choice(gameWords)

    print('Find the password in the computer\'s memory:')
    print(gameBoard)
    for triesRemaining in range(4, 0, -1):
        playerMove = getPlayerMove(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            print('Access Denied (%s/7 correct)' % getNumberOfMatchingLetters(secretPassword, playerMove))
    print('Out of tries. Secret password was %s.' % (secretPassword))


if __name__ == '__main__':
    runGame()