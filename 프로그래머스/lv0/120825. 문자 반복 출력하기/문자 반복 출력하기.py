def solution(my_string, n):
    result = ''
    my_list = []
    for char in my_string:  # 문자열을 리스트로 변환
        my_list.append(char)
        
    for char in my_list:    # char에는 my_list의 0번째의 문자부터 마지막 문자까지 차례로 할당됨.
        result += char * n  # result에 char에 저장된 단어를 n의 개수 만큼 저장함.
        
    return result

            