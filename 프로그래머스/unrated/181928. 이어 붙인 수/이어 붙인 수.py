def solution(num_list):
    even = ""
    odd = ""
    result = 0
    
    for i in num_list:
        if i % 2 != 0: odd += str(i)
        else: even += str(i)
        
    result = int(odd) + int(even)
    return result

    
    
            
    
         