# 모듈과 import

# 모듈을 불러와서 사용하기
#
#     <형식>
#     import 모듈이름 as 별칭 --> as 별칭은 생략 가능
#     또는
#     from 모듈이름 import 모듈함수
#     --> 호출 시 모듈 이름을 생략하고 함수만 사용하고 싶을 떄
#     from 모듈이름 import *
#     --> 모듈 안에 있는 모든 함수를 당겨쓸 때 모두의 의미를 가진 *를 사용

# ex) import 방식
import m # m이라는 모듈(파이썬 파일)을 불러온다
''
result1 = m.add(1, 2) # m모듈에 있는 add함수를 호출
result2 = m.sub(2, 1) # m모듈에 있는 sub함수를 호출
print(result1)
print(result2)

# ex) from방식 (1)
from m import mul, div # m모듈에 있는 mul, div함수 가져온다

result3 = mul(1,2) # from으로 가져올 때는 모듈명이 필요없다
result4 = div(2,1) # from으로 가져올 때는 모듈명이 필요없다
print(result3)
print(result4)

# ex) from방식 (2)
from m import * # m모듈안에 있는 모든 함수를 가져온다

x = int(input('x를 입력하세요 : '))
y = int(input('y를 입력하세요 : '))
n1 = add(x, y)
n2 = sub(x, y)
n3 = mul(x, y)
n4 = div(x, y)
print(n1, n2, n3, n4, sep='\n')

# 예제)
from my_secure import *
print(secure_name('김철수'))
print(secure_no('951012-123456'))
print(securte_phone('010-1234-5678'))

# __name__
#
#     현재 모듈의 이름을 담고 있는 내장 변수
#
#     원래 파일에서 실행하면 __name__에
#     '__main__'이 할당
#     모듈로 참조하고 있는 다른 파일에서 실행하면
#     __name__에 해당 모듈명이 할당됨

# 예제)
from my_secure import *

print(secure_no('951012-1234567'))

# 표준 모듈
# math 모듈
import math

print(math.pi) # 원주율
print(math.ceil(1.1)) # 올림
print(math.floor(1.9)) # 내림
print(math.sqrt(25)) # 제곱근(루트)
print(math.pow(2, 3)) # 거듭제곱

# random 모듈
import random

print(random.randint(1, 10)) # 1 이상 10이하의 정수 중 아무 정수

print(random.randrange(10)) # 0~9 중 아무 정수
print(random.randrange(1, 11)) # 1~10 중 아무 정수
print(random.randrange(1, 10, 2)) # 1, 3, 5, 7, 9 중 아무 정수

print(random.random()) # 0이상 1미만 중 아무 숫자(실수)

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons)) # seasons 리스트 값 중 하나

print(random.sample(range(1, 46), 6)) # 중복없이 6개의 숫자를 리스트 형태로

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list) # 임의로 섞기
print(my_list)

# 예제) 주사위 숫자 맞추기!
import random

dice = random.randint(1, 6) # 1~6
while True:
    user = int(input('주사위 값은 얼마일까요? >>> '))
    if dice == user:
        print('{}! 정답입니다!'.format(dice))
        break
    else:
        print('오답입니다! 다시 시도해보세요!')

# 예제) 모듈을 이용해서 속으로 10초 세어 맞히는 프로그램
import time

input('엔터를 누르고 10초를 셉니다!')
start = time.time() # 현재 시간을 저장

input('10초 후에 다시 엔터를 누릅니다!')
end = time.time()

es = end - start # 두 시간의 차이
print(f'실제 걸린 시간 : {es}초')
print(f'내가 예측한 시간과의 차이 : {abs(es-10)}') # abs() : 절대값

# 예제)
from datetime import *

start = datetime.now() # 계산하기 전 현재 날짜와 시간
total = 0
for num in range(1, 10000001):
    total += num
end = datetime.now() # 계산 완료 후 현재 날짜와 시간
elapse = end - start # 차이
elapse = elapse.total_seconds() # 초 단위로 변환해서 다시 저장
print('총 합은 {}입니다.'.format(total))
print('총 {}초가 소요되었습니다.'.format(elapse))
###################################################
# 사용자 함수 문제)
# 두 개의 정수를 전달받아서 그 두 수의 몫과 나머지를 각각 반환하는 함수를 만들어 보자
# 이 때 두개의 정수는 input을 이용해서 입력받는다
# 반환값 return이 있도록 하고, 함수 이름과 매개변수이름 등은 자유롭게 한다
# 함수 호출은 한 번만 한다.
# [화면실행결과]
# 첫번째 수를 입력하세요 : 5
# 두번째 수를 입력하세요 : 2
# 2 1

# 전역변수
num1 = int(input('첫번째 수를 입력하세요 : '))
num2 = int(input('두번째 수를 입력하세요 : '))
def calc(num1, num2): # 여기의 매개변수는 지역변수
    return num1 // num2, num1 % num2
quotient, remainder = calc(num1, num2)
print(quotient, remainder)