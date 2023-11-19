def solution(strArr):
    new_str =  ''.join( [ word.lower() + ' ' if idx % 2 == 0 else word.upper() + ' '  for idx, word in enumerate(strArr) ] )
    return new_str.split()
    