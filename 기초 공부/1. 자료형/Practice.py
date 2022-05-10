Q1. 과목별 점수의 평균점수를 구하자.
국어 : 80
영어 : 75
수학 : 55

A1.
국어 = 80
영어 = 75
수학 = 55

A = 국어+영어+수학
print(A/3)

Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.

A2.
홀수 : 2로 나눌 시 나머지가 1
짝수 : 2로 나눌 시 나머지가 0

a = 13
print(a%2)

Q3. 홍길동의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 다양하게 출력하라
pin = "881120-1068234"
yyyymmdd = 
num =
print() # 연월일 부분출력
print() # 숫자 부분 출력

A3.
yyyymmdd =
문자열 슬라이싱
pin = "881120-1068234"
print(pin[0:6])

num =
pin = "881120-1068234"
print(pin[7:0])

Q4. pin = "881120-1068234" 성별을 나타내는 숫자 출력

A4. print(pin[7])

Q5. replace를 사용하여 a 를 # a#b#c#d 으로 바꾸어라
a = "a:b:c:d" 
b = 

A5. a = "a:b:c:d" 
print(a.replace(":","#"))

Q6. [1,3,4,5,2,] 리스트를 [5,4,3,2,1]로 만들어보자

A6. 
1. sort로 정렬
2. reverse로 뒤집기

a = [1,3,4,5,2]
a.sort()
a.reverse()
print(a)

Q7. ['Life', 'is', 'too', 'short']리스트를 Life is too short 문자열로 출력해보자
a = ['Life', 'is', 'too', 'short']
result =
print(result)

A7. 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)