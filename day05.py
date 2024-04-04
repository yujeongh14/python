# 연산자
## 산술연산자
# 예제)
a = 7
b = 2
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} ** {} = {}'.format(a, b, a ** b))  # 거듭제곱
print('{} / {} = {}'.format(a, b, a / b))  # 나누기 산술을 진행하면 무조건 결과가 실수형
print('{} // {} = {}'.format(a, b, a // b))  # 몫
print('{} % {} = {}'.format(a, b, a % b))  # 나머지

# 대입연산자
## 복합연산자
# 예제) a가 10에서 시작해서 코드가 진행될수록 값이 변하도록 해보기
a = 10
# print('a의 값 : {}'.format(a))

a += 5  # a = a + 5
print('a의 값 : {}'.format(a))

a -= 5  # a = a - 5
print('a의 값 : {}'.format(a))

a *= 5  # a = a * 5
print('a의 값 : {}'.format(a))

a /= 5  # a = a / 5
print('a의 값 : {}'.format(a))  # 결과가 실수형

a %= 5  # a = a % 5
print('a의 값 : {}'.format(a))

# 예제) 저금통에 있는 용돈으로 스낵 구입하기
piggy_bank = 0  # 저금통
money = 10000
piggy_bank += money  # piggy_bank = piggy_bank + money
print('저금통에 용돈 {}원을 넣었습니다.'.format(money))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))
snack = 2000
piggy_bank -= snack  # piggy_bank = piggy_bank - snack
print('저금통에서 스낵 구입비 {}을 뺐습니다.'.format(snack))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

## 관계연산자 : 2개의 항을 비교하여 그 결과를 논리(bool)자료형으로 반환하는 연산자
# 예제)
a = 15
print('{} > 10 :{}'.format(a, a > 10))
print('{} < 10 :{}'.format(a, a < 10))
print('{} >= 10 :{}'.format(a, a >= 10))
print('{} <= 10 :{}'.format(a, a <= 10))
print('{} == 10 :{}'.format(a, a == 10))
print('{} != 10 :{}'.format(a, a != 10))

## 논리연산자 : 관계연산자와 함께 사용되는 연산자로 2개 이상의 항을 논리적으로 연결할 때 사용하는 연산자
# 예제)
a = 10  # True (참)
b = 0  # False (거짓)
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0))
print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b > 0))
print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(b, not b))

## 비트연산자 (파이썬에서 중요x)
# 예제)
a = 10  # 00001010 (2진수)
b = 70  # 01000110
print('a & b : {}'.format(a & b))  # 00000010 (둘 다 1일 때 1) # 1의 자리 2의 0승 = 0 , 10의 자리 2의 1승 = 2
print('a | b : {}'.format(a | b))  # 01001110 (둘 중 하나가 1일 때 1)
print('a ^ b : {}'.format(a ^ b))  # 01001100 (서로 다르면 1)
print('~a: {}'.format(~a))  # 11110101 (not, 0을 1로 1은 0으로 변경)
# 2진수 맨 앞자리 1은 음수, 0은 양수
print('a << 1 : {}'.format(a << 1))  # 00010100 (왼쪽으로 1칸씩 이동)
print('a >> 1 : {}'.format(a >> 1))  # 00000101 (오른쪽으로 1칸씩 이동)

## 시퀀스연산자 : 순서가 있는 데이터 구조인 시퀀스에서 사용할 수 있는 연산자 (+ , *)
# 예제) 기호로 크리스마스 트리 만들기
tree = '#'
space = ' '
print(space * 4 + tree * 1)
print(space * 3 + tree * 3)
print(space * 2 + tree * 5)
print(space * 1 + tree * 7)
print(space * 0 + tree * 9)

# 기타 연산자
## 멤버쉽 연산자 (in 연산자, not in 연산자)
# 예제)
print('안녕' in '안녕하세요')  # 포함되어 있다
print('메롱' in '안녕하세요')  # 포함되어 있지 않다
print('안녕' not in '안녕하세요')  # 포함되어 있다
print('메롱' not in '안녕하세요')  # 포함되어 있지 않다

## 조건 연산자 (삼항연산자) 참 if 조건식 else 거짓
# 예제)
a = 10
b = 20
result = (a - b) if (a >= b) else (b - a)
print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))

# if 조건문
# 예제) 100보다 작은 수인가요?
a = 99
if a < 100:
    print('100보다 작군요!')  # 참일 때만 출력

num = int(input('정수를 입력하세요 : '))
if num > 0:
    print('양수입니다!')
if num == 0:
    print('0입니다!')
if num < 0:
    print('음수입니다!')

# if - else문
# 예제) 나이를 입력 받은 후 성인,미성년자 구분하기
age = int(input('몇 살입니까? >>> '))
if age >= 20:
    print('성인!')  # 참일 경우
else:
    print('미성년자!')  # 거짓일 경우

# 예제2) 문자열 판단
string = 'python'
id = input('아이디를 입력하세요 : ')
if id == string:
    print('환영합니다!')  # 참
else:
    print('아이디를 찾을 수 없습니다!')  # 거짓

# 예제) 값을 입력받아 짝수, 홀수 구분하기
num = int(input('정수를 입력하세요 : '))
if num % 2 == 0:
    print('짝수!')  # 참
else:
    print('홀수!')  # 거짓

# 예제) 값을 입력 받아 in 연산자를 활용하여 짝수, 홀수 구분하기
num = input('정수를 입력하세요 : ')  # 문자열 형식으로 입력받을 것
a = num[-1]  # 맨 끝 글자를 a 변수에 담는다. 일의 자리. 문자열이라 인덱싱 가능. 숫자는 인덱싱 불가능
if a in '02468':  # 만약 맨 끝 글자가 02468 안에 있는 글자라면 (포함되었다면)
    print('짝수!')  # 참인 경우 짝수
else:
    print('홀수!')  # 거짓인 경우 홀수 (13579)

######################################################################
# 문제1) 정수 변수 2개를 만들어 숫자를 입력받는다. (input함수)
# 아래의 출력결과처럼 나오게 해보자
# [화면실행결과]
# 첫번째 정수는? 13
# 두번째 정수는? 5
# 나눈셈의 몫은 2 나머지는 3입니다.
a = int(input('첫번째 정수는? '))
b = int(input('두번째 정수는? '))
print('나눗셈의 몫은 {} 나머지는 {}입니다.'.format(a // b, a % b))

# 문제2) 변수 height를 정수형(int)로 만들어 값을 입력하시오. (input함수)
# 변수 weight를 실수형(float)으로 만들어 값을 입력하시오.
# [화면실행결과]
# 키가 얼마인가? 165
# 몸무게가 얼마인가요? 50.0
# 키 + 몸무게 = 215.0
height = int(input('키가 얼마인가요? '))
weight = float(input('몸무게가 얼마인가요? '))
print('키 + 몸무게 = {}'.format(height + weight))