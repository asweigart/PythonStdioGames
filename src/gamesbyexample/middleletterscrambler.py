"""Middle Letter Scrambler, by Al Sweigart al@inventwithpython.com

Scrambles the middle letters of words, but not the first and last
letters.
Tags: tiny, word"""
__version__ = 1

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # It's not a big deal if pyperclip is not installed.


def main():
    """Run the Middle Letter Scrambler program."""
    print('''Middle Letter Scrambler
By Al Sweigart al@inventwithpython.com

Your biran can pbablroy raed sambcerld wrdos as lnog as the fsirt and
last lteters are in the rihgt pcale.

Enter your message:''')
    scrambled = englishToMiddleLetterScramble(input())
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
