def solution(my_string, overwrite_string, s):
    List1 = list(my_string) # my_string 리스트 생성
    List2 = list(overwrite_string)  # overwrite_string 리스트 생성
    j = 0
    for i in range(s,s+len(List2)): # i가 s ~ s+len(List2) - 1 까지 반복
        List1[i] = List2[j] # List2의 j번째 요소값을 List1의 i번째 요소값에 대입
        j += 1  # j가 1 증가
        
    answer = ''.join(List1) # answer 문자열 변수에 list1 대입
    return answer   # answer 변수 반환
