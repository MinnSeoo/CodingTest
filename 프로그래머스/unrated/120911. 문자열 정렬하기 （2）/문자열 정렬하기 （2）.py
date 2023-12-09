def solution(my_string):
    new_string = my_string.lower()
    result = sorted(new_string)
    
    return ''.join(result)