def solution(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i**2 == n:
                return (i + 1) ** 2
    return -1