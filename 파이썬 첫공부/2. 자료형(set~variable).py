
자료형 - 집합(set) # 집합에 관련된 값을 처리하기 위한 자료형
# 중복 허용하지 않는다. 순서가 없다(Unordered)
# 데이터 관련하여 많이 다룬다

s1 = set([1,2,3]) # = {1, 2, 3}
s1 = {1, 2, 3} # = {1, 2, 3}

활용예시
1.
1 = [1, 2, 2, 3, 4]
newlist = list(set(1)) # = 중복제거 및 리스트 재생성 / [1, 2, 3, 4]

s2 = set("hello") # = {'e', 'l', 'h', 'o'} 중복 및 순서가 없다

2.
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

1. 교집합 (&, .intersection) # 공통적인 값 리턴
print(s1 & s2) / print(s1.intersection(s2)) # = {4, 5, 6}

2. 합집합 (|, .Union)
print(s1 | s2) / print(s1.Union(s2)) # = {1, 2, 3, 4, 5, 6, 7, 8, 9}

3. 차집합 (-, .difference)
print(s1 - s2) / print(s1.difference(s2)) # = {1, 2, 3,}

4. 값 1개 추가하기 - add
s1.add(7) / print(s1) # = {1, 2, 3, 4, 5, 6, 7}

5. 값 여러개 추가하기 - update
s1.update([7,8,9]) / print(s1) # = {1, 2, 3, 4, 5, 6, 7, 8, 9} 

6. 특정  값 1개 제거하기 - remove
s1.remove(1) / print(s1) # =  {2, 3, 4, 5, 6} 

자료형 - 불(bool) # True or False로 사용하는 자료형 / 제어문에서 사용
bool 자료형의 특징
문자열(str)이 어떤 값이 존재한다 : True로 취급
문자열(str)이 어떤 값이 없다 (" ") : False로 취급

list 어떤 값이 존재한다 : True로 취급
list 어떤 값이 없다 : False로 취급

tuple 어떤 값이 존재한다 : True로 취급
tuple 어떤 값이 없다 : False로 취급

dictionary 어떤 값이 존재한다 : True로 취급
dictionary 어떤 값이 없다 : False로 취급

숫자 1 : True로 취급
숫자 0 : False로 취급
None : False로 취급

활용예시
1.
a = "안녕"
if a:
    print(a) # = 안녕 리턴 / if 후 True, False 쓰지 않아도 "값"이 존재하므로 리턴 / 값 없으면 리턴 안됨

2.
a = [1, 2, 3, 4]
while a:
    a.pop()
    print(a) # = 값 존재 - True로 보고 pop 계속 실행 후 list(a)의 값이 사라지면 False로 보고 중단

a = [1, 2, 3, 4]
while True:
    print(a) # =  [1, 2, 3, 4]가 무한정 출력

자료형의 값을 저장하는 공간, 변수(variable)
# 변수는 메모리에 할당된 주소에 있는 값(객체 - 자료형)를 가리킨다
# a = 1 을 살펴보면, a라는 값은 1이 땀긴 주소를 갖고있다

a = 1 / b = "python" / c = [1,2,3] # = : 오른쪽에있는 값을 왼쪽에 넣는다 (변수 생성)

a = [1,2,3] # a라는 변수 상자가 메모리에 생성된 리스트 index 0,1,2에 각각 들어있는 1,2,3 이라는 값의 주소를 갖고있다.

b = a # 객체는 하나이므로 a가 갖고있는 주소를 b에게 넣는다 // a의 값을 넣는것이 아닌 주소를 넣어주는 것(같은 곳을 바라본다)

a = [1,2,3]
b = a[:] # 주소를 넣는 것이 아닌 slicing한 새로운 값을 넣어주므로 새로운 주소 생성


from copy import copy
from os import TMP_MAX
b = copy(a) # 주소를 넣는 것이 아닌 값을 복사하여 새로운 주소를 b에 할당

print(id(a)) = 주소값 확인가능 / pritn( a is b) = a와 b가 같은 곳을 바라보고 있는가 (True or False)

변수를 만드는 여러가지 방법

1. (a, b) or a, b = ('python', 'life') # a, b 에 각각 튜플 자료형을 할당

2. [a, b] = ['python', 'life'] # a, b 에 각각 리스트 자료형을 할당

3. a = b = 'hello' # a, b 에 동시에 할당

4. a, b 의 값을 서로 바꾸고 싶을 때 (다른언어)
a = 3
b = 5
tmp = b # tmp라는 임시변수에 b의 값을 저장
b = a # a값을 b에 덮어 씌운다
a = tmp # 임시로 저장해놓은 tmp를 a에 덮어 씌운다
print(a)
print(b)

5. a, b 의 값을 서로 바꾸고 싶을 때 (python)
a = 3
b = 5
a,b = b,a # 튜플 이용
print(a)
print(b)