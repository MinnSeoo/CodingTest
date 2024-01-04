def solution(x): 
    str_x = str(x)
    hap = 0
    
    for i in str_x:
        hap += int(i)
    
    return True if x % hap == 0 else False