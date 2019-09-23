# Morse Code, by Al Sweigart al@inventwithpython.com
# Translates between English and Morse Code.

# More info at: https://en.wikipedia.org/wiki/Morse_code

try:
    import pyperclip
except:
    pass # If pyperclip cannot be found, do nothing. It's not a big deal.

ENGLISH_TO_MORSE = {'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
                    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
                    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
                    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
                    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
                    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
                    'Y': '-.--',  'Z': '--..',  '1': '.----', '2': '..---',
                    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                    ' ': '/'}

# Instead of typing it out, use code to generate MORSE_TO_ENGLISH.
MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key


def englishToMorse(message):
    morse = [] # Make a list of each letter's morse code.
    for character in message:
        if character in ENGLISH_TO_MORSE:
            morse.append(ENGLISH_TO_MORSE[character])
    return ' '.join(morse)


def morseToEnglish(message):
    message = message.split(' ')
    english = [] # Make a list of English letters from the morse code.
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return ''.join(english)


print('MORSE CODE')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:
    print('Are you going to enter (E)nglish or (M)orse code?')
    response = input().upper()
    # Note that you DON'T want `response == 'E' or 'M'` here:
    if response == 'E' or response == 'M':
        break

if response == 'E':
    print('Enter English text:')
    english = input().upper()
    print('Morse code:')
    morse = englishToMorse(english)
    print(morse)
    try:
        pyperclip.copy(morse)
        print('(Morse copied to clipboard.)')
    except:
        pass
elif response == 'M':
    print('Enter Morse code (with spaces in between each letter\'s code):')
    morse = input()
    print('English:')
    english = morseToEnglish(morse)
    print(english)

    try:
        pyperclip.copy(english)
        print('(English text copied to clipboard.)')
    except:
        pass # If pyperclip cannot be found, it's not a big deal.
