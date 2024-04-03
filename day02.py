# 자료형
    # 프로그래밍할 때 쓰이는 숫자, 문자열 등 자료형태로 사용하는 모든 것
    # 다른 언어의 경우는 변수 설정 시 애초에 타입(자료형)을 설정해야 하는 경우가 많음
    # 파이썬의 경우는 값을 할당하면 그 때 타입이 결정되기 때문에 초보자가 배우기 쉽다
    # type 함수로 자료형을 볼 수 있다

# 예제) 자료형의 type 확인하기
print(type(1)) # 정수형(int)
print(type(1.0)) # 실수형(float)
print(type('Hello')) # 문자열(str)
print(type(True)) # 논리형(bool)

a = 100
print(type(a)) #int

# 정수형
print(int(1.9))
print(int(True)) # 1은 참
print(int(False)) # 0은 거짓

b = '100'   # 문자열
print(type(b))
c = 100     # 정수
print(type(c))

d = int(b)  # b변수의 값을 정수형으로 변환하여 d변수에 담아라
print(type(d))
print(d)

n = 95  # 10진수 정수
print(bin(n)) # 2진수(0, 1)
print(oct(n)) # 8진수(0 ~ 7)
print(hex(n)) # 16진수(0 ~ 9, A ~ F)

# 실수형
print(float(1))
print(float(True))
print(float(False))
print(float('3.14'))
print(float('100'))
print()

# 논리형
print(bool(0))
print(bool(1))
print(bool(2)) # 0을 제외한 나머지 수는 모두 참
print(bool('')) # 비어있는 값은 거짓
print(bool([]))

# 문자열
print(str(100))
print(str(True))
print(str(False))
print(str(3.14))

print('Hello, Python!') # 작은 따옴포
print("Hello, Python!") # 큰 따옴표

print('''
Life is too short,
you need python.
''') # 여러줄 출력할 때는 따옴표 3개를 시작과 끝에 넣는다

print("It's me.") # '를 표현할 때
print('"파이썬 아주 쉽네." 라고 그가 말했다.') # 인용문 넣을 때

# 문자열 인덱싱
    # [0] : 문자열의 처음
    # [-1] : 문자열의 마지막

# 예제)
print('안녕하세요'[-1])
print('안녕하세요'[-2])
print('안녕하세요'[-3])
print('안녕하세요'[-4])
print('안녕하세요'[-5])

a = 'My python'
print(a)
print(a[0])
print(a[2]) # 인덱싱에 포함(공백도 글자다)
print(a[-1])

# 문자열 슬라이싱
#     문자열의 구간을 표시
#     예를 들어 a라는 변수가 있다면
#     a[시작번호:끝번호+1]
#     [:] --> 처음부터 끝까지, 모두를 의미

# 예제)
print('안녕하세요'[1:3])
print('안녕하세요'[2:5])
print()

a = 'python'
print(a[0:2])
print(a[:]) # 모두 다 (전체)
print(a[:3]) # 처음부터 (시작번호를 생략)
print(a[2:]) # 끝까지 (끝번호를 생략)

b = 'Hello'
print(b[1])     # 인덱싱
print(b[2:4])   # 슬라이싱
print(b)        # 원본에는 영향을 주지 않는다

c = b[1]
d = b[2:4]      # 다음에도 사용하려면 변수에 담아서 사용하면 된다
print(c)
print(d)

##############################################################################
# 문제1) 날짜와 시간이 출력되게 만들기
# [화면실행결과]
# 2020/10/31 11:43:59
# print함수의 sep, end

print(2020, 10, 31, sep= '/', end=' ')
print(11, 43, 59, sep=':' )

# 문제2) 화면실행결과를 참고하여 문자열 인덱싱으로 한 글자씩 출력해보자.
# string = 'PYTHON'
# [화면실행결과]
# P
# Y
# H

string = 'PYTHON'
print(string[0])
print(string[1])
print(string[3])