def solution(arr,n):
    result = []
    
    for idx,num in enumerate(arr):
        if (len(arr) % 2 == 0 and idx % 2 != 0) or (len(arr) % 2 != 0 and idx % 2 == 0):
            result.append(num+n)
        else:
            result.append(num)
    return result