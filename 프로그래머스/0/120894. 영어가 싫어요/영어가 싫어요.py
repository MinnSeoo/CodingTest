def solution(numbers):
    num_dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 
               'eight': 8, 'nine': 9}
    result = ''
    tmp = ''
    for char in numbers:
        tmp += char
        if tmp in num_dic:
            result += str(num_dic[tmp])
            tmp = ''
    return int(result)