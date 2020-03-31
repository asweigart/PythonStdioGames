"""Calendar Maker, by Al Sweigart al@inventwithpython.com

Create monthly calendars, saved to a text file and fit for printing.
Tags: short, artistic"""
__version__ = 0
import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
ONE_DAY = datetime.timedelta(days=1)

DAY_BOX_SIZE = 10
assert DAY_BOX_SIZE >= len('Wednesday')

print(
    '''Calendar Maker
By Al Sweigart al@inventwithpython.com
'''
)

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric year, like 2019.')
        continue

    year = int(response)
    break

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)

    if 1 <= int(response) <= 12:
        break
    # At this point, go back to the start of the loop.


def getCalendarFor(year, month):
    # Add the month and year label to the calendar:
    calText = ''  # calText will contain the string of our calendar page.
    fullCalendarWidth = DAY_BOX_SIZE * 7
    fullCalendarWidth += 8  # There are 8 vertical lines between boxes.
    calLabel = MONTHS[month - 1] + ' ' + str(year)
    calText += calLabel.center(fullCalendarWidth) + '\n'

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
    calDate = datetime.date(year, month, 1)

    while True:  # Loop for each week in the month.
        if calDate.month != month:
            break  # We are done with this month.

        calText += horizontalLine
        labeledLine = verticalLine

        while True:  # Fill in the day labels for this week:
            if calDate.month != month:
                break  # We are done with this month.

            # Adjust since weekday() has Mon as 0:
            calDay = (calDate.weekday() + 1) % 7
            calLabelIndex = calDay * (DAY_BOX_SIZE + 1) + 1
            labeledLine = (
                labeledLine[:calLabelIndex]
                + str(calDate.day).rjust(2)
                + labeledLine[calLabelIndex + 2 :]
            )

            calDate += ONE_DAY

            # If we've reached Sunday, break and start a new week:
            if calDate.weekday() == 6:
                break
            # At this point, go back to the start of the loop.

        # At this point, we're done with the labeled line.
        calText += labeledLine

        for i in range(DAY_BOX_SIZE // 2):
            calText += verticalLine
        # At this point, go back to the start of the loop.

    # At this point, we're done with the month.
    calText += horizontalLine
    return calText


calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

# Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
