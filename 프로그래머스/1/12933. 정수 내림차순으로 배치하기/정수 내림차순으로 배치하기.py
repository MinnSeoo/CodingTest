def solution(n):
    list_n = list(str(n))
    result = sorted(list_n, reverse=True)
    
    return int(''.join(result))