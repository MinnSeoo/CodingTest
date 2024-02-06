def solution(left,right):
    now_num = [i for i in range(left, right + 1)]
    result = 0
    
    for num in now_num:
        divisorList = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisorList.append(i)
        if len(divisorList) % 2 == 0:
            result += num
        else:
            result -= num
    return result


# test code
left = 13
right = 17
print(solution(left, right))