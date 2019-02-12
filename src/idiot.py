# How to Keep an Idiot Busy for Hours, by Al Sweigart al@inventwithpython.com

while True:
    print('Would you like to know how to keep an idiot busy for hours?')
    response = input()
    if response.lower() == 'no' or response.lower() == 'n':
        break
    if response.lower() == 'yes' or response.lower() == 'y':
        continue
    print('"%s" is not a valid yes/no response.' % (response))

print('Thank you. Have a nice day!')