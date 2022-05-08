사용자 입력과 출력

1. input의 사용
a = input() # 내장함수 : 미리 정의되어있는 함수, command창에서 a 값을 넣어줄 수 있음

number = input("숫자를 입력하세요:")
print(number) # command창에서 유저의 input을 넣을 수 있음

2. print의 사용
print("life" "is" "too short") # 자동으로 인수들을 더해준다 / ,를 추가 시 띄어쓰기가 된다
# lifeistoo short 출력 / , 추가 시 life is too short

for i in range(10):
    print (i, enn=' ') # 띄어쓰지 않고 한줄에 출력하며 사이사이에 ' '를 추가함

파일 읽고 쓰기

쓰기모드
f = open("새파일.txt", 'w') # 현재 같은경로에 파일 생성 / 상대주소
f.close()

'''
파일열기모드
1. r : 읽기모드 - 파일을 읽기만 할 때 사용
2. w : 쓰기모드 - 파일에 내용을 쓸 때 사용
3. a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
'''

f = open("C:/Python/새파일.txt", 'w', encoding="UTF-8") # 처음부터 주소를 써주는 절대주소
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# encoding="UTF-8" : 전체 캐릭터에 대한 자료형 느낌, 사용자가 작성한 문자 및 기호들을 깨지지 않게 출력해줌(한글)

읽기모드

1. readline 함수 # 파일의 한줄 씩 읽어오는 함수
한줄 읽어오기
f = open("새파일.txt", 'r', encoding="UTF-8")
line = f.readline()
print(line)
f.close() # open 했으면 항상 close 하기

여러줄 읽어오기
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

# readlines : 파일 속 모든 라인 다 읽어 올 수 있다 list 형태로 가져온다
f = open("새파일.txt", 'r')
lines = f.readlines() # list형태 속 하나씩 뺴서 출력함
for line in lines:
    print(line)
# 위쪽 예시에서 작성한 것은 한줄띄어진 "n번째 줄입니다"가 반복됨
# = print("n번째 줄입니다.\n")을 불러오기 때문에 한줄 씩 더 띄어진다.
# 한줄씩 더 띄어지는걸 방지하기 위해서 1. print(line, end="")을 써주면 됨.
# 한줄씩 더 띄어지는걸 방지하기 위해서 2. print(line.strip("\n"))
# 전체를 한 줄에 나타내는 방법 : print(line.strip("\n"), end=" ")
f.close

2. read 함수 # 모든걸 읽어서 통채로 가져온다
f = open("새파일.txt", 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close

추가모드 # add의 의미
f = open("새파일.txt", 'a', encoding="UTF-8") # 출력되는 값을 그대로 둔 채 뒤로 추가하는 모드
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close

with 문 # close 안해도 됨 / 간단하게 사용
with open("foo.txt", "w") as f: # 쓰기모드로 파일을 열어서 f라는 변수에 저장한다
# 지역변수 개념 적용 with 문 끝 시 f는 close
    f.write("Life is too short, you need python")

변하는 자료형(Immutable) vs 변하지 않는 자료형(Mutable)
Immutable : 정수, 실수, 문자열 ,튜플
Mutable : 리스트, 딕셔너리, 집합

# Immutable
a = 1
def vartest(a):
    a = a + 1 # 지역변수
vartest(a)
print(a) # a = 1 출력 (리턴값 존재 하지않음)

# Mutable
b = [1,2,3] # 전역변수
def vartest2(b):
    b = b.apppend(4) # 지역변수
vartest2(b)
print(b) # b = [1,2,3,4] 출력 / 전역변수와 지역변수로 나뉘어 서로 별개이다.
# 같은 주소값이 들어가서 그대로 사용한다. Mutable이기 때문에 전역변수가 변화가 가능하다