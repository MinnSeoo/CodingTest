# case 1
def solution(my_string, k):
    answer = []
    
    for s in my_string:
        answer.append(s)
    
    result = "".join(answer)
    return result * k


# case 2
def solution(my_string, k):
    return my_string * k
