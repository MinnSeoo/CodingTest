def solution(arr):
    new_list = []
    
    for i in arr:
        if not new_list:
            new_list.append(i)
        else:
            if new_list[-1] != i:
                new_list.append(i)
    return new_list    