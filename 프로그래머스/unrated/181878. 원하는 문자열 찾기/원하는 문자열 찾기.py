def solution(my_string, pat):
    upper_myString = my_string.upper()
    upper_pat = pat.upper()
    
    return 1 if upper_pat in upper_myString else 0