import re
from collections import deque


pattern = r"\(|\)|\[|\]"

while 1:
    answer = "yes"
    sentence = input()
    parentheses_stack = deque()
    if sentence == ".":
        break

    parentheses_array = re.findall(pattern, sentence)
    parentheses_array2 = parentheses_array
    length_parentheses_array = len(parentheses_array)
    if length_parentheses_array % 2 == 1 and length_parentheses_array == 0:
        answer = "no"
    else:
        for parentheses in parentheses_array2:

            if parentheses == '(' or parentheses == '[':
                parentheses_stack.append(parentheses)
            elif len(parentheses_stack) > 0:
                open_parenthesis = parentheses_stack.pop()

                if open_parenthesis == '(':
                    open_parenthesis = ')'

                    if open_parenthesis == parentheses:
                        continue
                    else:
                        answer = "no"
                        break
                elif open_parenthesis == '[':
                    open_parenthesis = ']'
                    if open_parenthesis == parentheses:
                        continue
                    else:
                        answer = "no"
                        break
            else:
                answer = "no"
                break
    if len(parentheses_stack) > 0:
        answer = "no"

    print(answer)
