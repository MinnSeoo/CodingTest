def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    # case 2
    
    return "Even" if num & 1 == 0 else "Odd"