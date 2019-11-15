# Calendar Maker, by Al Sweigart al@inventwithpython.com
# Create monthly calendars, saved to a text file and fit for printing.

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
ONE_DAY = datetime.timedelta(days=1)

DAY_BOX_SIZE = 10
assert DAY_BOX_SIZE >= 9

print('''Calendar Maker
By Al Sweigart al@inventwithpython.com
''')

while True: # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    year = input()

    try:
        year = int(year)
    except:
        print('Please enter a numeric year, like 2019.')
        continue
    break

while True: # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    month = input()

    try:
        month = int(month)
    except:
        print('Please enter a numeric month, like 3 for March.')
        continue

    if 1 <= month <= 12:
        break

def getCalendarFor(year, month):
    # Add the month and year label to the calendar:
    calText = '' # calText will contain the string of our calendar page.
    fullCalendarWidth = 8 + (DAY_BOX_SIZE * 7) # There are 8 vertical lines.
    calText += '{} {}'.format(MONTHS[month - 1], year).center(fullCalendarWidth) + '\n'

    # Add the days of the week labels to the calendar:
    calText += ' '
    for day in DAYS:
        calText += day.center(DAY_BOX_SIZE)
        if day != DAYS[-1]:
            calText += ' '
    calText += '\n'

    # Create the horizontal lines:
    horizontalLine = (('+' + ('-' * DAY_BOX_SIZE)) * 7) + '+\n'

    # Create the vertical line:
    verticalLine = (('|' + (' ' * DAY_BOX_SIZE)) * 7) + '|\n'

    # Figure out on what day the month starts:
    #breakpoint()
    calDate = datetime.date(year, month, 1)

    while True: # Loop for each week.
        if calDate.month != month:
            break # We are done with this month.

        calText += horizontalLine
        labeledLine = verticalLine

        while True: # Fill in the day labels for this week:
            if calDate.month != month:
                break # We are done with this month.

            calDay = (calDate.weekday() + 1) % 7 # Adjust since weekday() has Mon as 0.
            calLabelIndex = calDay * (DAY_BOX_SIZE + 1) + 1
            labeledLine = labeledLine[:calLabelIndex] + str(calDate.day).rjust(2) + labeledLine[calLabelIndex+2:]

            calDate += ONE_DAY

            if calDate.weekday() == 6: # If we've reached Sunday, break and start a new week.
                break

        # At this point, we're done with the labeled line.
        calText += labeledLine

        for i in range(DAY_BOX_SIZE // 2):
            calText += verticalLine

    # At this point, we're done with the month.

    calText += horizontalLine

    return calText


calText = getCalendarFor(year, month)

# Display the calendar:
print(calText)

# Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print(f'Saved to {calendarFilename}.')