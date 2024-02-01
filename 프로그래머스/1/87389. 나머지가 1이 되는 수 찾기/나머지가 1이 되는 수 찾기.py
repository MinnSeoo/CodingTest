def solution(n):
    num_list = []
    for i in range(1, n + 1):
        if n % i == 1:
            num_list.append(i)
        
    return min(num_list)

n = 12
print(solution(n))