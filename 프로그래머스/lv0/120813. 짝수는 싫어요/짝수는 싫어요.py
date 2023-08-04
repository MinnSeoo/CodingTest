def solution(n):
    sort_list = []
    cnt = 1
    while n >= cnt:
        if cnt % 2 != 0:
            sort_list.append(cnt)
        cnt += 1
    return sort_list