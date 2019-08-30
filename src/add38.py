# TODO - add a way to quit
# TODO - Add instructions & title
# More info at https://www.youtube.com/watch?v=ZkVSRwFWjy0
# Solution video is here: https://www.youtube.com/watch?v=qjgTcWJ6lZY


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

boardTemplate = r"""            {48}    {49}    {50}
         _  /  _  /  _  /
        / \/  / \/  / \/    {51}
       / {19} \ / {20} \ / {21} \    /
      | {0}  | {1}  | {2}  |--/-----{38}
     / \   / \   / \   / \/    {52}
    / {22} \ / {23} \ / {24} \ / {25} \    /     +--------------+
   | {3}  | {4}  | {5}  | {6}  |--/--{39}  |  Space Map:  |
  / \   / \   / \   / \   / \/       |   01 02 03   |
 / {26} \ / {27} \ / {28} \ / {29} \ / {30} \       |  04 05 06 07 |
| {7}  | {8}  | {9}  | {10}  | {11}  |--{40}  |08 09 10 11 12|
 \   / \   / \   / \   / \   /       |  13 14 15 16 |
  \ / {31} \ / {32} \ / {33} \ / {34} \ /\       |   17 18 19   |
   | {12}  | {13}  | {14}  | {15}  |--\--{41}  +--------------+
    \   / \   / \   / \   /    \
     \ / {35} \ / {36} \ / {37} \ /\    {43}
      | {16}  | {17}  | {18}  |--\-----{42}
       \   / \   / \   /    \
        \_/\  \_/\  \_/\    {44}
            \     \     \
            {47}    {46}    {45}"""
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

    rowSums = {}

    rowSums[1] = nums[1] + nums[2] + nums[3] # Row 1
    if rowSums[1] != 38:
        marks[1] = marks[2] = marks[3] = '_'

    rowSums[2] = nums[4] + nums[5] + nums[6] + nums[7] # Row 2
    if rowSums[2] != 38:
        marks[4] = marks[5] = marks[6] = marks[7] = '_'

    rowSums[3] = nums[8] + nums[9] + nums[10] + nums[11] + nums[12] # Row 3
    if rowSums[3] != 38:
        marks[8] = marks[9] = marks[10] = marks[11] = marks[12] = '_'

    rowSums[4] = nums[13] + nums[14] + nums[15] + nums[16] # Row 4
    if rowSums[4] != 38:
        marks[13] = marks[14] = marks[15] = marks[16] = '_'

    rowSums[5] = nums[17] + nums[18] + nums[19] # Row 5
    if rowSums[5] != 38:
        marks[17] = marks[18] = marks[19] = '_'

    rowSums[6] = nums[3] + nums[7] + nums[12] # Row 6
    if rowSums[6] != 38:
        marks[3] = marks[7] = marks[12] = '_'

    rowSums[7] = nums[2] + nums[6] + nums[11] + nums[16] # Row 7
    if rowSums[7] != 38:
        marks[2] = marks[6] = marks[11] = marks[16] = '_'

    rowSums[8] = nums[1] + nums[5] + nums[10] + nums[15] + nums[19] # Row 8
    if rowSums[8] != 38:
        marks[1] = marks[5] = marks[10] = marks[15] = marks[19] = '_'

    rowSums[9] = nums[4] + nums[9] + nums[14] + nums[18] # Row 9
    if rowSums[9] != 38:
        marks[4] = marks[9] = marks[14] = marks[18] = '_'

    rowSums[10] = nums[8] + nums[13] + nums[17] # Row 10
    if rowSums[10] != 38:
        marks[8] = marks[13] = marks[17] = '_'

    rowSums[11] = nums[1] + nums[4] + nums[8] # Row 11
    if rowSums[11] != 38:
        marks[1] = marks[4] = marks[8] = '_'

    rowSums[12] = nums[2] + nums[5] + nums[9] + nums[13] # Row 12
    if rowSums[12] != 38:
        marks[2] = marks[5] = marks[9] = marks[13] = '_'

    rowSums[13] = nums[3] + nums[6] + nums[10] + nums[14] + nums[17] # Row 13
    if rowSums[13] != 38:
        marks[3] = marks[6] = marks[10] = marks[14] = marks[17] = '_'

    rowSums[14] = nums[7] + nums[11] + nums[15] + nums[18] # Row 14
    if rowSums[14] != 38:
        marks[7] = marks[11] = marks[15] = marks[18] = '_'

    rowSums[15] = nums[12] + nums[16] + nums[19] # Row 15
    if rowSums[15] != 38:
        marks[12] = marks[16] = marks[19] = '_'


    templateArgs = []
    for key in range(1, 20):
        templateArgs.append(str(nums[key]).rjust(2))
    for key in range(1, 20):
        templateArgs.append(marks[key])
    for key in range(1, 16):
        templateArgs.append(str(rowSums[key]).rjust(2))
    print(boardTemplate.format(*templateArgs))


    if '_' not in marks.values():
        print('You\'ve solved the puzzle! Hurray!')
        break

    while True:
        space = input('Select a space from 01 to 19: ')
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
