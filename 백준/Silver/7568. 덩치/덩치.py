N = int(input())
result = []

for _ in range(N):     # N번 입력받음 
    x,y = map(int, input().split())
    result.append((x,y))

for i in result:
    rank = 1
    for j in result:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1 
    print(rank, end = " ")
