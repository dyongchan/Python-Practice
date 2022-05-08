
자료형 - 숫자형

a = 1 # int : 정수형
b = 2.4 # float : 실수형
c = 23e10 # float : 실수형 지수 표현
d = 0o37 # 8진수
e = 0x7A # 16진수

print(type(a), type(b), type(c), type(d), type(e))

'''
숫자형의 사칙연산
+,-,*,/ 이외
// : 나머지
% : 몫
** : 제곱 
'''

자료형 - 문자형 (' , ", \', \" 이용) syntax error에 유의
h = "Python codes"
print(type(h)) # 문자열 : string(str)

escape codes
# \n : 줄 바꾸기, \t : 탭 간격 주기
# \', \\, \" : \ 이후의 것 삽입  
"Python is simple, so you can need Python"
'Python is simple, so you can need Python'
'"Python is so easy", he says.'
"\"Python is so easy\", he says."
'Python\'s codes are so fun'
'Python is simple, \nso you can need Python'
"""Python is simple, so you can need Python""" # """ or ''' : escape code 없이 원하는대로 출력가능

'''
문자열 연산 : 문자열끼리 더하거나 여러번 표시가능
ex)
print("=" * 50)
print("my codes" * 50)
print("=" * 50)
'''

1. 문자열 길이 구하기 함수 : len()
'''
a = "Python is easy"
len(a)
'''

# 파이썬은 0부터 숫자를 센다
# 문자열의 인덱싱과 슬라이싱
a = "Language"
a[0] = L, a[3] = g, a[-1] : g, a[-3] : u # indexing 
a[(이상):(미만):(간격)] # slicing

2. 문자열 포매팅
'''
문자열 포맷 코드
%s : 문자열(str) - 어떤 형태든 대입가능
%c : 문자 1개
%d : 정수(integer)
%f : 부동소수(float)
%o : 8진수
%x : 16진수
%% : literal %
'''
number = 14
day = "Three"
"I ate %s apples. so I was sick for %s days." % (number, day) # 여러 변수 대입가능

"Error is %d%%" % 98 # %%으로 % 표현

a ="aasdf asdasfasd asdwad {} asdwasd".format("안녕") # {} 에 삽입됨
a =-"aasdf {age} asdasfasd asdwad {name} asdwasd".format(name = "안녕", age = "14") # 변수에 맞게 대입가능
name = "int"
a = f"나의 이름은 {name} 입니다" # f만 첫글자로 작성해도 format 기능 사용가능

3. 정렬과 공백

# :< 왼쪽정렬 / :> 오른쪽정렬 / :^ 가운데정렬
f'{"hi":<10(문자열 자릿수)}'
a = "{0:>10}".format("hi")
# 공백채우기
a = "{0:(지정해서넣을문자)>10}".format("hi") # ex) a = "{0:!>10}".format("hi") = !!!!!!!!hi
a = f'{"hi":=^10}' # = ====hi====

a = "10s or -10s" % "hi" # 앞 또는 뒤로 10칸 띄우고 출력
a = "0(간격).5(소수점 남기는 자리 수)5" % 3.124254 # = 3.12425


# 문자열 관련 함수

문자 개수 세기(count)

a = "hobby"
a.count('b') # b의 개수 세기

print(a.find('b')) # find : b가 가장 먼저 나오는 인덱스 리턴 (있으면 리턴, 없으면 -1 출력)

",".join('abcd') # join : 각 문자열 사이에 대입 a,b,c,d
a = ",".join(["a","b","c"]) # = a,b,c

# upper : 대문자로 바꾸기 / lower : 소문자로 바꾸기 / (ls or rs or x)strip : (왼쪽, 오른쪽 양쪽) 공백지우기
# a.replace("___", "___") a의 문자 중 일부를 교체한다
# a.split() : 문자열 자료형을 띄어씌기 기준으로 잘라서 리스트로 만들어주는 함수

자료형 - 리스트 : 변수 여러 개를 묶는 역할

a = ["조(0)","용(1)","찬(2)"] # 리스트 속 리스트 넣어서 리스트 자체 출력 가능 : print(a[3][1]) 3번째 속 1번째
print(a[1]) # = 용

1. 인덱싱
a = [1,2,3] / print(a[0]) # = 1

2. 슬라이싱
a = [1,2,3,4] print(a[0:2:1]) # = [1,2,3]

3. 사칙연산 가능 

4. 리스트 수정 및 교체
a = ["조","용","찬","굿"]
a[1] = ["영"] # ["조","영","찬","굿"]
a[0:2] = ["주","양"] # = ["주","양","찬","굿"] / a[] = ["굿"]
# del 함수 : del a[0] = ["영","찬","굿"]

5. append 함수 (리스트 맨뒤에 추가)
a = ["조","용","찬","굿"]
a.append("짱") # a = ["조","용","찬","굿","짱"] 

6. sort 함수 (정렬) 문자 = 가나다 or 알파벳 순 / 숫자 = 크기 순
a = [1,5,3]
a.sort() # a = [1,3,5]

7. reverse 함수 (뒤집기)
a = [1,5,3]
a.reverse() # a = [3,5,1]

8. index 함수 (위치 반환)
a = [1,5,3]
a.index(3) # = 2

9. insert 함수 (특정위치 값 삽입)
a = [1,5,3]
a.inset(0(몇번째 인덱스),4(값)) # a = [4,1,5,3]

10. remove 함수 (가장 먼저 발견되는 값 제거)
a = [1,5,3]
a.remove(1) # = a = [5,3] / a = [1,5,3,1,1,1] - a = [5,3,1,1,1]

11. pop 함수 (리스트의 마지막 값 추출)
a = [1,5,3]
a.pop() # = a = [1,5]

12. count 함수 (리스트 속 특정 값 개수 세기)
a = [1,5,3,1,1]
a.count(1) # = 3

13. extend 함수 (리스트 확장)
a = [1,5,3]
a.extend([2,3]) # = a = [1,5,3,2,3]

자료형 - 튜플(tuple) 길이 및 값이 고정된 것(변함이 없다) [] 대신 () 사용 
# indexing, slicing, 덧 뺄셈, len(길이)함수 가능 하지만 값은 변함이 없다.

t1 = (1,2,'a','b')
print(t1[0]+1) # = 2

a = (1,2)
a = a * 3 # = a 라는 저장공간에 a라는 튜플을 세번 넣는다

자료형 - 딕셔녀리(Dictoinary) # 단어를 key로해서 어떤 값(value)이 존재하는 자료구조
# 연관 배열(Associative array) 또는 해시(Hash)
# API에 자주 활용된다

dic = {'name' : 'Eric', 'age' : 14}
print(dic['name']) # = Eric

1. 딕셔너리 쌍 추가
a = {1: 'a'}
a['name'] = '익명' # = {1: 'a', 'name' = '익명} # 새로운 키를 할당

2. 딕셔너리 삭제
a = {1: 'a'}
del a[1(key)] # =  삭제됨 / key와 value 만 존재한다. (순서 상관없음)

# 주의사항 : key는 중복되며 안됨 / value는 중복가능

3. key 리스트 만들기(keys)

a = {1: '구름', 2: '하늘', 3: '태양'}
print(a.keys()) # = dict_keys([1, 2, 3])
print(a.values()) # = dict_values(['구름', '하늘', '태양'])
print(a.items()) # = dict_values([(1, '구름'), (2, '하늘'), (3, '태양')])
# items() : 새로울 배열 속 튜플 형태로 key, value 쌍으로 담을 수 있다

for k in a.keys(): # = keys만 뽑아서 배열처럼 반복문을 돌려서 쓰게 됨
for v in a.values(): # = values만 뽑아서 배열처럼 반복문을 돌려서 쓰게 됨
for k, v in a.items():
    print("키는: " + str(k))
    print("벨류는: " + v)

4. 추가적 딕셔너리 함수
a.clear(): # key 및 value 모두 지우기

a.get('key') # keyd에 대한 value 값 얻기
a = {1: '구름', 2: '하늘', 3: '태양'}
print(a[4]) : key errer 도출 / print(a.get(4)) : none 도출 # 없는 값 나태내기 가능 
print(a.get(4,'없음')) # = '없음' 리턴 / 해당되는 key값이 없다면 '없음'을 리턴해라 라는 뜻

print(4 in a) # a라는 dic에 4라는 키가 존재하는가 = false 리턴 (true or false)