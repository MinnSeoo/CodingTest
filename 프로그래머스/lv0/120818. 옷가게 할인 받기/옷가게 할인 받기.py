def solution(price):
    discount = 0
    discount_price = 0
    
    if price >= 500000:     # 50만원 이상 구매시
        discount = price * 0.2  # 20% 할인 값을 discount에 저장
        discount_price = price - discount   # 원가에서 discount 값을 뺀 값을 저장
        return int(discount_price)   # 최종금액인 discount_price를 반환
    
    elif price >= 300000:   # 30만원 이상 구매시
        discount = price * 0.1  # 10% 할인 값을 저장
        discount_price = price - discount  # 원가에 할인값을 뺀 값을 저장
        return int(discount_price)  # 최종금액인 discount_price를 반환
    
    elif price >= 100000:   # 10만원 이상 구매시
        discount = price * 0.05 # 1% 할인 값을 discount에 저장
        discount_price = price - discount   # 원가에 할인값을 뺀 값을 저장
        return int(discount_price)  # 최종금액인 discount_price를 반환

    else:
        return price

    
        
        