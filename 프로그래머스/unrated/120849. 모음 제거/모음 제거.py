def solution(my_string):
    moeum = ['a','e','i','o','u']
    
    for char in moeum:
        my_string = my_string.replace(char,'')
    return my_string