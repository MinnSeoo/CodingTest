def solution(array):
    max_num_list = max(array)    # max_num에 array 리스트의 max값 대입
    count = [0] * (max_num_list + 1) # 빈도값을 셀 list (+1 하는 이유는 0 포함하기 위해(dummy 값))
    max_num = 0     # 최대값의 개수를 확인하기 위한 변수
    for i in array:
        count[i] += 1   # +1을 하는 이유는 count의 0번째 인덱스는 dummy 값이기 때문.
    for c in count:
        if c == max(count): # count의 최대값이 같다면 max_num에 + 1 
            max_num +=1 
    if max_num > 1:
        return -1
    else:
        return count.index(max(count))
    
    