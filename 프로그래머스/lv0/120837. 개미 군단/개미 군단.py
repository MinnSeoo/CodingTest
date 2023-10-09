def solution(hp):
    General_Ant = 5
    Soldier_Ant = 3
    Working_Ant = 1
    
    remain = 0
    Max_Ant= 0
    Ant_count = 0
    if hp > General_Ant:
        Max_Ant = hp // General_Ant
        Ant_count += Max_Ant 
        hp -= Max_Ant * General_Ant


    if hp >= Soldier_Ant:
        Max_Ant = hp // Soldier_Ant
        Ant_count += Max_Ant 
        hp -= Max_Ant * Soldier_Ant

    if hp >= Working_Ant:
        Max_Ant = hp // Working_Ant
        Ant_count += Max_Ant 

    return Ant_count



# 풀이2
# def solution(hp):
#     count = 0
#     ants = [5, 3, 1]    

#     for att in ants:
#         count += hp // att
#         hp %= att

#     return count