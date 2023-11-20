def solution(num_list):
    add = 0
    odd = 0
    
    for idx,num in enumerate(num_list):
        if idx % 2 == 0:
            add += num
        else : odd += num
    
    return add if add > odd else odd