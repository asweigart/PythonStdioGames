"""Text To Speech Talker, by Al Sweigart al@inventwithpython.com
An example program using the text-to-speech features of the pyttsx3
module.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner"""
__version__ = 0
import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

tts = pyttsx3.init()  # Initialize the TTS engine.

print('Text To Speech Talker, by Al Sweigart al@inventwithpython.com')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
print('eSpeak (on Linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say it.
