def solution(arr, idx):
    for arr_idx, num in enumerate(arr):
        if arr_idx >= idx and num == 1:
            return arr_idx
    return -1