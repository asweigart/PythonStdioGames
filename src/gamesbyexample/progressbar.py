"""Progress Bar Simulation, by Al Sweigart al@inventwithpython.com
A sample progress bar animation that can be used in other programs.
This and other games are available at https://nostarch.com/XX
Tags: tiny, module"""
__version__ = 0
import random, time

BAR = chr(9608) # Character 9608 is '█'

def main():
    # Simulate a download:
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # "Download" a random amount of "bytes":
        bytesDownloaded += random.randint(0, 100)

        # Get the progress bar string for this amount of progress:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # Don't print a newline at the end, and immediately flush the
        # printed string to the screen:
        print(barStr, end='', flush=True)

        time.sleep(0.2)  # Pause for a little bit:

        # Print backspaces to move the text cursor to the line's start:
        print('\b' * len(barStr), end='', flush=True)


def getProgressBar(progress, total, barWidth=40):
    """Returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of a total amount."""

    progressBar = ''  # The progress bar will be a string value.
    progressBar += '['  # Create the left end of the progress bar.

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars  # Add the progress bar.
    progressBar += ' ' * (barWidth - numberOfBars)  # Add empty space.
    progressBar += ']'  # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # Add percentage.

    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar  # Return the progress bar string.


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
