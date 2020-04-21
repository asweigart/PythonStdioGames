"""Leetspeak, by Al Sweigart al@inventwithpython.com
Translates English messages into l33t5p34]<.
This and other games are available at https://nostarch.com/XX
Tags: tiny, beginner, word, pyperclip"""
__version__ = 0
import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.


def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        # Trying to use pyperclip will raise a NameError exception if
        # it wasn't imported:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass  # Do nothing if pyperclip wasn't installed.


def englishToLeetspeak(message):
    """Convert the English string in message and return leetspeak."""
    # Make sure all the keys in `charMapping` are lowercase.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:  # Check each character:
        # There is a 70% chance we change the character to leetspeak.
        if char.lower() in charMapping and random.random() <= 0.70:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # Don't translate this character:
            leetspeak = leetspeak + char
    return leetspeak


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
