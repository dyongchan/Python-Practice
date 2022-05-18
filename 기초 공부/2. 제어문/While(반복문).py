While (반복문) # 특정 구조 및 구문을 반복적으로 실행 시킬 때 사용하는 문구

While 기본구조
while <조건문>: # bool 자료형 도출 
    <수행할 문장1>
    <수행할 문장2>
    ... # while이 True 일 경우 while 문장 속 코드는 계속 실행 - False가 될 때 까지

실습1

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무르,ㄹ %d번 찍었습니다." % treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다.")
        

실습2

coffee = 10
money = 300
while money: # True
  print("돈을 받았으니 커피를 줍니다.")
  coffee = coffee = 1
  print("남은 커피의 양은 %d개 입니다."% cofee)
  if not coffee: # False
    print("컾;가 다 떨어져습니다. 판매를 중지합니다")
    break # 반복문의 구문을 빠져나간다.


실습3

a = 0
while a < 10:
    a = a + 1
    if a %2 == 0: # 짝수인지 확인하는 코드
        continue
    print(a)


무한루프 # 무한정 실행되는 루프
while True:
  print("안녕하세요")