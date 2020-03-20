"""Periodic Table of Elements, by Al Sweigart al@inventwithpython.com

Displays atomic information for all the elements.
Tags: short, science"""
__version__ = 1

# Data from https://en.wikipedia.org/wiki/List_of_chemical_elements
# Highlight the table, copy it, then paste it into a spreadsheet program
# like Excel or Google Sheets like in https://invpy.com/elements
# Then save this file as elements.csv.
# Or download this csv file from https://invpy.com/elements.csv

import csv, sys, re

# Read in all the data from elements.csv.
elementsFile = open('elements.csv', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

# To justify the text, we need to find the longest string in ALL_COLUMNS.
LONGEST_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)

# Put all the elements data into a data structure:
ELEMENTS = {}  # The data structure that stores all the element data.
for line in elements:
    element = {'Atomic Number':  line[0],
               'Symbol':         line[1],
               'Element':        line[2],
               'Origin of name': line[3],
               'Group':          line[4],
               'Period':         line[5],
               'Atomic weight':  line[6] + ' u', # atomic mass unit
               'Density':        line[7] + ' g/cm^3', # grams/cubic cm
               'Melting point':  line[8] + ' K', # kelvin
               'Boiling point':  line[9] + ' K', # kelvin
               'Specific heat capacity':      line[10] + ' J/(g*K)',
               'Electronegativity':           line[11],
               'Abundance in earth\'s crust': line[12] + ' mg/kg'}

    # Some of the data has bracketed text from Wikipedia that we want to
    # remove, such as the atomic weight of Boron:
    # "10.81[III][IV][V][VI]" should be "10.81"

    for key, value in element.items():
        # Remove the [roman numeral] text:
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

    ELEMENTS[line[0]] = element  # Map the atomic number to element.
    ELEMENTS[line[1]] = element  # Map the symbol to element.

print('PERIODIC TABLE OF ELEMENTS')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:  # Main program loop.
    # Show table and let the user select an element:
    print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input().title()  # Convert to titlecase e.g. 'mg' to 'Mg'

    if response == 'Quit':
        sys.exit()

    # Display the selected element's data:
    if response in ELEMENTS:
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ' + ELEMENTS[response][key])
        input('Press Enter to continue...')
    # At this point, go back to the start of the main program loop.
