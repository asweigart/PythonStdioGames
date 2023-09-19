# Wheel of colors, a game similar to the wheel of fortune,
# Choose a color then spin the wheel,
# And await your destiny

print('''Welcome to the wheel of colors, where /n you can gamble to your hearts content.
Here, if your first guess is correct, your bet is tripled and returned
If your second guess is correct, your bet is doubled and returned

''')

import random

# All possible colors
colorsInWheel = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'black']
# Amount in purse
purse = 500


while purse > 0:
    # Players Guess
    guess1 = str(input('Choose one color : '))
    guess2 = str(input('Choose another color : '))

    # The players bet
    bet = int(input('Enter your bet : '))

    # The color it lands on
    theColor = random.choice(colorsInWheel)

    # The Checking system
    if guess1 == theColor:
        print('Wow! You got it correct! You get', bet * 2, '!')
        purse = purse + (bet * 2)
        print('''You have', purse, 'in your purse!
        
        ''')

    elif guess2 == theColor:
        print('Wow! You got it correct! You get', bet, '!')
        purse = purse + bet
        print('''You have''', purse, '''in your purse!
        
        ''')

    else:
        print('Sorry! The color was :', theColor, '. Better luck next time')
        purse = purse - bet
        print('''You have''', purse, '''in your purse!
        
        ''')


else:
    print('Sorry! You do not have any money left.')
