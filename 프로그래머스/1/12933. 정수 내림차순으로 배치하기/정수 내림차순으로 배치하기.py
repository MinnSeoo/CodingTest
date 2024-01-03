def solution(n):
    list_n = list(str(n))
    str_listN = []

    for i in list_n:
        str_listN.append(i)
    
    result = sorted(str_listN, reverse=True)
    return int(''.join(result))
            