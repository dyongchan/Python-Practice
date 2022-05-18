for (반복문) # 특정 구조 및 구문을 반복적으로 실행 시킬 때 사용하는 문구

for문의 기본 구조
for 변수 in 리스트(또는 튜플, 문자열): # 변수 = 하나씩 꺼낸 값
    수행할 문장1
    수행할 문장2
    ... 

다양한 사용 - tuple 출력
ㅁ


실습1

test_list = ['one', 'two', 'three']
for i in test_list
    print(i)

실습2 # for 문의 활용\

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first, last)
  
(a,b) = (1,2)


실습3

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    nuimber = number + 1
    if nmark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)


실습4

marks = [90,25,67,45,80]
number = 0
for mark in marks:
    nuimber = number + 1
    if nmark  <  60: continue 
    # continue 기준 아래쪽 코드느 실행되지않고 처음으로 돌아간다.
        print("%d번 학생 축하합니다. " % number)


실습5 range
sum = 0
for i in range(1,12): # (이상, 미만)
    .sum = sum + i
  print(sum)

