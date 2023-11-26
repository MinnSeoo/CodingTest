def solution(arr, delete_list):
    new_arr = []
    for idx,num in enumerate(arr):
        if num not in delete_list:
           new_arr.append(num)
    return new_arr