while (True):
    num = int(input())
    reversed_str = ''.join(reversed(str(num)))
    reversed_int = int(reversed_str)
    
    if num == 0:
        break
    elif num != 0:
        if num == reversed_int:
            print("yes")
        elif num != reversed_int:
            print("no")