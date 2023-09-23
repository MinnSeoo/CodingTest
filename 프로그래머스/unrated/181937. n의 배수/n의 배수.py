def solution(num, n):
    return int(not(num % n))   

# num % n 했을때 나누어 떨어지면 true 지만 not을 붙어서 false가 됨 -> 1를 반환!