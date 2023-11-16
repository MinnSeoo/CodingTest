def solution(numbers):
    cnt = 0
    sorted_num = sorted(numbers)
    max1 = sorted_num[-1]
    max2 = sorted_num[-2]
    min1 = sorted_num[0]
    min2 = sorted_num[1]
    max_mul = max1 * max2
    min_mul = min1 * min2
    
    # 음수가 있는지 확인 
    for n in numbers:
        if n < 0:
            cnt += 1
    
    # 음수가 2개 이상이면
    if cnt >= 2 and min_mul >= max_mul:
        return min_mul
    else: return max_mul
        