from itertools import combinations

def solution(number):
    number_list = list(combinations(number, 3))
    count = 0   
    for n_list in number_list:
        if sum(n_list) == 0:
            count += 1
    return count