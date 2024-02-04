def solution(s):
    s_len = len(s)
    
    if s_len % 2 == 0:
        even_answer = s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
        return even_answer
    else:
        odd_answer = s[len(s) // 2]
        return odd_answer