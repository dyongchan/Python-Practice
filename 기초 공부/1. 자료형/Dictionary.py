딕셔너리(dictionary) # 단어를 key로 해서 특정 값이 있는 자료구조
- 연관배열(Associative array) 또는 해시(Hash)
- key를 통해 value 를 얻는다.

기본구조
dic = {'name':'용찬', 'today':'tuesday'}
print(dic['today'])

- 새로운 key 할당
a = {1:'a'}
a['name'] = "익명" # [1:'a', 'name': '익명']

- 요소 삭제
# 순서가 없기 때문에 key를 입력해야함
del a[key]

- key의 중복에 주의
a = {1: "a", 1: 'b'}
prin(a) # 마지막 key 및 value 출력

- key list 만들기 (.keys)
a = {1:'조용찬', 2:'찬용조', 3:'용찬조'}
print(a.keys()) # dict_keys([1,2,3])

- value list 만들기(.values)
print(a.values()) # dict_values(['조용찬','찬용조','용찬조'])

- 각각의 key, value 들을 새로운 튜플에 쌍으로 담기(.items)
print(a.items()) # dict_items([(1,'조용찬'),(2,'찬용조') ,(3,'용찬조')])

# 반복문에서의 이용
a = {1:'조용찬', 2:'찬용조', 3:'용찬조'}
# print(a.keys())
# print(a.values())
# print(a.items())
for k in a.keys(): / a.values() / a.items()
    print(k)
'''
1
2
3
'''

활용 예시)
for k,v in a.items():
  print("키는: " + str(k))
  print("밸류는: " + v)

- 딕셔너리 비우기
a = {1:'조용찬', 2:'찬용조', 3:'용찬조'}
a.clear() #  {}

- key를 통해 value 얻기 (.get)
# 없는값을 출력할 때 사용하기 좋음
a = {1:'조용찬', 2:'찬용조', 3:'용찬조'}
print(a[4]) # none / 대괄호만 사용시 keyerror 출력

get의 활용 : print(a.get(4,'없음')) # 4라는 key가 없을 시 '없음' 출력

- key값이 존재하는지 찾기(in)
a = {1:'조용찬', 2:'찬용조', 3:'용찬조'}
primt(k in a) # True or False 출력 