# sPoNgEtExT, by Al Sweigart al@inventwithpython.com
# Translates English messages into sPOnGEtExT.
__version__ = 1

import random

try:
    import pyperclip
except ImportError:
    pass # It's not a big deal if pyperclip is not installed.

def englishToSpongetext(message):
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
    return spongetext


def main():
    print('''sPoNgEtExT
bY aL sWeIGaRt Al@iNvEnTwItHpYtHoN.cOm

eNtEr YoUr MeSsAgE:''')
    spongetext = englishToSpongetext(input())
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass # Do nothing if pyperclip wasn't installed.

if __name__ == '__main__':
    main()