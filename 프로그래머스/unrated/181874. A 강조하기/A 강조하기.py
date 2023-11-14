def solution(myString):
    lower_String = myString.lower()
    return "".join([ word.upper() if word == 'a' else word for word in lower_String ])