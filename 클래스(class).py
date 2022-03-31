클래스(class) : 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
# python 프로그래밍의 핵심이 됨

클래스(class)의 필요성

1. 하나의 계산 시 (class 없이 가능)
result  = 0
def add(num):
    global result # 전역변수로 지정
    result += num
    return result

print(add(3))
print(add(4))

2. 각각 다른 여런 계산 시 (class 사용)
result1  = 0
result2  = 0

def add1(num):
    global result1 # 전역변수로 지정
    result1 += num
    return result1

def add2(num):
    global result2 # 전역변수로 지정
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# class로 만들어서 함수를 여러개의 instace로 찍어낸다
클래스 쓰는 법
1. Class 입력
2. 대문자로 시작하는 클래스의 이름 작성
3. 안에 들아갈 함수와 변수 설정

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

1. class 의 작동 구조
class FourCal:
    pass

a = FourCal() # a라는 변수에 class로 만들어낸 객체(설계도)를 넣는다
print(a)
print(type(a)) # class로 만든 instance

2. class의 예시 1
class Fourcal:
    def setdata(self, first, second): # class 속 함수: 메서드
        self.first = first # a의 first라는 변수에 정한 first의 값 1을 넣는다
        self.second = second # a의 second라는 변수에 정한 second의 값 2를 넣는다

a = FourCal() # a라는 변수에 class로 만들어낸 객체(설계도)를 넣는다
a.setdata(1,2) # a 에 있는 함수를 사용하겠다
# a.setdat(1,2) 중 a = self / 1 = first / 2 = second 로 할당 됨
print(a.first)
print(a.second)

3. class의 예시 2
class Fourcal:
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
        result = self.first + self.second
        return result

a = FourCal()
a. setdata(4, 2)
print(a.add())