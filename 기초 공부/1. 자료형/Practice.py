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
print(pin[:6])

num =
pin = "881120-1068234"
print(pin[7:])

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

Q8.(1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해보자
A8.

a = (1,2,3)
a = a + (4,)
print(a) 

Q9. a = dic()
print(a) # {}

A9.
오류가 발생하는 코드는? 3번 
1. a['name'] = 'python'
2. a[('a',)] = 'python'
3. a[[1]] = 'python'
4. [250] = 'python'
# dictionary의 key 값으로는 변하는 값을 사용할 수 없다. ex) list 

Q10. dictionary a에서ㅏ 'B' 에 해당하는 값을 추출해 보자
a = {'A':90, 'B':80, 'C':70}
result =
print(a) # {'A':90, 'C':70} 출력
print(result) # 80 출력

A10. 2가지 방법 존재 (a의 일반적인 Value 출력)
1. a['B'] 출력
print(a['B'])

2.a.get 활용
print(a.get('B'))

- 문제풀이 : pop 함수 사용
result = a.pop(1) : X # dict는 key와 value로 구성되어 있다.
result = a.pop('B') # Key값만 빼오기

Q11. a 리스트에서 중복 숫자를 제거해보자
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a[:])
b = list(set(aSet))
print(b)

A11.
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a[:])
b = list(set(aSet))
print(b)


Q12. 파이썬 변수의 특징
a = b = [1,2,3]
a[1] = 4
print(b)

A12.
a = b = [1,2,3] # [1,2,3] 이라는 객체의 주소를 똑같이 a,b에 넣어준다
a[1] = 4 # 객체의 첫번째 인덱스의 변화 = 주소는 같지만 값은 변했다 [1,4,3]
print(b) # 주소값이 같으므로 출력 : [1,4,3]