# 컬렉션 자료형
# 리스트
a = []          # 빈 리스트
b = [1, 2, 3]   # 정수로만 이루어진 리스트
c = ['a', 'b', 'c', 'd']    # 문자열 4개로 이루어진 리스트
d = [1, 2, 'a', 'b', True]  # 여러 자료형으로 이루어진 리스트
e = [1, 2, ['a', 'b']]  # 중첩 리스트
print(a)
print(b)
print(c)
print(d)
print(e)

# 리스트 인덱싱
print(b[1])
print(c[3])
print(d[0])
print(e[2])
print(e[2][0])  # 중첩 리스트 안에 있는 값을 출력하고자 할 때
print(e[2][1])
print(e[-1])    # 맨 마지막 요소(값)

f = [1, 2, ['a', 'b', ['안녕', '하세요']]]
print(f[2])
print(f[2][2])
print(f[2][2][0])

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:3])
print(a[:3])    # 처음부터 (0 생략 가능)
print(a[2:])    # 끝까지 (끝번호 생략 가능)

b = [1, 2, 3, ['b', 'c', 'd'], 4, 5]
print(b[2:5])
print(b[3][:2])

# 리스트 연산자
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print('list_a :',list_a)
print('list_b :',list_b)

list_c = list_a + list_b # 하나의 리스트로 합쳐진다(이어진다)
print('list_c :',list_c)

list_d = list_a * 3 # 3번 반복
print('list_d :',list_d)

# 리스트의 요소(값) 추가 : append, insert
list1 = [1, 2, 3]
print('list1:', list1)

list1.append(4) # 맨 뒤에 값 4를 삽입
print('list1:', list1)

list1.append(100)
print('list1:', list1)

list1.insert(1, 50) # 1번 인덱스 자리에 50을 삽입
print('list1:', list1)

# 리스트에 요소(값) 제거 - 인덱스 번호로 삭제 : pop, del
list2 = [0, 1, 2, 3, 4, 5]
print('list2:', list2)

del list2[1] # 1번 인덱스 자료(값)을 삭제
print('list2:', list2)

list2.pop(1) # 1번 인덱스 자료(값)을 삭제
print('list2:', list2)

list2.pop() # 맨 마지막 사료를 삭제
print('list2:', list2)

# 튜플 - 읽기 전용 리스트 (생성되고 나면 변경 불가능)
t1 = (1, 2, 3)
print('튜플 t1:',t1)
print(type(t1))

t2 = 1, 2, 3
print('튜플 t2:',t2)
print(type(t2))

t3 = tuple([100, 3.14, 'Hello'])
print('튜플 t3:',t3)
print(type(t3))

t4 = (100) # 튜플이 아님! 변수로 인식
print('변수 t4:',t4)
print(type(t4))

t5 = (100,) # t5 = 100,
print('튜플 t5:',t5)
print(type(t5))

# 리스트와 튜플의 차이점
#     리스트는 [], 튜플은 ()
#     리스트는 그 값의 추가, 수정, 삭제 가능
#     튜플은 그 값을 바꿀 수 없다

# 리스트와 튜플의 공통점
#     연산 가능 (덧셈, 곱셈)
#     인덱싱, 슬라이싱 가능 (시퀀스 자료형 - 순서가 있는 자료형)

# 세트 (집합) - 순서가 없으므로 인덱싱, 슬라이싱 불가, set는 중복 제거용으로 사용 (중복된 값 저장 불가)
s1 = {1, 2, 3}
print('set s1:', s1)
print(type(s1))

# 값 1개 추가하기 - add
s1.add(4) # 무조건 맨 뒤에 추가 (순서가 없기 때문에)
print('set s1:', s1)

# 값 여러개 추가하기 - update
s1.update([5, 6, 7])
print('set s1:', s1)

# 특정 값을 제거하기 - remove (인덱싱, 슬라이싱 안되므로 지울 값 직접 기입)
s1.remove(3) # 값 3을 지워라
print('set s1:', s1)

# 딕셔너리 /딕셔너리는 인덱스가 존재않는 대신 키를 인덱스처럼 사용
dic = {} # 빈 딕셔너리
print(type(dic))

s2 = set() # 빈 set
print(s2)
print(type(s2))

dic = {'name': '홍길동', 'birthday':'1212'}
print('딕셔너리 dic:', dic)

# 특정 값을 출력할 때
print(dic['name']) # 값 (홍길동)이 출력
a = dic['birthday'] # 1212가 변수 a에 담긴다
print(a)

# 딕셔너리 값을 수정할 떄
dic['name'] = '라이언'
print(dic['name'])

# 딕셔너리 쌍(키, 값)을 추가할 때 (수정과 추가는 형태가 같음)
dic['address'] = '대구' # 해당하는 키가 없으면 추가 됨
print('딕셔너리 dic:', dic)

# 딕셔너리 쌍을 삭제할 때 - del
del dic['address'] # address에 해당하는 키와 값을 삭제
print('딕셔너리 dic:', dic)

# key 리스트 만들기 - keys
print(dic.keys()) # 키 부분만 따로 모은 것
li = list(dic.keys())
print(li)
print(type(li))

# 값(value) 리스트 만들기 - values
print(dic.values()) # 값 부분만 따로 모은 것

# items 함수를 이용해서 쌍을 얻기
print(dic.items()) # 쌍이 튜플 형식으로 묶인다

# 키와 값을 모두 지우기
dic.clear()
print('딕셔너리 dic:', dic)

# mutable (리스트, 세트, 딕셔너리)
# immutable(정수, 실수, 문자열, 튜플)

##########################################
# 문제1) 문자열 슬라이싱으로 화면 실행 결과와 같도록 출력해보자
# mystr = 'GOOD NIGHT'
# [화면 실행 결과]
# OO
# GH
#  NIGHT

mystr = 'GOOD NIGHT'
print(mystr[1:3])
print(mystr[7:9])
print(mystr[4:])

# 문제2) 과일 이름을 요소로 하는 값이 3개인 리스트 a를 생성해라 (과일이름 3개)
a = ['딸기', '샤인머스캣', '복숭아']
print(a)

# 문제3) 음식 이름을 요소로 하는 값이 3개인 리스트 b를 생성하라 (음식이름 3개)
b = ['삼겹살', '수제비', '갈비']
print(b)

# 문제4) 위 두개의 리스트를 하나로 합친 리스트 c를 생성해라
c = a + b
print(c)

# 문제5) 리스트 c에서 마지막 과일을 다른 과일로 대체해라
c[2] = '자두'
print(c)

