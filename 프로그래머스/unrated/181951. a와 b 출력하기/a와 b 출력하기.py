# input, strip, split ->
# input으로 사용자의 입력 받고 문자열으로 반환
# strip으로 문자열 앞뒤 공백 제거
# split 메서드로 입력 문자열을 공백 기준으로 문자열을 나눔. 
# map은 반복가능한 객체를 생성하는 내장 함수이다.
a, b = map(int, input().strip().split(' '))

a = 'a = ' + str(a) + '\n'
b = 'b = ' +  str(b)

print(a+b)