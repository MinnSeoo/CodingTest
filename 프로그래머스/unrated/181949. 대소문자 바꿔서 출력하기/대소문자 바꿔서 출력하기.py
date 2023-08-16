str = input()
List = list(str)    # str을 문자열 list로 변환하여 저장
changed = []

for char in List:     # List에 있는 각각의 문자를 순회한다. 이때 char 변수에 현재 순회 중인 문자가 할당됨.
    if char.islower():    # char 변수에 할당된 문자가 소문자 일 경우 / '()' 문자열 메소드 이므로 괄호 사용
        changed.append(char.upper())    # char 변수에 할당된 문자를 대문자로 변경후 changed list에 추가.
    elif char.isupper():    # char 변수에 할당된 문자가 대문자 일 경우 / '()' 문자열 메소드 이므로 괄호 사용
        changed.append(char.lower())    # char 변수에 할당된 문자를 소문자로 변경후 changed list에 추가

result = ''.join(changed)   # 리스트의 문자들을 하나의 문자열로 합침
print(result)

        
    