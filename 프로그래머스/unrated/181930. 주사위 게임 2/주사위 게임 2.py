# case 1
def solution(a, b, c):
    if a == b and b == c:
        result = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)  # 세 숫자가 모두 같은 경우
    elif a == b or a == c or b == c:
        result = (a + b + c) * (a**2 + b**2 + c**2) # 두 숫자가 같고 나머지 하나가 다른 경우
    else:
        result = a + b + c   # 세 숫자가 모두 다른 경우

    return result


# case 2
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:                        # 세 숫자 모두 같을 때
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:                      # 두 숫자만 같을 때
        return (a+b+c)*(a**2+b**2+c**2)
    else:                               # 세 숫자가 모두 다를 때
        return (a+b+c)