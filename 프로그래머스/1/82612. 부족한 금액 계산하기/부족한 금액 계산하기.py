def solution(price, money, count):
    N_price = 0
    for c in range(1, count + 1):
        N_price += price * c 
    
    if N_price < money:
        return 0
    else:
        result = abs(money - N_price)
        return result 
