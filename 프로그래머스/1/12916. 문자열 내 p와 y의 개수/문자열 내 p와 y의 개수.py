def solution(s):
    cnt_p = 0
    cnt_y = 0
    
    for char in s:
        if char == 'P' or char == 'p':
            cnt_p += 1
        elif char == 'Y' or  char == 'y':
            cnt_y += 1
    
    if cnt_p == cnt_y:
        return True
    else:
        return False