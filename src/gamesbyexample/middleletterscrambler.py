"""Middle Letter Scrambler, by Al Sweigart al@inventwithpython.com
Scrambles the middle letters of words, but not the first and last
letters.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, word"""
__version__ = 0
import random, sys

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    print('''Middle Letter Scrambler
By Al Sweigart al@inventwithpython.com

Your brain can probably read scrambled words as long as the first and
last letters are in the right place.
Your biran can pbablroy raed sambcerld wrdos as lnog as the fsirt and
last lteters are in the rihgt pcale.''')

    while True:
        print()
        print('Enter your message (or nothing to quit):')
        message = input('> ')
        if message == '':
            print('Thanks for playing!')
            sys.exit()
        scrambled = englishToMiddleLetterScramble(message)
        print()
        print(scrambled)

        try:
            pyperclip.copy(scrambled)
            print('(Copied scrambled text to clipboard.)')
        except:
            pass  # Do nothing if pyperclip wasn't installed.


def englishToMiddleLetterScramble(message):
    """Convert the string message into middle-letter scrambled text."""
    if message == '':
        # If the message is blank, the scrambled text is blank too.
        return ''

    scrambled = ''

    words = message.split()
    for word in words:
        if len(word) <= 3:
            scrambled += word + ' '  # Add the short word unscrambled.
            continue

        # Convert the middle letters to a list:
        middleLetters = list(word[1:-1])
        # Shuffle the middle letters:
        random.shuffle(middleLetters)
        # Convert the list back into a string:
        middleLetters = ''.join(middleLetters)

        scrambled += word[0] + middleLetters + word[-1] + ' '

    return scrambled[:-1]  # [:-1] to cut off the final added ' ' space.


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
