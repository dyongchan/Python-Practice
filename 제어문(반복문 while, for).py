from os import makedirs


반복문 - while 문 # while 내부의 코드를 반복적으로 실행
기본구조
while <조건문>:
  <수행할 문장1>
  <수행할 문장2>
  <수행할 문장3> ...

treeHit = 0 # treeHit이 0이다
while treeHit < 10: # treeHit이 10보다 작은동안 + True
    treeHit = treeHit + 1 # treeHit에 1을 더한 값을 넣어준다
    print("나무를 %d번 찍었습니다." % treeHit) # 1 더한 값 넣은 후 출력
    if treeHit == 10: # treeHGit이 10이 되면 + True
        print("나무 넘어갑니다.") # "나무 넘어갑니다." 출력

coffee = 10
money = 300
while money: # money는 True로 고정
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee: # coffee가 not으로 False가되어 if문이 작동하지 않음 / coffee = 0이 되면 0은 false이기 떄문에 not + F = T
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문 빠져나감

a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: # 2로 나눈 나머지가 0 (짝수)
        continue # 아래 문장 실행하지 않고 while의 처음으로 돌아간다
    print(a)

무한루프
while True: #아래문장을 무한히 실행 / Ctrl + c 누르면 멈춤
print("안녕하세요")

반복문 - for 문
기본구조
for 변수 in 리스트(또는 튜플, 문자열): # 구조 속 하나씩 꺼내는 값을 변수에 대입
    수행할 문장1
    수행할 문장2
    ...

test_list = ['one', 'two', 'three'] # 순서대로 하나씩 꺼내서 for 문 속 i에 하나씩 담는다
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last) # 3, 7, 11

marks = [90, 25, 67, 45, 80]
1.
[
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
]

2.
[
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue # for문으로 돌아간다
        print("%d번 학생은 축하합니다. 합격입니다." % number) # continue에 걸리지 않으면 출력
]

for 문 - range 함수 # 이상, 미만으로 뺴낼수 있는 함수

sum = 0
for i in range(1, 11): # 1이상 11 미만 / 1 <= x < 11
    sum = sum + i # 0에서 시작하여 1~10까지 더한다
print(sum)

range 함수를 이용한 구구단 (이중 for 문)

for i in range(2,10):
    for j in range(1,10):
        print(i * j, end=" ") # print함수의 옵션 : end=" " 두번째 인수를 주는 것 / 다음줄로 넘어가지 않고 출력
    print('') # 안쪽 for 문이 모두 실행되어야 바깥쪽 print 실행

for 문 - list comprehensuon (리스트 내포)

result = [num * 3 for num in a] # num은 뒤에나오는 for을 돌린 결과이다 그리고 리스트로 만들어라 (num*3)의 리스트를 만들기

result = []
for num in a:
  result.append(num*3)

조건문추가

result = [num * 3 for num in a if num % 2 == 0] # 넘이 짝수일때만 추가해라

result[]
for num in a:
  if num % 2 == 0:
    result.append(num*3)

result = [x*y for x in range(2,10) for y in range(1,10)] # 구구단 이중 for 문

result = []
for x in range(2,10):
  for y in range(1,10):
    result.append(x*y)