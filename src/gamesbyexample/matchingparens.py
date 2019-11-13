# Matching Parentheses, by Al Sweigart al@inventwithpython.com
# A parentheses/bracket/braces matching algorithm.

def isMatchingParens(strToCheck):
    # A Python list is a stack data structure if we only push values on it
    # with the append() method and pop values off it with the pop() method.
    # The "top" of a Python list is the end of list.
    stack = []

    # Loop over every character in strToCheck.
    for i, character in enumerate(strToCheck):
        if character == '(':
            stack.append('(')
            print(strToCheck)
            print((' ' * i) + '^ Push ( to the stack.')
            print('STACK:', stack)
        elif character == '{':
            stack.append('{')
            print(strToCheck)
            print((' ' * i) + '^ Push { to the stack.')
            print('STACK:', stack)
        elif character == '[':
            stack.append('[')
            print(strToCheck)
            print((' ' * i) + '^ Push [ to the stack.')
            print('STACK:', stack)
        elif character == ')' or character == '}' or character == ']':
            if len(stack) == 0:
                print(strToCheck)
                print((' ' * i) + '^ Nothing to pop off the stack.')
                print('STACK:', stack)
                print('STACK IS ALREADY EMPTY.')
                return False # Too many close parens/braces/brackets.

            if stack[-1] == '(':
                expectedCloseChar = ')'
            elif stack[-1] == '{':
                expectedCloseChar = '}'
            elif stack[-1] == '[':
                expectedCloseChar = ']'

            if character == ')' and stack[-1] != '(':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + character + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False # Expected a close parenthesis.
            elif character == '}' and stack[-1] != '{':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + character + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False # Expected a close brace.
            elif character == ']' and stack[-1] != '[':
                print(strToCheck)
                print((' ' * i) + '^ Pop ' + character + ' off the stack.')
                print('STACK:', stack)
                print('EXPECTED A ' + expectedCloseChar)
                return False # Expected a close bracket.

            # Remove the parens/braces/brackets from the end of the stack:
            stack.pop()
            print(strToCheck)
            print((' ' * i) + '^ Pop "' + character + '" off the stack.')
            print('STACK:', stack)
        else:
            print(strToCheck)
            print((' ' * i) + '^ ' + character + ' is ignored.')
            print('STACK:', stack)
        print('Press enter to continue...')
        input()

    # The parens/braces/brackets are matching if the stack is empty.
    isMatching = len(stack) == 0
    if isMatching:
        print('STACK IS EMPTY:', stack)
    else:
        print('STACK IS NOT EMPTY:', stack)
    return isMatching


print("""MATCHING PARENTHESES ALGORITHM
By Al Sweigart al@inventwithpython.com

This program demonstrates an algorithm for detecting matching parentheses,
curly braces, and square brackets in a string. For example:

    MATCHING     NOT MATCHING
    ()           )(
    {}[]         [[]
    ({[]})       ({)}
    {[][](())}   {}}

The algorithm works by using a "stack" data structure, where values are only
added or removed from the "top" of the stack.

To check a string, we loop over each character in order. Opening characters
are "pushed" (added) to the stack, while closing characters "pop" (remove)
the character off of the stack (but only if it's matches the opening
character at the top of the stack.)
The string has matching parentheses/braces/brackets if the stack is empty at
the end of the string.

Enter the string to check:""")
response = input()
print()

result = isMatchingParens(response)
print('"' + response + '"', 'IS MATCHING:', result)