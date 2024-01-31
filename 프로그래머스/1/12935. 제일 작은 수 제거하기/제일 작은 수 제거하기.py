def solution(arr):
    min_num = min(arr)
    
    if len(arr) == 1:
        return [-1]
    
    else:    
        for i in arr:
            if i == min_num:
                arr.remove(i)
        return arr