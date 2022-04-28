모듈(module) : 미리 만들어 놓은.py file을 불러와서 사용하는 구조 (함수, 변수, 클래스)
# import : 가져온다 / 같은경로(같은폴더)내에 존재 시 바로 사용가능

1. 함수 가져와서 적용

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b
'''

import mod1
print(mod1.add(1,2)) # 3 출력

2. 여러 함수가 포함 될 시

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b
def aasdasdasd(a,b):
    return a + b
'''

from mod1 import add # mod1.py 속 add의 함수만 사용
print(add(1,2)) # 3 출력

3. print가 포함된 mod1.py import

다른 파일 속 함수
'''
# mod1.py
def add(a,b):
    return a + b

def sub(a,b):
    retirn a - b
'''
if __name__ == "__main__" 
# name = 가져올 함수가 존재하는 파일
# main = 함수가 실행될 현재 파일의 이름
    print(add(1,4))
    print(add(4,2))
# name과 main과 일치할 때 만 print를 실행하라는 조건문

4. 경로가 다를 시(ex-불러오는 파일이 다른 폴더에 있는경우) 사용하는 명령어
sys.path.append("경로")

ex)
import sys
sys.path.append("C:\\jocoding\\subFolder") # 경로를 작성해야 다른 경로 속 파일 가져오기 가능
import mod1
print*mod1.add(3,4)

패키지(package) : 