# Leetspeak, by Al Sweigart al@inventwithpython.com

import random

try:
    import pyperclip
except ImportError:
    pass # It's not a big deal if pyperclip is not installed.

def englishToLeetspeak(message):
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'],
    'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leet = []
    for char in message:
        if char.lower() in charMapping and random.randint(1, 100) > 30:
            leet.append(random.choice(charMapping[char.lower()]))
        else:
            leet.append(char)
    return ''.join(leet)

print('Enter your leet message:')
english = input()
print()
leetspeak = englishToLeetspeak(english)
print(leetspeak)

try:
    pyperclip.copy(leetspeak)
    print('(Copied leetspeak to clipboard.)')
except:
    pass # Do nothing if pyperclip wasn't installed.
