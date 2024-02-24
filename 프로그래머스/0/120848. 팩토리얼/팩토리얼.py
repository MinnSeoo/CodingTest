import math

def solution(n):
    check = 0
    while(math.factorial(check) <= n):
        check += 1
    return check - 1