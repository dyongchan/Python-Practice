조건문 : if # 특정 조건에 대한 참, 거짓으로 판명하는 문장
- 비교연산자를 비롯한 다양한 연산자의 사용 및 bool 자료형이 많이 사용된다.

실습1 - 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True
if money: # money가 True면 바로 아래있는 절 실행
  print("택시를 타고 가라")
else: # False면 아래 문장 실행
  print("걸어 가라")

- 들여쓰기 오류 주의!

실습2
money = True
if money: 
  print("택시를 타고 가라")
print("aa") # invalid syntax error 발생 (들여쓰기 중요!)
else:
  print("걸어 가라")

- 조건식의 불자료형 및 비교연산자

''' 비교연산자 정리
x < y : x가 y보다 작다
x > y : x가 y보다 크다
x == y : x와 y가 같다
x != y : x와 y가 같지 않다
x >= y : x가 y보다 크거나 같다
x <= y : x가 y보다 작거나같다.
'''

실습1
a = 1
b = 2
if a < b: #  비교연산자 바꿔가면 출력해보기
  print("택시를 타고 가라")
else:
  print("걸어가라")

실습2
만약 3000원 이상의 돈을 가지고 있으면 택시틑 타고 그렇지 않으면 걸어 가라
money = 3000
if money >= 3000:
  print("택시를 타고 가라")
else:
  print("걸어가라")

''' and, or, not
x or( | }y : x와 y 둘중에 하나만 참이면 참
x and(&) y : x와 y 모두 참이어야 참
not x : x가 거짓이면 참 # True는 False로 / False 는 True로 바뀜
'''

실습1
money = 2000
card = 1 # (Ture : not 0)
if money >= 3000 or card: # money가 False지만 card가 존재하기 때문에 참 (or)
  print("택시를 타고가라")
else:
  print("걸어가라") # "택시를 타고가라"

실습2
money = 4000 # True
card = 1 # True
if money >= 3000 and card: # 두가지 조건 모두 True이므로 참 (and)
  print("택시를 타고가라")
else:
  print("걸어가라") # "택시를 타고가라"

'''
x in s : (찾는 값) in (리스트,튜플.. 여러 값을 포함하는 구조)
x not in s : (찾는 값) in (찾는값 없는가)
'''

실습 
if 1 in [1,2,3]:
  print("택시를 타고가라")
else:
  print("걸어가라")  # "택시를 타고가라"

- 조건문에서 아무런 일이 나오지 않게 만들 때
if 1 in [1,2,3]:
  pass # (지나가라)
else:
  print("걸어가라") # 결과값 아무것도 안나옴

- 다중 조건 판단 elif # 여러개의 elif를 통하여 다중 조건 추가 가능
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocekt:
  pass
elif card:
  print("택시를 타고가라")
else:
  print("걸어가라")

- 조건부 표현식
1. 기존 코드
score = 70
if scroe >= 60:
  message = "success"
else:
  message = "failure"
print(message)

2. 간결한 조건부 표현식 # 성공일때의 조건식을 먼저 쓴 후 다음 조건식 작성
message = "success" if scroe >=60 else "failure"
print(message)