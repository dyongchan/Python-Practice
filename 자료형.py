# 자료형 - 숫자형

from re import L


a = 1 # int : 정수형
b = 2.4 # float : 실수형
c = 23e10 # float : 실수형 지수 표현
d = 0o37 # 8진수
e = 0x7A # 16진수

print(type(a), type(b), type(c), type(d), type(e))

'''
숫자형의 사칙연산
+,-,*,/ 이외
// : 나머지
% : 몫
** : 제곱 
'''

# 자료형 - 문자형 (' , ", \', \" 이용) syntax error에 유의
h = "Python codes"
print(type(h)) # 문자열 : string(str)

# escape codes
# \n : 줄 바꾸기, \t : 탭 간격 주기
# \', \\, \" : \ 이후의 것 삽입  
"Python is simple, so you can need Python"
'Python is simple, so you can need Python'
'"Python is so easy", he says.'
"\"Python is so easy\", he says."
'Python\'s codes are so fun'
'Python is simple, \nso you can need Python'
"""Python is simple, so you can need Python""" # """ or ''' : escape code 없이 원하는대로 출력가능

'''
문자열 연산 : 문자열끼리 더하거나 여러번 표시가능
ex)
print("=" * 50)
print("my codes" * 50)
print("=" * 50)
'''

# 문자열 길이 구하기 함수 : len()
'''
a = "Python is easy"
len(a)
'''

# 파이썬은 0부터 숫자를 센다
# 문자열의 인덱싱과 슬라이싱
a = "Language"
a[0] = L, a[3] = g, a[-1] : g, a[-3] : u # indexing 
a[(이상):(미만):(간격)] # slicing

# 문자열 포매팅

