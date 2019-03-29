# Hamsburger, a program for making silly pluralization
# by Al Sweigart al@inventwithpython.com

# nounlist.txt can be downloaded from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

import random, os, sys

def pluralize(word):
    if word.endswith('o'):
        return word + 'es'
    elif word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] == 's' or word[-1] == 'x' or word[-2:] == 'sh' or word[-2:] == 'ch':
        return word + 'es'
    else:
        return word + 's'


# Loading nouns from nounlist.txt
if not os.path.exists('nounlist.txt'):
    sys.exit('nounlist.txt not found. Download it from http://www.desiquintans.com/downloads/nounlist/nounlist.txt')

fo = open('nounlist.txt')
nouns = fo.readlines()
fo.close()

for i, noun in enumerate(nouns):
    nouns[i] = noun.strip() # Remove the trailing \n from each string.

print('Generating silly pluralizations...')

sillyPluralizations = []
for stem in nouns:
    for fullWord in nouns:
        if fullWord.startswith(stem) and fullWord != stem:
            sillyPluralizations.append((fullWord, pluralize(stem) + fullWord[len(stem):]))

print(len(sillyPluralizations), 'silly pluralizations generated.')
print('Press Ctrl-C to quit, or press Enter for more words.')
try:
    while True:
        originalWord, sillyWord = random.choice(sillyPluralizations)
        print('The plural of %s is %s.' % (originalWord, sillyWord))
        response = input()
except KeyboardInterrupt:
    sys.exit()