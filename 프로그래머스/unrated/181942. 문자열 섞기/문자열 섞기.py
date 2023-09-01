def solution(str1, str2):
    s1 = list(str1)
    s2 = list(str2)
    new_list = []
    
    for i in range(0, len(s1)):
        new_list.append(s1[i])
        new_list.append(s2[i])
    answer = ''.join(new_list)
    return answer
    