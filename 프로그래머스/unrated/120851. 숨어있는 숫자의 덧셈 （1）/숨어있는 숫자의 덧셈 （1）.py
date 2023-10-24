import re

def solution(my_string):
    result = 0
    num = re.findall(r'\d', my_string)

    for i in num:
        result += int(i)
    return result