# 기본 입출력
# 표준 출력
# 이스케이프 문자
#     프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 문자 조합
#     출력물을 보기 좋게 보는 용도로 사용
#     대표적인 것 ----> \n (엔터)

# print('Hello \'World\'')
# print("Hello 'World'")
#
# print("Hello \"World\"")
# print('Hello "World"')
#
# print('*\n**\n***')
#
# # 예제)
# print('재미있는','파이썬')
# print('Python', 'Java', 'C', sep=',')
#
# print('영화 타이타닉')
# print('평점', end=':')
# print('5점')
#
# fos = open('sample.py', mode='wt') # 파일 열기
# print('print("Hello World")', file=fos) # 파일에 출력 (저장)
# fos.close() # 파일 담기
#
# # 형식을 갖춘 문자열 (문자열 포매팅)
# # % 연산자 (기본 포매팅)
# # 예제)
# name = 'Kai' # 문자열
# print('내 이름은 %s 입니다.' %name)
#
# height = 120.6 # 실수
# print('내 키는 %.fcm입니다.' %height) # 소수 여섯 째자리까지 출력
#
# weight = 23.55 # 실수
# print('내 몸무게는 %.1fkg입니다.' %weight) # 소수 첫 째자리까지 반올림
#
# year, month, day = 2024, 3, 20 # 정수
# print('내 생일은 %d년 %d월 %d일 입니다.' % (year, month, day)) # (year, month, day) -> 튜플
#
# # .format()
# # <형식>
# # '문자열 {}'.format(변수명)
#
# # 예제)
# zipcode = '06236'
# print('우편번호 : {}'.format(zipcode))
#
# address = '''서울특별시 강남구
# 테헤란로 146'''
# print('주소 : {addr}'.format(addr=address))
#
# tel1, tel2, tel3 = '02', '538', '0021'
# print('연락처 : {0}-{1}-{2}'.format(tel1, tel2, tel3))
#
# # 예제)
# print('{0:<10}'.format('Hi')) # 전체 10칸, 왼쪽 정렬
# print('{0:>10}'.format('Hi')) # 전체 10칸, 오른쪽 정렬
# print('{0:^10}'.format('Hi')) # 전체 10칸, 가운데 정렬
#
# print('{:=^8}'.format('python')) # 전체 8칸, 공백을 =로 표현, 가운데 정렬
# print('{:!<8}'.format('python')) # 전체 8칸, 공백을 !로 표현, 왼쪽 정렬
#
# n = 3.141592
# print('{:.3f}'.format(n)) # 소수 셋 째자리까지 반올림
#
# a = '파이썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
# b = '{} {}               {}'.format(100, 200, 300)
# c = '{} {} {}'.format(1, '파이썬', True)
# print(a)
# print(b)
# print(c)
#
# # f-strings (f 문자열 포매팅)
# #     <형식>
# #     f'문자열 {변수명} 문자열'
#
# # 예제)
# name = '라이언'
# age = 20
# print(f'나의 이름은 {name}입니다. 나이는 {age}살입니다.')
# print(f'나는 내년이면 {age+1}살이 됩니다.')
#
# print(f'{"python":=^30}')  # 전체 30칸, 공백을 =로 표현, 가운데 정렬
# print(f'{"python":!<30}')  # 전체 30칸, 공백을 !로 표현, 왼쪽 정렬
#
# n = 3.141592
# print(f'{n:.3f}') # 소수 셋 째자리까지 반올림
#
# # 포매팅 비교하기
# n = 3 # 정수
# print('I eat', n, 'apples.')
# print('I eat %d apples.' %n) # % 연산자 포매팅(기본 포매팅)
# print('I eat {} apples.'.format(n)) # format 메서드 포매팅
# print(f'I eat {n} apples.') # f-strings (f 문자열 포매팅)
#
# # 예제 ) 포매팅
# price = 50000 # 물건 값
# n = int(input('할부 개월 입력 >>> ')) # 정수로 형 변환
# print('매달 내는 돈은 {}원입니다.'.format(price / n)) # 실수형으로 출력 (기본 형태)
#
# # 표준 입력 (input)
# n = input('정수를 입력하세요 : ')
# print(n)
#
# # 예제)
# name = input('이름을 입력하세요 >>>')
# age = input('나이를 입력하세요 >>>')
# print('입력된 이름은 {}입니다.'.format(name))
# print('입력된 나이는 {}살입니다.'.format(age))
#
# # 예제) input의 형변환
# a = input('입력 : ')
# print('변수 a의 값 {}'.format(a))
# print('변수 a의 자료형(타입) : {}'.format(type(a)))
# print()
#
# b = int(input('입력 : '))
# print('변수 b의 값 : {}'.format(b))
# print('변수 b의 자료형(타입) : {}'.format(type(b)))
#
# # 예제) 더하기 계산의 차이
# s1 = input('입력 s1 : ') # 문자열로 입력됨
# s2 = input('입력 s2 : ')
# print('s1 + s2 = {}'.format(s1 + s2)) # 문자열이니까 이어붙임(연결)
# print()
#
# i1 = int(input('입력 i1 : ')) # 정수형으로 형변환
# i2 = int(input('입력 i2 : '))
# print('i1 + i2 : = {}'.format(i1 + i2)) # 정수형이니까 더하기 계산
#
# # 예제) 실수형으로 입력받기
# num1 = float(input('실수로 된 첫번째 숫자 : '))
# num2 = float(input('실수로 된 두번째 숫자 : '))
# print('덧셈 결과 : {}'.format(num1 + num2))
# print('뺄셈 결과 : {}'.format(num1 - num2))
#
# #########################################################
# # 문제1) 변수 number에 정수 5를 담고 오늘 배운 3가지 포매팅 형식으로
# # 출력해보자.
# # [화면실행결과]
# # I eat 5 apples.
# # I eat 5 apples.
# # I eat 5 apples.
#
# number = 5
# print('I eat %d apples.' %number)
# print('I eat {} apples.'.format(number))
# print(f'I eat {number} apples.')
#
#
# # 문제2) 정수 변수 2개를 만들어 숫자를 입력받는다 (input함수)
# # 아래의 출력 결과처럼 나오게 해보자
# # [화면실행결과]
# # 첫 번째 정수는 ? 13
# # 두 번째 정수는 ? 5
# # 두 수를 더하면 18입니다.
# a = int(input('첫 번째 정수는 ?'))
# b = int(input('두 번째 정수는 ?'))
# print('두 수를 더하면{}입니다.'.format(a + b))

# 정수 입력 받기
# num = int(3)
#
# # 입력된 정수의 이진, 16진수, 8진수 표현 구하기
# binary = bin(num)
# hexadecimal = hex(num)
# octal= oct(num)
#
# # 결과 출력
# print("입력한 정수:", num)
# print("이진수 표현:", binary)
# print("16진수 표현:", hexadecimal)
# print("8진수 표현:", octal)

li = [7, 8, 10, 2, 4, 3]

# len() : 길이(항목 수) 구하기
length = len(li)
print(length) # 6

# max() : 최댓값 구하기
max_value = max(li)
print(max_value) # 10

# min() : 최솟값 구하기
min_value = min(li)
print(min_value) # 2

# sorted() : 정렬 후 리스트로 반환
sorted_value = sorted(li)
print(sorted_value) # [2, 3, 4, 7, 8, 10]

# enumerated() : 인덱스와 요소 함께 반환
for index, value in enumerate(li):
    print(f'{index}번째:{value}') # [2, 3, 4, 7, 8, 10]

# zip() : 튜플로 묶어 반환
letters = ['a', 'b', 'c', 'd', 'e']
zipped = zip(li, letters)
print(list(zipped))