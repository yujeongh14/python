# 주석
'''
작성자 : 황유정
작성일자 : 24-03-13
'''

# 출력해 주는 함수
print('안녕하세요!!')
print('주석 해제하기!!')
# 한꺼번에 주석처리하는 방법
# --> 원하는 부분을 드래그해서 ctrl / 누른다
# --> 주석을 해제할 때도 똑같이 ctrl / 누른다

# 실행하는 방법
# --> 마우스 오른쪽 버튼 -> Run
# --> 또는 단축키 ctrl shift F10

# 저장하는 방법
# --> 실행을 하면 자동저장이 된다.
# --> 그래도 저장하고 싶으면 ctrl s

# print 함수 (표준 출력)
print('안녕~') # 문자는 앞뒤로 작은 따옴표 또는 큰 따옴표를 넣는다

print(1) # 숫자는 따옴표를 붙이지 않는다
print(2)
print(3)
print() # 빈 줄 : 파이썬의 print함수는 기본적으로 엔터를 포함한다

print(1,2,3) # 쉼표 : 구분자, 구분자는 실행 시 스페이스(공백)으로 바뀐다
print(4,'안녕',5,'메롱')
print('     ','빈칸') # 공백도 글자다

print(1,2,3,sep=',') # 출력 시 사이사이에 콤마(,) 표현 -> sep=','
print(4,5,6,sep=':') # 출력 시 사이사이에 콜론(:) 표현 -> sep=','
print(7,8,9,sep='')

print(1,end='') # 엔터 기능을 없앤다
print(2,end=':') # 엔터 대신에 콜론(:)이 나온다
print(3,end='     ') # 엔터 대신에 공백글자 (스페이스)가 나온다
print(4)
print(5)

# 변수
# 상자 또는 그릇(메모리 저장소)에 내용물을 담았다라는 의미
#
#    <형식>
#    변수이름 = 값
#    = : 대입연산자 (assinment operator)
#
#    예약어(키워드) : 특별한 의미가 부여된 단어
#        파이썬에서 미리 특정 의미로 사용하기로 약속해놓은 것
#        프로그래밍에서 이름을 정할 때 똑같이 사용할 수 없다
#        대소문자 구분

# ex) 예약어 확인하는 방법
import keyword
print(keyword.kwlist)
# C:\python_저녁반\venv\Scripts\python.exe C:\python_저녁반\1일차_240313.py
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 예제) 변수에 Alice의 개인정보를 담고 출력해 보기
name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호'''
boyfriend = None # None : 없다
height = 168.5

print('name:',name)
print('age:',age)
print('address:',address)
print('boyfriend:',boyfriend)
print('height:',height)

# 여러개의 변수
a, b, c = 1, 2, 3 # 변수의 값을 대입할 때 한번에 순서대로 대입, 짝이 맞아야 함
print(a)
print(b)
print(c)

a = b = c = 4
print(a)
print(b)
print(c)

# 변수의 교환
a = 1
b = 2
print(a)
print(b)

# a, b = b, a #변수 교환(맞교환 가능)
print(a)
print(b)

#####################################################################################
# 문제1) b라는 변수를 생성하고 음수3을 저장한 후 출력해 보자
b = -3
print(b)

# 문제2) 자신의 이름(영어)을 변수명으로 한 후 자신의 나이를 할당하여 보자
# 출력도 하자
Hwangyujeong = 35
print(Hwangyujeong)