def solution(myString):
    StringList = myString.split('x')
    SplitList = list(filter(None,StringList))
    
    return sorted(SplitList)
        