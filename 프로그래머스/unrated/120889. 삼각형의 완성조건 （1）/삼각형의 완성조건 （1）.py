def solution(sides):
    max_sides = max(sides)
    sides_hap = 0
    same = 0
    
    for i in sides:
        if i == max_sides:
            same += 1
            if same >= 2:
                sides_hap += i
        
        if i != max_sides:
            sides_hap += i        
        
    return 1 if max_sides < sides_hap else 2