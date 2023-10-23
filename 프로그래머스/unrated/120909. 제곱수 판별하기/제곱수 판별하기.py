def solution(n):
    return 1 if any(i * i == n for i in range(n)) else 2