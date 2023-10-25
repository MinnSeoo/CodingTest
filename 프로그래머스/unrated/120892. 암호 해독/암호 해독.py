def solution(cipher, code):
    result = ""
    
    for idx,char in enumerate(cipher):
        if (idx + 1) % code == 0:
            result += char
    return result 