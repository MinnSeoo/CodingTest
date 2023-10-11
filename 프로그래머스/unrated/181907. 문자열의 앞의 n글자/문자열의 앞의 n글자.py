def solution(my_string, n):
    new_string = ""
    
    for i, char in enumerate(my_string):
        if i < n:
            new_string += char
    return new_string