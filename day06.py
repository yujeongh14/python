# if-elif
# 예제) 값을 입력 받아 음수, 양수, 0 구분하기
num = int(input('정수를 입력하세요 : '))
if num > 0:
    print('양수입니다!')
elif num == 0:
    print('0입니다!')
else:
    print('음수입니다!')

# 반복문 (while, for)
# while
#     <형식 : 조건문으로 판단하는 경우>
#     while 조건식:
#         이 부분을 반복
#
#     <형식 : 반복 횟수가 정해진 경우>
#     변수 = 시작 값
#     while 변수 < 끝 값:
#         변수 = 변수 + 증감 값
#         추가적인 코드들~

# 예제) 100번 출력
i = 0 # 시작 값 (초기식)
while i < 100: # while 조건식
    print('Hello, World!')
    i = i + 1 # i += 1 (증감식, 1씩 증가)

# 예제) 10부터 1까지 출력
n = 10 # 시작 값 (초기식)
while n >= 1:
    print(n)
    n -= 1 # n = n -1 (증감식, 1씩 감소)

# 예제) 무한 반복
while True:
    print('ㅋ', end='')

# 예제) while을 이용해서 숫자로 데미지를 입힌 후 체력이 0이 되면 종료하기
hp = 100 # 기본 체력은 100으로 한다
while hp > 0: # hp가 0보다 작거나 같으면 반복문을 종료
    print(f'주인공의 체력은 {hp}입니다!') # f-strings 포매팅 형식
    damage = int(input('얼마의 데미지를 입히겠습니까?')) # 실행 시 입력
    hp -= damage # hp = hp - damage

print('주인공의 체력은 0이 되어 종료합니다!') # 반복문이 끝난 후에 실행

# 예제)
my_list = []
n = int(input('정수를 입력하세요 (종료는 0입니다) >>> '))
while n != 0: # n이 0이 되면 종료
    my_list.append(n) # 리스트에 변수 n의 값을 추가한다
    n = int(input('정수를 입력하세요 (종료는 0입니다) >>> '))
print(my_list)

# while문의 중첩
# 예제) 1~5일의 1~3교시 나타내기
day = 1
while day <= 5: # 일차
    hour = 1
    while hour <= 3: # 교시
        print('{}일차 {}교시 입니다.'.format(day, hour))
        hour += 1 # 교시 1 증가
    day += 1 # 일차 1 증가

# 예제) 구구단 만들기
dan = 2 # 구구단의 단
while dan <= 9: # 2~9
    print('----{}단----'.format(dan))
    n = 1 # 곱해지는 수
    while n <= 9: # 1~9
        print(f'{dan} x {n} = {dan * n}')
        n += 1 # n = n + 1 # 곱해지는 수를 1 증가
    print() # 빈 줄을 추가
    dan += 1 # dan = dan + 1 # 단을 1 증가

#################################################
# 문제) 변수 age에 나이를 입력받은 후 15세 이상이면 영화를 볼 수 있고,
# 아니면 영화를 볼 수 없다는 코드를 작성하시오.
# [화면실행결과]
# 당신의 나이는?? 17
# 이 등급의 영화를 볼 수 있습니다.
age = int(input('당신의 나이는??'))
if age >= 15:
    print('이 등급의 영화를 볼 수 있습니다.')
else:
    print('이 등급의 영화를 볼 수 없습니다.')

# 문제2) 변수 n에 정수를 입력받는다.
# 입력받은 정수가 10보다 크면 '10보다 크다.', 10보다 작으면 ' 10보다 작다.'
# 10과 같으면 '10과 같다.'
# 라고 출력해 보세요
n = int(input('정수를 입력하세요 : '))
if n > 10:
    print('10보다 크다.')
elif n < 10:
    print('10보다 작다.')
else:
    print('10과 같다.')