def solution(strArr):
    return [char for char in strArr if "ad" not in char]
    
    # 만약 문자에 ad가 포함되어있다면 제거 후 반환