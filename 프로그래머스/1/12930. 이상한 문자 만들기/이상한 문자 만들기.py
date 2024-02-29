def solution(s):
    s_split = s.split(" ")      # 함수의 인자값으로 공백 설정
    result = ''

    for word in s_split:
        for idx in range(len(word)): # 한개 단어 for문
            if idx % 2 == 0:        # 짝수
                result += word[idx].upper() 
            else: 
                result += word[idx].lower()
        result += ' '
    return result[0:-1]
