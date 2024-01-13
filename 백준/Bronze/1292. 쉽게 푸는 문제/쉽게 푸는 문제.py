a,b = map(int,input().split())
hap = 0
sequence = []
check = 0

for i in range(1, b + 1):
    check = i
    for _ in range(check):
        sequence.append(i)

hap = sum(sequence[a-1:b])

print(hap)