import random
GUILLOTINE_PICS = [r'''
|
|
|
|
|
|
|
|===|''', r'''
|   |
|   |
|   |
|   |
|   |
|   |
|   |
|===|''', r'''
|===|
|   |
|   |
|   |
|   |
|   |
|   |
|===|''', r'''
|===|
|   |
|   |
|   |
|   |
|   |
|\ /|
|===|''', r'''
|===|
|   |
|   |
|   |
|   |
|/-\|
|\ /|
|===|''', r'''
|===|
|| /|
||/ |
|   |
|   |
|/-\|
|\ /|
|===|''', rf'''
|===|
|| /|
||/ |
|   |
|   |
|/-\|
|\{chr(9786)}/|
|===|''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def displayBoard(GUILLOTINE_PICS, missedLetters, correctLetters, secretWord):
    print(GUILLOTINE_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


print('GULLIOTINE')

while True:
    # Setup variables for a new game:
    missedLetters = ''
    correctLetters = ''
    secretWord = random.choice(words)
    gameIsDone = False

    while True: # Main game loop.
        displayBoard(GUILLOTINE_PICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            if len(missedLetters) == len(GUILLOTINE_PICS) - 1:
                displayBoard(GUILLOTINE_PICS, missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            break

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break