def solution(n):
    cnt = 0
    
    while True:
        if n == 1:
            break
        if cnt == 500:
            break
        if n % 2 == 0: 
            n = n // 2
            cnt += 1
        else:
            n = n * 3 + 1
            cnt += 1 
    
    return cnt if cnt != 500 else -1 