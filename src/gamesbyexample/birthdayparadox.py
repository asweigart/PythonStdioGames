"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com

Explore the mathematics of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
Tags: short, math, simulation"""
__version__ = 0

import datetime, random


def getBirthdays(number):
    """Returns a list of number random date objects."""
    birthdays = []
    for i in range(number):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a matching birthday.

    This date object appears more than once in birthdays."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''Birthday Paradox

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly small.
This program does a monte carlo simulation to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input()
    if response.isdecimal() and (0 < int(response) <= 100):
        number = int(response)
        break  # User has entered a valid amount.
    # At this point, go back to the start of the loop.
print()

# Generate and display the birthdays:
print('Here are', number, 'birthdays:')
birthdays = getBirthdays(number)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    dateText = '{} {}'.format(MONTHS[birthday.month - 1], birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    dateText = '{} {}'.format(MONTHS[match.month - 1], match.day)
    print('multiple people have a birthday on ' + dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 1000 simulations and get the matching birthday probability.
print('Press Enter to run 100,000 more monte carlo simulations.')
input()

print('Running simulations of', number, 'people...')
simMatch = 0
for i in range(1, 100001):
    if i % 10000 == 0:
        print(str(i // 1000) + '% done...')
    birthdays = getBirthdays(number)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

# Display simulation results:
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', number, 'people, there was a')
print('matching birthday', simMatch, 'times, or', probability, '%')
