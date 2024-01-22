test_case = int(input())

for _ in range(test_case):
    quiz_result = input()
    count = 0
    hap = 0
    
    for i in quiz_result:   
        if i == "O":
            count += 1
            hap += count
            
        elif i == "X":
            count = 0
            
    print(hap)
