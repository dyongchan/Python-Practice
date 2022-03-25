
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
