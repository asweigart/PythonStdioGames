"""Bagels (barebones version), by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues."""
import random

def main():
    print('Bagels (barebones version), a deductive logic game.')
    print('By Al Sweigart al@inventwithpython.com')
    print()
    print('When I say:    That means:')
    print('  Pico         One digit is correct but in the wrong place.')
    print('  Fermi        One digit is correct and in the right place.')
    print('  Bagels       No digit is correct.')
    print()
    print('For example, if the number is 248 and you guess 843')
    print('the clues would be Fermi Pico.')

    # Make the secret number the player needs to guess:
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first 3 digits in the list for the secret number:
    secretNum = str(numbers[0]) + str(numbers[1]) + str(numbers[2])

    print('I have thought up a 3-digit number.')
    print('You have 10 guesses to get it.')

    numGuesses = 1
    while numGuesses <= 10:
        print('Guess #', numGuesses)
        guess = input('> ')

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break  # They're correct, so break out of this loop.
        if numGuesses > 10:
            print('You ran out of guesses.')
            print('The answer was', secretNum)

    print('Thanks for playing!')


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = ''
    for i in range(3):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues += 'Fermi '
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues += 'Pico '

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Make a single string from the list of string clues.
        return clues


# Call the main() function to play the game:
main()
