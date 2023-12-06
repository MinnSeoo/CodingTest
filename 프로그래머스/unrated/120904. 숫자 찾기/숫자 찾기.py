def solution(num,k):
    num_list = list(str(num))
    k_str = (str(k))
    
    for i in num_list:
        if i == k_str:
            return int(num_list.index(i)) + 1
    return -1
  