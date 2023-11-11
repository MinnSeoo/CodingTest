import math

def solution(num_list):
    mul = math.prod(num_list)
    hap = sum(num_list)
    hap_sqare = hap ** 2 
    
    if mul > hap_sqare:
        return 0
    else:
        return 1