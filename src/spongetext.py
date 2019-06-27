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
    print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
except:
    pass # Do nothing if pyperclip wasn't installed.
