def solution(n):
    result = []
    
    while n != 1:
        result.append(int(n))
        
        if n % 2 == 0:      # 짝수이면
            n = n // 2
        else:
            n = 3 * n + 1
    result.append(1)
    return result
    
    return answer