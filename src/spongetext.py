# Spongetext, by Al Sweigart al@inventwithpython.com

import random

try:
    import pyperclip
except ImportError:
    pass # It's not a big deal if pyperclip is not installed.

print('Enter your message:')
message = input()
print()

spongetext = []
useUpper = False

for char in message:
    if not char.isalpha():
        spongetext.append(char)
        continue

    if useUpper:
        spongetext.append(char.upper())
    else:
        spongetext.append(char.lower())

    useUpper = not useUpper

    if random.randint(1, 100) <= 10:
        useUpper = not useUpper

spongetext = ''.join(spongetext)
print(spongetext)
try:
    pyperclip.copy(spongetext)
    print('(Copied spongetext to clipboard.)')
except:
    pass # Do nothing if pyperclip wasn't installed.
