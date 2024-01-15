N, X = map(int,input().split())
A = list(input().split()[:N])
result = []

for num in A:
    if int(num) < X:
        result.append(int(num))

print(*result)