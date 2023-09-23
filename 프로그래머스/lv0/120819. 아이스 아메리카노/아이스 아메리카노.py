def solution(money):
    ice_drink = 5500
    result = []
    
    max_drink = money // ice_drink
    penny = money % ice_drink
    
    result.append(max_drink)
    result.append(penny)
    
    return result