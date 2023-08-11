import statistics

def solution(array):
    result = 0
    array.sort()
    result = statistics.median(array)
    return result