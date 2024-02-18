n,m = map(int,input().split())      
num_list = list(map(int,input().split()))
result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            choice = num_list[i] + num_list[j] + num_list[k]
            if choice <= m:
                result.append(choice)
print(max(result))
