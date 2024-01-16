count = int(input())
answer = []

for i in range(count):
    answer.append(input())

result = sorted(set(answer), key = lambda x: (len(x), x))

for j in result:
    print(j)