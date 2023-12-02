def solution(array):
    max_num = max(array)
    
    for idx,num in enumerate(array):
        if num == max_num:
            max_idx = idx
    return [max_num, max_idx]