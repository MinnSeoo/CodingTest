def solution(a, b):
    hap1 = str(a) + str(b) 
    hap2 = 2 * a * b
    
    if int(hap1) > hap2:
        return int(hap1)
    
    elif int(hap1) < hap2:
        return hap2
    
    elif int(hap1) == hap2:
        return hap1