def solution(rny_string):
    result = []
    search = 'm'
    change = 'rn'
    
    for char in rny_string:
        if char == search:
            result.append(change)
        else:
            result.append(char)
    return ''.join(result)