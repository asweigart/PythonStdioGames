"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This and other games are available at https://nostarch.com/XX
Tags: short, artistic"""
__version__ = 0
import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
ONE_DAY = datetime.timedelta(days=1)  # A time duration of one day.

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal():
        year = int(response)
        break

    print('Please enter a numeric year, like 2019.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    # Add the month and year label to the calendar:
    calText = ''  # calText will contain the string of our calendar page.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal lines string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The lines that have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Figure out on what day the month starts (the datetime module
    # handles all the complicated calendar stuff for us here):
    calDate = datetime.date(year, month, 1)

    while True:  # Loop over each week in the month.
        calText += weekSeparator

        # The row with day numbers starts off blank, and then we'll add
        # day numbers in it:
        dayNumberRow = blankRow

        while True:  # Fill in the day number labels for this week:
            # weekDayNumber goes from 0 to 6. We have the "+ 1" since
            # weekday() has Mon (not Sun) as 0:
            weekDayNumber = (calDate.weekday() + 1) % 7

            # Find out where in dayNumberRow we add the day number:
            dayNumberIndex = (weekDayNumber * 11) + 1

            # Add the day number:
            rowPartBeforeDayNumber = dayNumberRow[:dayNumberIndex]
            rowPartAfterDayNumber = dayNumberRow[dayNumberIndex + 2 :]
            dayNumberRow = (
                rowPartBeforeDayNumber
                + str(calDate.day).rjust(2)
                + rowPartAfterDayNumber
            )

            calDate += ONE_DAY  # Move on to the next day in the month.

            # If we've reached Sunday, break and start a new week:
            if calDate.weekday() == 6:
                break

        # Add the day number row and 5 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(5):
            calText += blankRow

        if calDate.month != month:
            break  # We are done with this month and this calendar.

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

# Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)
