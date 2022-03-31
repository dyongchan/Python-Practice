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

# class로 만들어서 함수를 여러개의 instance로 찍어낸다
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
# a가 add , sedata라는 함수를 포함하고 있음 (class로 찍어낸 걸 a에 삽입)

4. class - 생성자 # 관례적으로 맨 앞에 사용함
class Fourcal:
    def __init__(self, first, second): # __init__ : (처음시작하다) - 예약어 /  class를 찍어낼 때 무조건 처음으로 시행하는 함수
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
        result = self.first + self.second
        return result
    
a = Fourcal() # __init__으로 first 및 second를 정의 해주어야 함수 실행 가능 / ex) a = Fourcal(1,2)

5. class - 상속 # 찍어낸 class에 기능을 추가 및 파생하여 다른 class를 생성할 수 있음
class Fourcal:
    def __init__(self, first, second): # __init__ : (처음시작하다) - 예약어 /  class를 찍어낼 때 무조건 처음으로 시행하는 함수
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
        result = self.first + self.second
        return result 
# 상위 class (부모)를 활용

class MoreFourCal(FourCal): # 괄호안에 상위 class의 이름을 넣어줌으로 상속받는 (자식) class 생성
    pass
# 기능 똑같이 사용가능
a = MoreFourCal(4, 2)
print(a.add()) # = 6

6. class - 상속 (메서드추가)
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
        result = self.first + self.second
        return result 
class MoreFourCal(FourCal):
    def pow(self)
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
print(a.pow())

7. class - 상속 (메서드 오버라이딩) # 상위 class의 변수를 덮어 쓴다
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
        result = self.first + self.second
        return result 
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result  = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
calss SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/ self.second # 부모, 자식의 메서드가 겹칠때 - 자식의 메서드가 우선 + 부모의 class 변형가능
        
8. class 변수, 객체 변수
class Fourcal:
    first = 2 # 클래스변수 class에 미리선언해놓은 변수
    second = 3 # 클래스변수
    def __init__(self, first, second): # 객체변수
        self.first = first
        self.second = second
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self)
            result = self.first + self.second
        return result

a = FourCal()
print(a.first) # = 2 class의 변수로 미리 선언되었기 때문
b = FourCal()
print(b.first # = 2 class의 변수로 미리 선언되었기 때문
      
class Family:
      lastname : "김" # class 변수
      
Famil.lastname = : "박" # 설계도 자체를 호출해서 설계도 자체를 수정한다
primt(Family.lastname)
      
a = Family()
b = family()
print(a.lastname)
print(a.lastname)
