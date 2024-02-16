def solution(number):
    a  = [int(i) for i in number]
    result = 0
    for num in a:
        result += num
    return result % 9