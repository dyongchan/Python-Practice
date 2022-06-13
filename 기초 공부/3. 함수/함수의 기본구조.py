from unittest import result


def sun(a, b): # 함수의 정의
  result = a + b
  return result 

# 함수의 사용  = 호출
print(sum(1,2)) #  = 3

입력값이 없는 함수
def say():
  return 'Hi'
print(say()) # Hi

MyList = [1,2,3]
print(MyList.pop())
# 3 / 입력값이 없지만 리턴은 가능

출력값이 없는 함수
def sum(a, b):
  print("%d, %d의 합은 %d입니다.") % (a, b, a+b)
print(sum(1,2)) 

''' 
1, 2의 합은 3 입니다.
none 
'''

MyList = [1,2,3]
print(MyList.append(4))
# none / list에 값만 추가하는 기능만 존재 리턴값이 없음

입출력이 모두 없는 함수
def say():
  print('Hi')
print(say())
# none