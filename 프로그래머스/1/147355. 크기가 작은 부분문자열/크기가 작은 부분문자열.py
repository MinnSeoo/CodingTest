def solution(t,p):
    new_list = []   
    list_t = list(t)
    
    while(len(list_t) >= len(p)):
        tmp = ''
        for i in range(len(p)):
            tmp += list_t[i]
        new_list.append(tmp)
        list_t.pop(0)    
    
    a = [1 for num in new_list if num <= p ]
    return len(a)