함수(Function) : input이 어떠한 Function을 통하여 output으로 나오는 것
# 프로그래밍에서는 입출력이 존재하지 않을 수 있거나 둘 중 하나만 존재할 수도 있음

Python의 함수의 구조
def 함수면(매개변수 - input):
    <수행할 문장1> #
    <수행할 문장2> # - function
    ... #
    return (리턴 값- output)

def sum(a, b):
    result = a + b
    return result # = 정의
print(sum(1,2)) : 함수의 호출

1. 입력값이 없는 함수 / 출력값만 존재
def say():
    return 'Hi'

print(say())

2. 출력값이 없는 함수 / 입력값만 존재
def sum(a, b):
    print("%d, %dd의 합은 %d입니다." % (a, b, a+b))
print(sum(1,2))

1, 2의 합은 3입니다.
None # return 값이 존재하지 않아 none으로 출력

myList = [1,2,3]
print(myList.append(4)) # = none / append는 출력이 없는 함수이다.
# append는 기능으로 4를 추가했지만 return 값은 없다.

myList = [1,2,3]
print(myList.pop()) # = 3 / pop은 출력이 있는 함수이다.
# pop은 마지막 list 값을 뽑아서 출력해준다 - return 값이 있는 함수이다.

3. 입출력이 모두 없는 함수

def say():
    print('Hi')
print(say())

Hi
none # return이 없음

4. 여러개의 입력값을 갖는 함수

1.
def sum_many(*args): # *args(or 원하는 이름) : 몇개든 상관없이 전부 가능하다 // 한번에다 관리할 수 있음
    sum = 0
    for i in args :
        sum = sum + 1                                                                                                                         
    return sum
print(sum_many(1,2,3))

2. def print_kwargs(**kwargs) # **() : keysword argument // dictinonary의 형태
    for k in kwargs.keys():    
        if(k == "name"):
            print("당신의 이름은" + k)
print(print_kwargs(a="1", b="2"))


2. def print_kwargs(**kwargs) # **() : keysword argument // dictinonary의 형태
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은" + kwargs[k])
print(print_kwargs(name="int 조수", b="2"))

= name이라는 변수만 받아서 key 중 name이라는 것이 있으면 출력하겠다.and
# 특정요소가 있을 때 그것만 출력하겠다로 사용

5. 함수의 결과값은 언제나 하나이다
def su_and_mul(a,b)
    return a+b, a*b

print(sum_and_mul(1,2)[index로 특정값만 사용 가능]) # = (3, 2) 튜플로 묶여서 나온다 / return 값은 하나 이기 때문에

6. 매개 변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): # True로 고정해버린 후 마지막 출력에 man에관한 입력을 안넣어도 자동으로 True
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d살 입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
say_myself("용찬", 26) # 정상적으로 man=True로 출력됨
say_myself("용찬", 26, False) # 기본값이 True여도 False를 넣으면 값이 바뀜

def say_myself(name, man=True, old): # 기본값은 맨 뒤에 써주자 / 중간에 있을 시 출력할때 오류발생 가능성 높음

7. 함수 안에서 선언된 변수의 효력 범위
1번 방법
a = 1
def vartest(a)
    a = a + 1 # 함수속 선언된 변수는 지역변수로 임시변수이다 함수 밖의 변수에 영향미치기가 힘들다
# return을 해주지 않았기 때문에 a = 2라고 해서 2가 출력되지 않는다 / 계산만 마무리한 것
    return a # output이 존재하기 때문에 a = 2로 할당 및 출력됨    
vartest(a) 
print(a) # a = 1 출력

2번 방법
a = 1
def vartest():
    global a # 전역변수로 바깥(전체)에서도 영향을 주는 변수로 선언
    a = a + 1

vartest()
prtin(a)

8. Lambda 함수 # 함수 이름, 변수, 리턴을 정하지 않고 축약모드로 간단하게 쓸 수 있는 함수
add = lambda a, b: a+b
print(add(1,2))

List 내에서도 사용가능 # 원래 함수는 List내에서 사용이 불가능하다
myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](1,2))  # 함수를 불러와서 인수 1,2를 a,b에 넣는다