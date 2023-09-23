def solution(n):
    answer = 0
    
    if n % 2 == 1:          # 홀수일 경우
        for i in range(1, n + 1):   # range -> 범위는 n부터 n-1까지 / 따라서 + 1을 해줌.
            if i % 2 == 1:  # 홀수중에서 양의 정수를 판별
                answer += i # 모든 양의 정수합을 반환
    else:
        for i in range(1, n + 1):   
            if i % 2 == 0:  # 
                answer += int(i*i)
    
    return answer