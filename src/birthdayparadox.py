# Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
# More info at https://en.wikipedia.org/wiki/Birthday_problem

import datetime, random

def getBirthdays(number):
    birthdays = []
    for i in range(number):
        birthday = datetime.date(2001, 1, 1) + datetime.timedelta(random.randint(0, 364))
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None.

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            #if a == b:
            #    continue # Don't compare a person's own birthday.
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday.

# Display the intro:
print('''Birthday Paradox

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly small.
This program does a monte carlo simulation to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    number = input()
    if number.isdigit() and (0 < int(number) <= 100):
        number = int(number)
        break # User has entered a valid amount.
print()

# Generate and display the birthdays:
print('Here are', number, 'birthdays:')
birthdays = getBirthdays(number)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    print(MONTHS[birthday.month - 1] + ' ' + str(birthday.day), end='')
print()
print()

# Determine if there are two birthdays that match.
matchingBirthday = getMatch(birthdays)

# Display the results:
if matchingBirthday != None:
    print('Multiple people have a birthday on ' + MONTHS[matchingBirthday.month - 1] + ' ' + str(matchingBirthday.day))
else:
    print('There are no matching birthdays.')
print()

# Run through 1000 simulations and get the matching birthday probability.
print('Press Enter to run 100,000 monte carlo simulations.')
input()

print('Running simulations of', number, 'people...')
simMatch = 0
for i in range(100000):
    birthdays = getBirthdays(number)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

# Display simulation results:
print('Out of 100,000 simulations of', number, 'people, there was a')
print('matching birthday', simMatch, 'times.')
print('The probability is therefore', round(simMatch / 100000 * 100, 2), '%')

