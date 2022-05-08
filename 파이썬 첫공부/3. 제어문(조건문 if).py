제어문 - if # 조건에 맞는 상황을 수행하는데 사용 / 들여쓰기가 매우 중요하다.

money = True
if money: # True 시 바로 아래 줄 실행
    print("택시를 타고 가라")
else: # False 시 바로 아래 줄 실행
    print("걸어 가라")


1. if 문에서 자주 사용되는 비교연산자 # 결국 True or False를 만드는 것!
x < y : x가 y보다 작다
x > y : x가 y보다 크다
x == y : x와 y가 같다
x != y : x와 y가 같지 않다
x >= y : x가 y보다 크거나 같다
x <= y : x가 y보다 작거나 같다

a = 1
b = 2
if a < b: # True이므로 if 바로 아래 문장 출력
    print("택시를 타고 가라")
else: 
    print("걸어 가라")
# = True : "택시를 타고 가라"


money = 2000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어라가")
# = False : "걸어라가"

2. if 문의 and, or, not

or(|) :
1. True or False 둘 중 하나라도 True 면 True
2. False or Fasle : False가 됨
money = 2000
card = 1 # 1 = 참 / 0 = 거짓
if money >= 3000(False) or card(True):
    print("택시를 타고가라")
else:
    print("걸어라가")
# = True : "택시를 타고 가라" - False or True 

and(&) :
1. True and True 둘다 True여야 True가 됨
2. 둘중 하나라도 False 가 있다면 False

not
if not False: # False를 True로 변경
if not True: # True를 False로 변경


3. x in s / x not in s : # in / not in 기호는 따로 없음
money = 2000
card = 1
if 1 in [1,2,3,]: # in 왼쪽 값이 in 오른쪽에 있는가 / not in은 반대로 해석
    print("택시를 타고가라")
else:
    print("걸어라가")


4. if문 특정 값 입력안할 때
money = 2000
card = 1 
if 1 in [1,2,3,]:
    pass
else:
    print("걸어라가")


5. 다양한 조건의 제시 # else if = elif
pocket = ['paper', 'cellphone]
card = False
a = True
if 'money' in pocket:
    pass
elif card:
    print("택시를 타고가라")
elif a:
    print("aa")
else:
    print("걸어기라")
# = 'aa' 한줄 씩 처리 후 True가 나오면 출력 

6. 조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "faliure"의 표현식을 간단하게 표현하면,
# 3항 연산자
message = "success" if score >= 60 else "failure" : # if문을 간단하게 쓰는법
print(message)