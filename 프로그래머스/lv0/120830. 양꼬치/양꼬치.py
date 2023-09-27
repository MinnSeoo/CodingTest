def solution(n, k):
    food_price = 12000
    drink_price = 2000
    service_drink = 0
    result = 0
    
    for food_eat in range(1,n+1):
        if food_eat % 10 == 0:
            service_drink += 1
            
    result = (n * food_price) + (drink_price * (k - service_drink))
    return result