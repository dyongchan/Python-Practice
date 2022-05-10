from xmlrpc.client import Boolean


불(Boolean) : True or False 로 구분하는 자료형
- 제어문에서 많이 사용된다.

if False:
  print(a)

while a==3 / True / False:
  a += 1
  ...

# 자료형의 참과 거짓 / 값이 존재 = 참
"python" - 문자열 = 참 
"" = 거짓
[1,2,3] = 참
[] = 거짓
() = 거짓
{} = 거짓
1 = 참
0 = 거짓
none = 거짓

실습) # 값이 존재 = 참
1.
a = True / "안녕"
if a:
  print(a)

2.
a = [1,2,3,4] # 값이 전부 없어지면 False로 본다.
while a:
  a.pop()
  print(a) # a가 참일때 끝부터 요소를 하나씩 추출한다.
4
3
2
1
while 문 종료 (False)

