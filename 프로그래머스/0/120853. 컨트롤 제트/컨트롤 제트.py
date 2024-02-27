def solution(s):
    s_list = s.split()
    answer = 0
    
    for idx, n in enumerate(s_list):
        if n != "Z":
            answer += int(n)
        else:
            tmp = s_list[idx-1]
            answer -= int(tmp)
    return answer