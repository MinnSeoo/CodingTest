def solution(absolutes, signs):
    answer = 0
    for idx,num in enumerate(absolutes):
        if signs[idx] == True:
            answer += num
        elif signs[idx] == False:
            answer -= num
    return answer