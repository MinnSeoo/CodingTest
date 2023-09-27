def solution(numbers, num1, num2):
    result = []
    for index, value in enumerate(numbers):     
        if index in range(num1, num2+1):
            result.append(value)
    return result


# enumerate는 반복 가능한 객체(리스트, 튜플, 문자열 등)을/를 순회하면서
# 각 요소의 인덱스와 값을 함께 반환하는데 사용된다.

