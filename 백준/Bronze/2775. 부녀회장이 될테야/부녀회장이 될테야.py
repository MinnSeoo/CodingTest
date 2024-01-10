def count_people(k, n):
    apartment = [[i for i in range(1, n + 1)] for j in range(k + 1)]
    
    for floor in range(1, k + 1):
        for room in range(n):
            apartment[floor][room] = sum(apartment[floor - 1][:room + 1])
    return apartment[k][n - 1]


test = int(input())

for _ in range(test):
    k = int(input())
    n = int(input())
    print(count_people(k, n))