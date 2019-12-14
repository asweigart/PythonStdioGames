# Trick Questions, by Al Sweigart al@inventwithpython.com
# A quiz of several trick questions.

import random, sys

QUESTIONS = [
 {'question': "How many times can you take 2 apples from a pile of 10 apples?",
  'answer': "Once. Then you have a pile of 8 apples.",
  'accept': ['once', 'one', '1']},
 {'question': 'What begins with "e" and ends with "e" but only has one letter in it?',
  'answer': "An envelope.",
  'accept': ['envelope']},
 {'question': "Is it possible to draw a square with three sides?",
  'answer': "Yes. All squares have three sides. They also have a fourth side.",
  'accept': ['yes']},
 {'question': "How many times can a piece of paper be folded in half by hand without unfolding?",
  'answer': "Once. Then you are folding it in quarters.",
  'accept': ['one', '1', 'once']},
 {'question': "What does a towel get as it dries?",
  'answer': "Wet.",
  'accept': ['wet']},
 {'question': "What does a towel get as it dries?",
  'answer': "Drier.",
  'accept': ['drier', 'dry']},
 {'question': "Imagine you are in a haunted house full of evil ghosts. What do you have to do to stay safe?",
  'answer': "Nothing. You're only imagining it.",
  'accept': ['nothing', 'stop']},
{'question': "A taxi driver is going the wrong way down a one way street. She passes ten cops but doesn't get a ticket. Why not?",
  'answer': "She was walking.",
  'accept': ['walk']},
 {'question': "What does a yellow stone thrown into a blue pond become?",
  'answer': "Wet.",
  'accept': ['wet']},
 {'question': "How many miles does must a cyclist bike to get to training?",
  'answer': "None. They're training as soon as they get on the bike.",
  'accept': ['none', 'zero', '0']},
 {'question': "What building do people want to leave as soon as they enter?",
  'answer': "An airport.",
  'accept': ['airport', 'bus', 'port', 'train', 'station', 'stop']},
 {'question': "If you're in the middle of a square house facing the west side with the south side to your left and the north side to your right, which side of the house are you next to?",
  'answer': "None. You're in the middle.",
  'accept': ['none', 'middle', 'not', 'any']},
 {'question': "How much dirt is in a hole 3 meters wide, 3 meters long, and 3 meters deep?",
  'answer': "There is no dirt in a hole.",
  'accept': ['no', 'none', 'zero']},
 {'question': "A girl mails a letter from America to Japan. How many miles did the stamp move?",
  'answer': "Zero. The stamp was in the same place on the envelope the whole time.",
  'accept': ['zero', '0', 'none', 'no']},
 {'question': "What was the highest mountain on Earth the day before Mount Everest was discovered?",
  'answer': "Mount Everest was still the highest mountain of Earth the day before it was discovered.",
  'accept': ['everest']},
 {'question': "How many fingers do most people have on their two hands?",
  'answer': "Eight. They also have two thumbs.",
  'accept': ['eight', '8']},
 {'question': "The 4th of July is a holiday in America. Do they have a 4th of July in England?",
  'answer': "Yes. All countries have a 4th of July on their calendar.",
  'accept': ['yes']},
 {'question': "Which letter of the alphabet makes honey?",
  'answer': "None. A bee is an insect, not a letter.",
  'accept': ['no', 'none', 'not']},
 {'question': "How can a doctor go 30 days without sleep?",
  'answer': "By sleeping at night.",
  'accept': ['night', 'evening']},
 {'question': "How many months have 28 days?",
  'answer': "12. All months have 28 days. Some have more days as well.",
  'accept': ['12', 'twelve', 'all']},
 {'question': "How many two cent stamps are in a dozen?",
  'answer': "A dozen.",
  'accept': ['12', 'twelve', 'dozen']},
 {'question': "Why is it illegal for a person living in North Dakota to be buried in South Dakota?",
  'answer': "Because it is illegal to bury someone alive.",
  'accept': ['alive', 'living', 'live']},
 {'question': "How many heads does a two-headed coin have?",
  'answer': "Zero. Coins are just circular pieces of metal. They don't have heads.",
  'accept': ['zero', 'none', 'no', '0']},
 {'question': "What kind of vehicle has four wheels and flies?",
  'answer': "A garbage truck.",
  'accept': ['garbage', 'dump', 'trash']},
 {'question': "What five-letter word becomes shorter by adding two letters?",
  'answer': "Short.",
  'accept': ['short']},
 {'question': "Gwen's mother has five daughters. Four are named Haha, Hehe, Hihi, and Hoho. What's the fifth daughter's name?",
  'answer': "Gwen.",
  'accept': ['gwen']},
 {'question': "How long is a fence if there are three fence posts each one meter apart?",
  'answer': "Two meters long.",
  'accept': ['2', 'two']},
 {'question': "How many legs does a dog have if you count its tail as a leg?",
  'answer': "Four. Calling a tail a leg doesn't make it one.",
  'accept': ['four', '4']},
 {'question': "How much more are 1976 pennies worth compared to 1975 pennies?",
  'answer': "One cent.",
  'accept': ['1', 'one']},
 {'question': "What two things can you never eat for breakfast?",
  'answer': "Lunch and dinner.",
  'accept': ['lunch', 'dinner', 'supper']},
 {'question': "How many birthdays does the average person have?",
  'answer': "One. You're only born once.",
  'accept': ['one', '1', 'once' 'born']},
 {'question': "Where was the United States Declaration of Independence signed?",
  'answer': "It was signed at the bottom.",
  'accept': ['bottom']},
 {'question': "A person puts two walnuts in their pocket but only has one thing in their pocket five minutes later. What is it?",
  'answer': "A hole.",
  'accept': ['hole']},
 {'question': "What did the sculptor make that no one could see?",
  'answer': "Noise.",
  'accept': ['noise']},
 {'question': "If you drop a raw egg on a concrete floor, will it crack?",
  'answer': "No. Concrete is very hard to crack.",
  'accept': ['no']},
 {'question': "If it takes ten people ten hours to build a fence, how many hours does it take five people to build it?",
  'answer': "Zero. It's already built.",
  'accept': ['zero', 'no', '0', 'already', 'built']},
 {'question': "Which is heavier, 100 pounds of rocks or 100 pounds of feathers?",
  'answer': "Neither. They weigh the same.",
  'accept': ['neither', 'none', 'no', 'same', 'even', 'balance']},
 {'question': "What do you have to do to survive being bitten by a poisonous snake?",
  'answer': "Nothing. Only venomous snakes are deadly.",
  'accept': ['nothing', 'anything']},
 {'question': "What three consecutive days don't include Sunday, Wednesday, or Friday?",
  'answer': "Yesterday, today, and tomorrow.",
  'accept': ['yesterday', 'today', 'tomorrow']},
 {'question': "If there are ten apples and you take away two, how many do you have?",
  'answer': "Two.",
  'accept': ['2', 'two']},
 {'question': "A 39 year old person was born on the 22nd of February. What year is their birthday?",
  'answer': "Their birthday is on February 22nd of every year.",
  'accept': ['every', 'each']},
 {'question': "How far can you walk in the woods?",
  'answer': "Halfway. Then you are walking out of the woods.",
  'accept': ['half', '1/2']},
 {'question': "Can a man marry his widow's sister?",
  'answer': "No, because he's dead.",
  'accept': ['no']},
 {'question': "What do you get if you divide one hundred by half?",
  'answer': "One hundred divided by half is two hundred. One hundred divided by two is fifty.",
  'accept': ['two', '200']},
 {'question': "What do you call a woman who always knows where her husband is?",
  'answer': "A widow.",
  'accept': ['widow']},
 {'question': "How can someone take a photo but not be a photographer?",
  'answer': "They can be a thief.",
  'accept': ['thief', 'steal', 'take', 'literal']},
 {'question': "An electric train leaves the windy city of Chicago at 4pm on a Monday heading south at 100 kilometers per hour. Which way does the smoke blow from the smokestack?",
  'answer': "Electric trains don't have smokestacks.",
  'accept': ["don't", 'not', 'no', 'none']},
 {'question': 'What is the only word that rhymes with "orange"?',
  'answer': "Orange.",
  'accept': ['orange']},
 {'question': "Who is the U.S. President if the U.S. Vice President dies?",
  'answer': "The current U.S. President.",
  'accept': ['president', 'current', 'already']},
 {'question': "A doctor gives you three pills with instructions to take one every half-hour. How long will the pills last?",
  'answer': "One hour.",
  'accept': ['1', 'one']},
 {'question': "Where is there an ocean with no water?",
  'answer': "On a map.",
  'accept': ['map']},
 {'question': "What is the size of a rhino but weighs nothing?",
  'answer': "A rhino's shadow.",
  'accept': ['shadow']},
 {'question': "The clerk at a butcher shop is exactly 177 centimeters tall. What does he weigh?",
  'answer': "Meat.",
  'accept': ['meat']}]

CORRECT_TEXT = ['Correct!', 'That is right.', "You're right.",
                    'You got it.', 'Righto!']
INCORRECT_TEXT = ['Incorrect!', "Nope, that isn't it.", 'Nope.',
                      'Not quite.', 'You missed it.']

print('''TRICK QUESTIONS
By Al Sweigart al@inventwithpython.com

Can you figure out the answers to these trick questions?
(Enter QUIT to quit at any time.)
''')

input('Press Enter to begin...')

random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS): # Main program loop.
    print('\n' * 40) # "Clear" the screen.
    print('Question:', questionNumber + 1)
    print('Score:', score, '/', len(QUESTIONS))
    print('QUESTION:', qa['question'])
    response = input().lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

    correct = False
    for acceptanceWord in qa['accept']:
        if acceptanceWord in response:
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['answer'])
        score += 1
    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'The answer is:', qa['answer'])
    response = input('Press Enter for the next question...').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()



print("That's all the questions. Thanks for playing!")
