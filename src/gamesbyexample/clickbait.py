"""Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com

A clickbait headline generator for your soulless content farm."""
__version__ = 1

import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Cat', 'Dog', 'Athlete', 'Clown', 'Shovel', 'Paleo Diet',
         'Chicken', 'Mom', 'Dad', 'Doctor', 'Video Game', 'Robot',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
DISEASES = ['The Flu', 'Autism', 'Cancer', 'Heart Disease', 'Alcoholism',
            'Lyme Disease', 'Cryptocurrency', 'Everything']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print('CLICKBAIT TITLE GENERATOR')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    while True:
        print('Our website needs to trick people into looking at ads!')
        print('Enter the number of headlines to generate:')
        response = input()
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break
        # At this point, go back to the start of the loop.

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillenialsAreKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateDoctorsHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomated()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuck', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


# Each of these functions returns a different type of clickbait headline:
def generateAreMillenialsAreKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)


def generateWhatYouDontKnowHeadline():
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun1, noun2, when)


def generateDoctorsHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    disease = random.choice(DISEASES)
    return 'Doctors Hate {}! See How This {} {} Cured {}'.format(pronoun, state, noun, disease)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun1, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    pluralNoun = random.choice(NOUNS) + 's'
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1, pluralNoun, number2)


def generateJobAutomated():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 1)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
