def solution(n,m):
    gcd = max([i for i in range(1, min(n,m) + 1) if n % i == 0 and m % i == 0])   # 최대공약수
    lcm = min([j for j in range( max(n,m),(n*m + 1) ) if j % n == 0 and j % m == 0])     # 최소공배수
    return [gcd,lcm]