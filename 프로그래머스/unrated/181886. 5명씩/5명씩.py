def solution(names):
    result = []
    
    for idx,name in enumerate(names):
        if idx % 5 == 0:
            result.append(name)
    return result
    