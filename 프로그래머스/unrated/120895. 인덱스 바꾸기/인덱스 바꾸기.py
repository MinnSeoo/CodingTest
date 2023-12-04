def solution(my_string, num1, num2):
    ns = list(my_string)
    
    ns[num1], ns[num2] = ns[num2], ns[num1]
    
    return ''.join(ns)
    