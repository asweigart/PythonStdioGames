# Pig Latin by Al Sweigart, al@inventwithpython.com

print('IGPAY ATINLAY (pig latin)')
print('By Al Sweigart al@inventwithpython.com')
print()

message = input('Enter your message> ')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
    prefixPunctuation = ''
    while not word[0].isalpha():
        prefixPunctuation += word[0]
        word = word[1:]

    suffixPunctuation = ''
    while not word[-1].isalpha():
        suffixPunctuation += word[-1]
        word = word[:-1]

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    prefixConsonants = ''
    while not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixPunctuation + word + suffixPunctuation)

print(' '.join(pigLatin))
