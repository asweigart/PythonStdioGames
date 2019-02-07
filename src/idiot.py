# How to Keep an Idiot Busy for Hours, by Al Sweigart al@inventwithpython.com

while True:
    print('Would you like to know how to keep an idiot busy for hours?')
    response = input().lower()
    if response == 'no' or response == 'n':
        break
    if response == 'yes' or response == 'y':
        continue
    print('"%s" is not a valid yes/no response.' % (response))
print('Thank you. Have a nice day!')