def solution(num_list):
    new_list = []
    even = 0
    odd = 0
    
    for i in num_list:
        if i % 2 == 0:
            even += 1 
        else:
            odd += 1
    new_list.append(even)
    new_list.append(odd)
    
    return new_list
    
        