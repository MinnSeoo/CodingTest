def solution(my_string):
    return ''.join([ i.upper() if i.islower() == True else i.lower() for i in my_string ])