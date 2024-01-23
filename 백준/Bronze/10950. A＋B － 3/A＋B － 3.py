T = int(input())
i = 1
sum = []
while (i <= T) :
    A, B = map(int, input().split())
    sum.append(A + B)
    i += 1

for j in sum:
    print(j)