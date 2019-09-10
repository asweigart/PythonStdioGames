# sPoNgEtExT, bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

import random

try:
    import pyperclip
except ImportError:
    pass # It's not a big deal if pyperclip is not installed.

print('sPoNgEtExT')
print('bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm')
print()
print('eNtEr YoUr MeSsAgE:')
message = input()
print()

spongetext = ''
useUpper = False

for character in message:
    if not character.isalpha():
        spongetext += character
        continue

    if useUpper:
        spongetext += character.upper()
    else:
        spongetext += character.lower()

    useUpper = not useUpper # Flip the case.

    # Randomly flip the case again in 1 in 10 characters.
    if random.randint(1, 10) == 1:
        useUpper = not useUpper

print(spongetext)
try:
    pyperclip.copy(spongetext)
    print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
except:
    pass # Do nothing if pyperclip wasn't installed.
