n = int(input("자연수 N을 입력하세요. : "))
print(n)
n_sum = 0      # n의 합
square_sum = 0      # 제곱의 합

for i in range(1,n+1):
    n_sum += i
    square_sum += i ** 2
    
sum_square = n_sum ** 2
print(sum_square - square_sum)