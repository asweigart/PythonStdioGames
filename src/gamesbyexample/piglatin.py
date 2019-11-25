# Pig Latin, by Al Sweigart al@inventwithpython.com
# Translates English messages into Igpay Atinlay.

try:
    import pyperclip # pyperclip copies text to the clipboard.
except ImportError:
    pass # It's not a big deal if pyperclip is not installed.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def englishToPigLatin(message):
    pigLatin = '' # A string of the pig latin translation.
    for word in message.split():
        # Separate the non-letters at the start of this word:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

        # Separate the non-letters at the end of this word:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters += word[-1]
            word = word[:-1]

        # Remember if the word was in uppercase or titlecase.
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower() # Make the word lowercase for translation.

        # Separate the consonants at the start of this word:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        # Add the pig latin ending to the word:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'yay'

        # Set the word back to uppercase or titlecase:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        # Add the non-letters back to the start or end of the word.
        pigLatin = pigLatin + prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


def main():
    print('''IGPAY ATINLAY (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:''')
    pigLatin = englishToPigLatin(input())

    # Join all the words back together into a single string:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass # Do nothing if pyperclip wasn't installed.


if __name__ == '__main__':
    main()