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

여러 개의 입력값
def sum(*args): # 여러개의 인자를 한 번에 받을 수 있다
  sum = 0
  for i in args:
    sum = sum + i
    return sum

def sum_many(a,b): # 인자의 개수가 맞지 않다고 출력
  # *args 사용
    sum = 0
  for i in args:
    sum = sum + i
    return sum_many(1,2,3)