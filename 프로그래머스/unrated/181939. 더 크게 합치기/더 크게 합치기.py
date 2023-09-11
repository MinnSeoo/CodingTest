# case 1
def solution(a, b):
    hap1 = str(a) + str(b)
    hap2 = str(b) + str(a)
    
    if int(hap1) > int(hap2):
        return int(hap1)
    
    elif int(hap1) < int(hap2):
        return int(hap2)
    
    elif int(hap1) == int(hap2):
        return int(hap1)
    
    
# case 2
def solution(a, b):
    hap1 = str(a) + str(b)
    hap2 = str(b) + str(a)
    
    return int(hap1) if int(hap2) < int(hap1) else int(hap2)
