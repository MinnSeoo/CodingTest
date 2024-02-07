def solution(s):
    lower_char = ""
    upper_char = ""
    
    for char in s:
        if char.islower():
            lower_char += char
        else:
            upper_char += char
    
    return "".join(sorted(lower_char, reverse=True) + sorted(upper_char, reverse=True))