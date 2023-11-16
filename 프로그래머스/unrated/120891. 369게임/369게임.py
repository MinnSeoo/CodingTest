def solution(order):
    result = 0
    str_order = str(order)

    for n in str_order:
        if int(n) in [3,6,9]:
            result += 1
    return result