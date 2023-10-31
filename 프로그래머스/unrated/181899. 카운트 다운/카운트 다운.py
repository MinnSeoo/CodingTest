def solution(start, end_num):
    result = []
    
    for i in range(end_num, start + 1):
        result.append(i)
        
    return list(reversed(result))