def solution(numbers):
    max_num1 = max(numbers)
    numbers2 = []
    max_cnt = 0
    
    for i in numbers:
        if i == max_num1:
            max_cnt += 1 
    
    if max_cnt >= 2:
        for j in numbers:
            result = max_num1 ** 2
        return result 
    
    for k in numbers:
        if k != max_num1:
            numbers2.append(k)
    max_num2 = max(numbers2)
    result = max_num1 * max_num2
    return result 