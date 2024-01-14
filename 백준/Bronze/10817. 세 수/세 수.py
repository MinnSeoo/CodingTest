a, b, c = map(int, input().split())
num_list = [a, b, c]
sorted_list = sorted(num_list)
second_max_num = sorted_list[1]

print(int(second_max_num))