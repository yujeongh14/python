# 반복문 : for문
'''
    반복 횟수가 정해져 있을 때 사용

    <형식>
    for 변수명 in 리스트명:
        반복할 코드

    for 변수명 in range(횟수):
        반복할 코드 - 횟수만큼 실행 -> 0부터 시작

    for 변수명 in range(시작값, 끝값+1):
        반복할 코드

    for 변수명 in range(시작값, 끝값, 증감값):
        반복할 코드

    for _ in range(횟수): # 반복할 변수를 생략 가능(횟수만 반복하고 싶을 때)
        반복할 코드
'''

# 시퀀스와 for문
## for와 리스트
for n in [1, 2, 3]:
    string = ['가위', '바위', '보']
for item in string:
    print(item)

## for문과 문자열
for ch in 'Hello':
    print(ch)

## for문과 tuple
four_seasons = ('Spring', 'Summer', 'Autumn', 'Winter')
for season in four_seasons:
    print(season)

# 예제)
pwd = input('비밀번호를 입력하세요 >>>')

ch_count = 0  # 문자 개수
num_count = 0  # 숫자 개수

for ch in pwd:  # 글자 개수만큼 반복
    if ch.isalpha():  # ch가 문자라면
        ch_count += 1  # 문자 개수 변수를 1 증가시킨다
    elif ch.isnumeric():  # ch가 숫자라면
        num_count += 1  # 숫자 개수 변수를 1 증가시킨다

if ch_count > 0 and num_count > 0:  # 각각 개수가 0보다 크다면
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호 입니다.')

# for문과 range()
for i in range(10):  # 10번 반복, i변수의 초깃값 0
    print(f'{i}번째 문장입니다.')  # 0~9

for i in range(1, 11):  # 10번 반복, i 변수의 초깃값 1, 끝값 10
    print(f'{i}번째 문장입니다.')  # 1~10

for i in range(1, 11, 2):  # 홀수만 출력, 증감값 2
    print(f'{i}번째 문장입니다.')  # 1, 3, 5, 7, 9

for i in range(10, 0, -1):  # 10부터 1까지 1씩 감소
    print(f'{i}번째 문장입니다.')  # 10~1

for i in reversed(range(10)):  # reversed : 반전 (반대로)
    print(f'{i}번째 문장입니다.')  # 9~0

count = int(input('반복할 횟수를 입력하세요'))
for i in range(1, count + 1):
    print(f'{i}번째 문장입니다.')

# 예제) 1부터 100까지 수 중 3의 배수, 5의 배수
for i in range(1, 101):  # 초기값 1, 끝값 100, 증감값 1(생략)
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} : 3과 5의 공배수')
    elif i % 3 == 0:
        print(f'{i} : 3의 배수')
    elif i % 5 == 0:
        print(f'{i} : 5의 배수')
    else:
        print(i)

# 예제) 구구단 만들기
dan = int(input('출력할 구구단을 입력하세요 >>> '))

for n in range(1, 10):  # 1~9
    print('{} x {} = {}'.format(dan, n, dan * n))

# 예제) 중첩 for문을 사용한 구구단 만들기
for i in range(2, 10):  # 단 (2~9)
    print('----{}단----'.format(i))  # 단 제목
    for k in range(1, 10):  # 곱해지는 수 (1~9)
        print('{} X {} = {}'.format(i, k, i * k))
    print()  # 다 끝난 후 빈 줄 추가

# 예제) 중첩 for문을 이용한 별 찍기
# 별찍기1
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

# 별찍기2
for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 별찍기3
for i in range(5):
    for j in range(5):
        if i > j:
            print(' ', end='')
        else:
            print('*', end='')
    print()

# 별찍기4
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()

# 비시퀀스 for문

## for문과 세트
for item in {'가위', '바위', '보'}:
    print(item)  # 순서는 랜덤으로 나온다

## for문과 딕셔너리
person = {
    'name': '에밀리',
    'age': 20
}
for item1 in person:
    print(item1)  # 키(key)가 출력

for item2 in person:
    print(person[item2])  # 값(value)을 출력

for item3 in person:
    print(person.get(item3)  # 값(value)을 출력

    ##########################################################
    # 문제1) 조건문 문제 if
    # 한 점을 구성하는 (x, y) 좌표를 입력받고, 이 점이 (50, 40), (50, 80)
    # (100, 40), (100, 80)을 꼭짓점으로 갖는 사각형이 안에 있는지
    # 판별하는 프로그램을 작성하시오.
    # (선 위에 점이 있는 것은 포함하지 않는 걸로 한다.)
    # [화면실행결과]
    # x좌표를 입력하세요 : 60
    # y좌표를 입력하세요 : 100
    # 사각형 안에 없습니다.

    x = int(input('x좌표를 입력하세요 : '))
    y = int(input('y좌표를 입력하세요 : '))
    if 50 < x < 100 and 40 < y < 80:
        print('사각형 안에 있습니다.')
    else:
        print('사각형 안에 없습니다.')

    # 문제2) for, range
    # for를 이용해서 1~5까지의 숫자들을 차례대로 출력하기
    # [화면실행결과]
    # 1 2 3 4 5

    for i in range(1, 6):
        print(i, end=' ')