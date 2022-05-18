집합(set) : 집합에 관련된 요소의 처리를 위해 사용 # 파이썬에서만 존재
- 중복된 요소를 가질 수 없다.
- 순서가 존재하지 않는다.

- 집합의 정의
1. set() 으로 list 감싸기
s1 = set([1,2,3])
print(s1)

2. 중괄호
s1 = {1,2,3}
print(s1)

예시)
- 리스트 중복제거
l = [1,2,2,3,4]
newlist = list(set(1))
print(newlist)

- 문자열 집합
s1 = set("Hello")
print(s1) # {"e", "l", "H", "o"}
# 순서가 없으며 중복이 없다

- 교집합(.intersection)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) # 공통적으로 있는 것 출력 / {4,5,6}
print(s1.intersection(s2))

- 합집합(.union)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 | s2) # 모든 원소 중복제거 후 출력 / {1,2,3,4,5,6,7,8,9}
print(s1.union(s2))

- 차집합(.difference)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 - s2) # 공통적으로 속한 부분 제거 / {1,2,3}
print(s1.difference(s2))

- 값 1개 추가하기(.add)
s1 = set([1,2,3,4,5,6])
s1.add(7) # {1,2,3,4,5,6,7}

- 값 여러개 추가하기(.update)
s1 = set([1,2,3,4,5,6])
s1.update([7,8,9]) # {1,2,3,4,5,6,7,8,9}

- 특정 값 제거하기
s1 = set([1,2,3,4,5,6])
s1.remove(1) # {2,3,4,5,6}