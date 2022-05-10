from tkinter import N

- 문자열 자료형 만드는 4가지 방식 (string)

1. " "
2. ' '
3. """  """ # escape code 사용하지 않아도 띄어쓰기, 탭 간격 출력 가능
4. '''  '''

a = 'python's favorite food is perl'

print(type(a)) : syntax error #구문의 오류
# python을 자료형으로 인식 이후 문장은 해석불가
# " " 로 양쪽 끝을 감싸주면 해결 or 반대 or 'python\' 로변경

'''
백슬래시(\)의 사용 (escape code)
\n : 문자열 안에서 줄 바꾸기
\t : 문자열 사이에 탭 간격 주기
\\ : \ 그대로 사용
\' : ' 그대로 사용
\" : " 그대로 사용
'''

- 문자열 더해서 연결하기

a = "python"
b = "is fun"

print(a+b) # python is fun

-문자열 곱하기

a = "python"
print(a * 100) # python 100번 출력

- indexing # python은 0부터 숫자를 셈
a = "Life is too short, You need Python"
print(a[0]) # L
print(a[1]) # i
print(a[-1]) # n

- slicing
= a[이상:미만:간격]

a = "Life is too short, You need Python"
print(a[0:4]) # 'Life'
print(a[:10]) # 'Life is to'
print(a[10:]) # 'o short, You need Python'
print(a[0:10:2]) # 2칸씩 간격을 준다 = 'Lf st'

- 문자열 포매팅
a = "I eat %d apples." % 3
print(a) # I eat 3 apples.

1.
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a) # I eat 3 apples. so I was sick for three days.

'''
문자열 포맷 코드
%s : 문자열(string)
%c :문자 1개(Character)
%d : 정수(integer)
%f : 부동 소수(Floating-point)
%o : 8진수
%x : 16진수
%% : 문자 % 자체
'''

2. 변수에 맞추는 포매팅
a = "asdwasd {age} asdwaf asdw {name} asdwa".format(name="조용찬", age="19")

3.
name = "int"
a = f"나의 이름은 {name} 입니다."

- 정렬과 공백
a = "%10s" % "hi"
# 10칸 띄워지고 출력
# -10 사용 시 왼쪽 정렬

- 소수점 표현
a = "%f" % 3.12414123
# 3.12414123

a = "%0.4f" % 3.12414123  # "(간격).(소수점 남기는 자리수)f

- 문자열 개수 세기(count) # 개수 출력
a = "hobby"
a.count('b') # 2

- 위치 알려주기 (find) # 인덱스 출력 / a.index도 있음
a = "hobby"
a.find('b') # 2 (가장 먼저오는 항목을 알려줌)
a.find('k') # -1 (없으면 -1)

- 문자열 삽입 (join)
a = ",".join("abcd")
# a,b,c,d

a = ",".join(["a","b","c","d"]) # list와 함께 많이 사용
# a,b,c,d

- 소문자를 대문자로 / 대문자를 소문자로 (upper / lower)

- 공백제거
a = "    HI    "
primt(a.strip()) # HI 

- 문자열 바꾸기 (replace)
print(a.replace("life", "leg")) # life 를 leg로 교체한다.

- 문자열 나누기 (split) # 문자열 자료형을 띄어쓰기를 기준으로 잘라서 리스트로 만든다.
+ 
a = "a:b:c:d"
print(a.split(":") # ['a', 'b', 'c', 'd'] # :를 기준으로 자른다.

