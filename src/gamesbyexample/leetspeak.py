# Leetspeak, by Al Sweigart al@inventwithpython.com
# Translates English messages into l33t5p34]<.
__version__ = 1

import random

try:
    import pyperclip # pyperclip copies text to the clipboard.
except ImportError:
    pass # If pyperclip cannot be found, do nothing. It's not a big deal.

def englishToLeetspeak(message):
    # Make sure all the keys in `charMapping` are lowercase.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'],
    'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leet = []
    for char in message: # Check each character:
        if char.lower() in charMapping and random.randint(1, 100) <= 70:
            leet.append(random.choice(charMapping[char.lower()]))
        else:
            leet.append(char) # Don't translate this character.
    return ''.join(leet)

def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input()
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass # Do nothing if pyperclip wasn't installed.

if __name__ == '__main__':
    main()
