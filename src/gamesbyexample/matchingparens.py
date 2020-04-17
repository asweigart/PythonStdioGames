"""Matching Parentheses, by Al Sweigart al@inventwithpython.com
A parentheses/bracket/braces matching algorithm.
This and other games are available at https://nostarch.com/XX
Tags: short, algorithm"""
__version__ = 0
def main():
    print('''Matching Parentheses Algorithm
    By Al Sweigart al@inventwithpython.com

    This demonstrates an algorithm for detecting matching parentheses,
    curly braces, and square brackets in a string. For example:

        MATCHING     NOT MATCHING
        ()           )(
        {}[]         [[]
        ({[]})       ({)}
        {[][](())}   {}}

    The algorithm works by using a "stack" data structure, where values
    are only added or removed from the "top" of the stack.

    To check a string, we loop over each symbol in order. Opening
    symbols are "pushed" (added) to the stack, while closing symbols
    "pop" (remove) the symbol off of the stack (but only if it's matches
    the opening symbol at the top of the stack.)
    The string has matching parentheses/braces/brackets if the stack is
    empty at the end of the string.
    ''')
    print('Enter the string to check, for example {[][](())}:')
    response = input('> ')
    print()

    result = isMatchingParens(response)
    print('"' + response + '"', 'IS MATCHING:', result)


def isMatchingParens(strToCheck):
    # A Python list is a stack data structure if we only push values on
    # it with the append() method and pop values off it with the pop()
    # method. The "top" of a Python list is the end of list.
    stack = []

    # Loop over every character in strToCheck.
    for i, char in enumerate(strToCheck):
        if char == '(':
            stack.append('(')
            print(strToCheck)
            print((' ' * i) + '^ Push ( to the stack.')
            print('STACK:', stack)
        elif char == '{':
            stack.append('{')
            print(strToCheck)
            print((' ' * i) + '^ Push { to the stack.')
            print('STACK:', stack)
        elif char == '[':
            stack.append('[')
            print(strToCheck)
            print((' ' * i) + '^ Push [ to the stack.')
            print('STACK:', stack)
        elif char == ')' or char == '}' or char == ']':
            if len(stack) == 0:
                print(strToCheck)
                print((' ' * i) + '^ Nothing to pop off the stack.')
                print('STACK:', stack)
                print('STACK IS ALREADY EMPTY.')
                return False  # Too many close parens/braces/brackets.

            if stack[-1] == '(':
                expectedCloseChar = ')'
            elif stack[-1] == '{':
                expectedCloseChar = '}'
            elif stack[-1] == '[':
                expectedCloseChar = ']'

            if char == ')' and stack[-1] != '(':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + char + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False  # Expected a close parenthesis.
            elif char == '}' and stack[-1] != '{':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + char + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False  # Expected a close brace.
            elif char == ']' and stack[-1] != '[':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + char + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False  # Expected a close bracket.

            # Remove the parens/braces/brackets from the stack's end:
            stack.pop()
            print(strToCheck)
            print((' ' * i) + '^ Pop "' + char + '" off the stack.')
            print('STACK:', stack)
        else:
            print(strToCheck)
            print((' ' * i) + '^ ' + char + ' is ignored.')
            print('STACK:', stack)
        input('Press Enter to continue...')

    # The parens/braces/brackets are matching if the stack is empty.
    isMatching = len(stack) == 0
    if isMatching:
        print('STACK IS EMPTY:', stack)
    else:
        print('STACK IS NOT EMPTY:', stack)
    return isMatching


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()
