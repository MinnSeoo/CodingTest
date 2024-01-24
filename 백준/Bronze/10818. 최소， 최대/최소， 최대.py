n = int(input())

input_num = input().split()
num_list = []

for i in input_num[:n]:
    num_list.append(int(i))
    
max_num = max(num_list)
min_num = min(num_list)

print(min_num, max_num)
    