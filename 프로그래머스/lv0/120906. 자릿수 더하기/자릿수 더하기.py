def solution(n):
    n_str = str(n)
    # n_list = list(n_str)
    result = 0
    
    for i in n_str:
        result += int(i)
    return result
        