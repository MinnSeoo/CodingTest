def solution(food):
    pop_bottle = food.pop(0)
    final_food_list = [ i if i % 2 == 0 else i - 1 for i in food ]
    food_num = 1
    left_food = ''
    
    for i in final_food_list:
        half_i = i // 2
        for j in range(half_i): 
            left_food += str(food_num)
        food_num += 1
    
    right_food = list(reversed(left_food))
    right_food = ''.join(right_food)
    print(right_food)
    result = left_food + '0' + right_food
    return result