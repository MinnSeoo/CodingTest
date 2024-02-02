def solution(seoul):
    kim_idx = [ idx for idx,name in enumerate(seoul) if name == 'Kim' ]
    print_kim = f"김서방은 {kim_idx[0]}에 있다"
    return print_kim
    