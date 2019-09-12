# Hamsburger, a program for making silly pluralization
# by Al Sweigart al@inventwithpython.com

# nounlist.txt can be downloaded from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

import random, os, sys

def pluralize(word):
    # Returns the pluralized form of `word`:
    if word.endswith('o'):
        return word + 'es'
    elif word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] == 's' or word[-1] == 'x' or word[-2:] == 'sh' or word[-2:] == 'ch':
        return word + 'es'
    else:
        return word + 's'


print('HAMSBURGER')
print('By Al Sweigart al@inventwithpython.com')
print()

# Loading nouns from nounlist.txt
if not os.path.exists('nounlist.txt'):
    print('nounlist.txt not found. Download it from http://www.desiquintans.com/downloads/nounlist/nounlist.txt')
    sys.exit()

fo = open('nounlist.txt')
nouns = fo.readlines()
fo.close()

for i, noun in enumerate(nouns):
    nouns[i] = noun.strip() # Remove the trailing \n from each string.

if not os.path.exists('hamsburger.txt'):
    print('Generating silly pluralizations for hamsburger.txt...')

    sillyPluralizations = []
    for stem in nouns:
        for fullWord in nouns:
            if fullWord.startswith(stem) and fullWord != stem:
                sillyPluralizations.append(f'The plural of {fullWord} is {pluralize(stem) + fullWord[len(stem):]}.')

    # Write the silly pluralizations out to hamsburger.txt.
    fo = open('hamsburger.txt', 'w')
    fo.write('\n'.join(sillyPluralizations))
    fo.close()

    print(len(sillyPluralizations), 'silly pluralizations generated.')
else:
    # Reading in hamsburger.txt:
    fo = open('hamsburger.txt')
    sillyPluralizations = fo.readlines()
    fo.close()

    for i, line in enumerate(sillyPluralizations):
        sillyPluralizations[i] = line.strip() # Remove the \n.


print('Press Ctrl-C to quit, or press Enter for more words.')
try:
    while True:
        print(random.choice(sillyPluralizations))
        response = input()
except KeyboardInterrupt:
    sys.exit()
