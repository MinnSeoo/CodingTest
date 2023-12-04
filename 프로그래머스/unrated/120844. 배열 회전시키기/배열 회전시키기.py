def solution(numbers,direction):
    new_list = [None for _ in range(len(numbers))]

    for i in range(len(new_list)):
        if direction == "left":
            new_list[i-1] = numbers[i]

        elif direction == "right":
            new_list[(i+1) % len(numbers)] = numbers[i]
    return new_list