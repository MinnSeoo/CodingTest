def solution(n):
    num_list = []
    cnt = 1
    while n >= cnt:
        if cnt % 2 != 0:    # 홀수이면 list에 추가
            num_list.append(cnt)
        cnt += 1

    sort_list = sorted(num_list)    # num_list를 정렬해 새로운 sort_list에 값 저장
    return sort_list
