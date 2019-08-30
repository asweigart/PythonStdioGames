import random

# https://pastebin.com/raw/h9ufKzSz
boardTemplate = r"""         _     _     _
        / \   / \   / \
       / {19} \ / {20} \ / {21} \
      | {0}  | {1}  | {2}  |
     / \   / \   / \   / \
    / {22} \ / {23} \ / {24} \ / {25} \
   | {3}  | {4}  | {5}  | {6}  |
  / \   / \   / \   / \   / \
 / {26} \ / {27} \ / {28} \ / {29} \ / {30} \
| {7}  | {8}  | {9}  | {10}  | {11}  |
 \   / \   / \   / \   / \   /
  \ / {31} \ / {32} \ / {33} \ / {34} \ /
   | {12}  | {13}  | {14}  | {15}  |
    \   / \   / \   / \   /
     \ / {35} \ / {36} \ / {37} \ /
      | {16}  | {17}  | {18}  |
       \   / \   / \   /
        \_/   \_/   \_/"""

#print(boardTemplate.format(*[str(i).rjust(2) for i in range(1, 20)] + ['_'] * 19))

nums = {}
for key in range(1, 20):
    nums[key] = key

r"""
ROW NUMBERING:
          12  14
       11 / 13/15
       / / / / /
      * * *-/-/--1
     * * * *-/---2
    * * * * *----3
     * * * *-\---4
      * * *-\-6--5
       \ \ \ 7
       10 9 8

"""


while True:
    # Determine which spaces are part of rows that don't add up to 38:
    marks = {}
    for key in range(1, 20):
        marks[key] = ' '

    if nums[1] + nums[2] + nums[3] != 38: # Row 1
        marks[1] = marks[2] = marks[3] = '_'

    if nums[4] + nums[5] + nums[6] + nums[7] != 38: # Row 2
        marks[4] = marks[5] = marks[6] = marks[7] = '_'

    if nums[8] + nums[9] + nums[10] + nums[11] + nums[12] != 38: # Row 3
        marks[8] = marks[9] = marks[10] = marks[11] = marks[12] = '_'

    if nums[13] + nums[14] + nums[15] + nums[16] != 38: # Row 4
        marks[13] = marks[14] = marks[15] = marks[16] = '_'

    if nums[17] + nums[18] + nums[19] != 38: # Row 5
        marks[17] = marks[18] = marks[19] = '_'

    if nums[3] + nums[7] + nums[12] != 38: # Row 6
        marks[3] = marks[7] = marks[12] = '_'

    if nums[2] + nums[6] + nums[11] + nums[16] != 38: # Row 7
        marks[2] = marks[6] = marks[11] = marks[16] = '_'

    if nums[1] + nums[5] + nums[10] + nums[15] + nums[19] != 38: # Row 8
        marks[1] = marks[5] = marks[10] = marks[15] = marks[19] = '_'

    if nums[4] + nums[9] + nums[14] + nums[18] != 38: # Row 9
        marks[4] = marks[9] = marks[14] = marks[18] = '_'

    if nums[8] + nums[13] + nums[17] != 38: # Row 10
        marks[8] = marks[13] = marks[17] = '_'

    if nums[1] + nums[4] + nums[8] != 38: # Row 11
        marks[1] = marks[4] = marks[8] = '_'

    if nums[2] + nums[5] + nums[9] + nums[13] != 38: # Row 12
        marks[2] = marks[5] = marks[9] = marks[13] = '_'

    if nums[3] + nums[6] + nums[10] + nums[14] + nums[17] != 38: # Row 3
        marks[3] = marks[6] = marks[10] = marks[14] = marks[17] = '_'

    if nums[7] + nums[11] + nums[15] + nums[18] != 38: # Row 14
        marks[7] = marks[11] = marks[15] = marks[18] = '_'

    if nums[12] + nums[16] + nums[19] != 38: # Row 15
        marks[12] = marks[16] = marks[19] = '_'


    templateArgs = []
    for key in range(1, 20):
        templateArgs.append(str(nums[key]).rjust(2))
    for key in range(1, 20):
        templateArgs.append(marks[key])
    print(boardTemplate.format(*templateArgs))


    if '_' not in marks.values():
        print('You\'ve solved the puzzle! Hurray!')
        break

    while True:
        print("""Select a space from 1 to 19:  _1 _2 _3
                             _4 _5 _6 _7
                           _8 _9 10 11 12
                             13 14 15 16
                              17 18 19""")

        space = input()
        if space.isdecimal() and (1 <= int(space) <= 19):
            break

    while True:
        print('Enter a number to place in space #' + space + ':')
        number = input()
        if number.isdecimal() and (1 <= int(number) <= 19):
            break

    numberAtSpace = nums[int(space)]
    for key in range(1, 20):
        if nums[key] == int(number):
            otherSpace = key

    nums[int(space)] = int(number)
    nums[otherSpace] = numberAtSpace
