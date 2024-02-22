def solution(num_list, n):
    result = []
    for _ in range(len(num_list) // n): 
        tmp = []
        for _ in range(n): 
            tmp.append(num_list.pop(0))
        result.append(tmp)
    return result
