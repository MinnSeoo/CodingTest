def solution(n):
    i = 2
    result = []
    answer = []
    while n >= i:
        if n % i == 0:
            result.append(i)
            n = n // i      # 몫을 n에 저장
        else:
            i += 1
    
    for num in result:
        if num not in answer:
            answer.append(num)
    
    answer.sort()
    
    return answer