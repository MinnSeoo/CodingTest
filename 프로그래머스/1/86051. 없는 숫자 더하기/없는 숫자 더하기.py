def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            print(i)
            answer += i
    return answer

# Test 
numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers))