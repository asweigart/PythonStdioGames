import csv, sys, re

ALL_KEYS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group', 'Period', 'Atomic weight', 'Density', 'Melting point', 'Boiling point', 'Specific heat capacity', 'Electronegativity', 'Abundance in earth\'s crust']
LONGEST_KEY = 0
for key in ALL_KEYS:
    if len(key) > LONGEST_KEY:
        LONGEST_KEY = len(key)

def displayPeriodicTable():
    print('''
  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
1 H                                                  He
2 Li Be                               B  C  N  O  F  Ne
3 Na Mg                               Al Si P  S  Cl Ar
4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

        Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
        Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
''')

# Read in all the elements information.
elementsFile = open('elements.csv')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

# Put all the elements data into a data structure.
ELEMENTS = {}
pat = re.compile(r'\[(I|V|X)+\]')

for line in elements:
    element = {'Atomic Number':  line[0],
               'Symbol':         line[1],
               'Element':        line[2],
               'Origin of name': line[3],
               'Group':          line[4],
               'Period':         line[5],
               'Atomic weight': pat.sub('', line[6]),
               'Density':       pat.sub('', line[7]),
               'Melting point': pat.sub('', line[8]),
               'Boiling point': pat.sub('', line[9]),
               'Specific heat capacity':    line[10],
               'Electronegativity':         line[11],
               'Abundance in earth\'s crust': pat.sub('', line[12])}
    ELEMENTS[line[1]] = element

while True:
    displayPeriodicTable()
    print('Enter a symbol to examine, or press Ctrl-C to quit.')
    try:
        symbol = input().title()
    except KeyboardInterrupt:
        sys.exit()

    if symbol in ELEMENTS:
        for key in ALL_KEYS:
            print(key.rjust(LONGEST_KEY) + ': ' + ELEMENTS[symbol][key])
        input('Press Enter to continue...')


















names = '''Hydrogen
Helium
Lithium
Beryllium
Boron
Carbon
Nitrogen
Oxygen
Fluorine
Neon
Sodium
Magnesium
Aluminium
Silicon
Phosphorus
Sulfur
Chlorine
Argon
Potassium
Calcium
Scandium
Titanium
Vanadium
Chromium
Manganese
Iron
Cobalt
Nickel
Copper
Zinc
Gallium
Germanium
Arsenic
Selenium
Bromine
Krypton
Rubidium
Strontium
Yttrium
Zirconium
Niobium
Molybdenum
Technetium
Ruthenium
Rhodium
Palladium
Silver
Cadmium
Indium
Tin
Antimony
Tellurium
Iodine
Xenon
Caesium
Barium
Lanthanum
Cerium
Praseodymium
Neodymium
Promethium
Samarium
Europium
Gadolinium
Terbium
Dysprosium
Holmium
Erbium
Thulium
Ytterbium
Lutetium
Hafnium
Tantalum
Tungsten
Rhenium
Osmium
Iridium
Platinum
Gold
Mercury
Thallium
Lead
Bismuth
Polonium
Astatine
Radon
Francium
Radium
Actinium
Thorium
Protactinium
Uranium
Neptunium
Plutonium
Americium
Curium
Berkelium
Californium
Einsteinium
Fermium
Mendelevium
Nobelium
Lawrencium
Rutherfordium
Dubnium
Seaborgium
Bohrium
Hassium
Meitnerium
Darmstadtium
Roentgenium
Copernicium
Nihonium
Flerovium
Moscovium
Livermorium
Tennessine
Oganesson'''.split('\n')

groups = '''1
18
1
2
13
14
15
16
17
18
1
2
13
14
15
16
17
18
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
1
2
3














4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
1
2
3














4
5
6
7
8
9
10
11
12
13
14
15
16
17
18'''.split('\n')

periods = '''1
1
2
2
2
2
2
2
2
2
3
3
3
3
3
3
3
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
5
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7
7'''.split('\n')

numbers = '''1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118'''.split('\n')


symbols = '''H
He
Li
Be
B
C
N
O
F
Ne
Na
Mg
Al
Si
P
S
Cl
Ar
K
Ca
Sc
Ti
V
Cr
Mn
Fe
Co
Ni
Cu
Zn
Ga
Ge
As
Se
Br
Kr
Rb
Sr
Y
Zr
Nb
Mo
Tc
Ru
Rh
Pd
Ag
Cd
In
Sn
Sb
Te
I
Xe
Cs
Ba
La
Ce
Pr
Nd
Pm
Sm
Eu
Gd
Tb
Dy
Ho
Er
Tm
Yb
Lu
Hf
Ta
W
Re
Os
Ir
Pt
Au
Hg
Tl
Pb
Bi
Po
At
Rn
Fr
Ra
Ac
Th
Pa
U
Np
Pu
Am
Cm
Bk
Cf
Es
Fm
Md
No
Lr
Rf
Db
Sg
Bh
Hs
Mt
Ds
Rg
Cn
Nh
Fl
Mc
Lv
Ts
Og'''.split('\n')

