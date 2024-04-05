# 과제) if문제
# 년도를 입력받아 윤년인지 판단해 주는 프로그램을 작성하시오.
# 년수가 4로 나누어 떨어지는 해는 윤년 (2월 29일)
# 그 중에서 100으로 나누어 떨어지는 해는 평년
# 다만, 400을 나누어 떨어지는 해는 다시 윤년
# 예를 들어, 2016년은 윤년, 2100년은 평년, 2000년은 윤년
# [화면실행결과]
# 년도를 입력하세요 : 2021
# 평년입니다.

### 내가 작성한 답 ###
year = int(input('년도를 입력하세요 : '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('윤년입니다.')
else:
    print('평년입니다.')

### 선생님이 작성한 답 ###
year = int(input('년도를 입력하세요 : '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('윤년입니다.')
else:
    print('평년입니다.')

# 예제) 딕셔너리를 활용한 영어 사전 만들기
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}
for word in eng_dict:
    print('{}의 뜻 : {}'.format(word,eng_dict.get(word)))

# 기타 제어문
# break문은 while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# 예제) 0부터 99까지 출력
i = 0
while True: # 무한 반복
    print(i, end=' ') # i출력
    i += 1 # i = i + 1
    if i == 100: # i가 100이 되면
        break   # 제어 흐름을 빠져나온다 (반복문을 종료)

# 예제) while-break를 이용한 수도 맞히기
while True:
    city = input('대한민국의 수도는 어디인가요? >>>')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다~!')
        break # 반복문을 종료
    else:
        print('오답입니다. 다시 시도하세요.')

# 예제) while-break를 이용한 취미를 리스트에 담기
hobbies = []
while True:
    hobby = input('취미를 입력하세요 (종료는 엔터) >>>')
    if hobby == '': # 아무것도 입력되지 않으면
        print('입력된 취미가 모두 저장되었습니다.')
        break # 반복문을 종료
    else:
        hobbies.append(hobby) # hobby변수에 담긴 값을 리스트에 추가
print(hobbies) # 반복문이 모두 끝난 후에 실행

# 예제) while, if, break 반복문을 이용한 커피자판기 프로그램
coffee = 3
while True:
    money = int(input('돈을 넣어주세요: '))
    if money == 300: # 커피값이 300원이라고 가정했을 경우
        print('커피 나왔습니다!')
        coffee -= 1 # coffee = coffee - 1
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    elif money > 300:
        print(f'거스름돈 {money-300}원을 주고 커피도 줍니다!')
        coffee -= 1
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    else:
        print(f'{money}원을 다시 돌려주고 커피는 주지 않습니다!')
        print(f'남은 커피의 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다!')
        break

# continue : 바로 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 continue문을 사용
# 예제) 0~10 사이의 수 중에서 홀수만 출력
a = 0
while a < 10:
    a += 1 # a = a + 1
    if a % 2 == 0: # 짝수라면
        continue
    print(a)

# 예제) 서로 다른 과일 5개를 담아보기 (중복x)
fruits = ['사과', '감귤']
count = 3 # 입력해야 할 남은 과일의 수
while count > 0:
    fruit = input('어떤 과일을 저장할까요? >>> ')
    if fruit in fruits: # friut변수에 있는 값이 fruits 리스트에 포함되었나?
        print('동일한 과일이 있습니다.')
        continue # 포함되었다면 다시 반복문의 처음(조건쪽)으로 간다
    fruits.append(fruit) # 포함되지 않았다면 리스트에 추가
    count -= 1 # 횟수를 1번 줄여준다
    print('입력이 {}번 남았습니다.'.format(count))
print('5개의 과일은 {}입니다.'.format(fruits))

# 예제) 5개의 양수를 입력받아 총 합을 구하기. 0이나 음수는 입력받지 않는다.
count = 0
total = 0 # 합계

while count < 5:
    n = int(input('{}번째 정수를 입력하세요 >>> '.format(count + 1)))
    if n <= 0: # 0과 음수를 제외하기 위해 넣은 코드
        print('0이하의 정수는 처리할 수 없습니다.')
        continue
    total += n # n의 값을 합계에 누적시킨다
    count += 1 # 횟수도 1증가 시킨다
print('입력된 5개의 양수의 총 합은 {}입니다.'.format(total))

# 리스트 내포 (리스트 컴프리헨션)
# 리스트를 생성할 때 for문을 유용하게 사용할 수 있습니다.
# 리스트 내부에 for문을 포함하는 방식을 사용하면 리스트를 쉽게 생성할 수 있습니다.
# 리스트 =[표현식 for 변수 in 반복가능개체]
# 리스트 =[표현식 for 변수 in 반복가능개체 if 조건식]

# 예제) append 사용 vs 리스트 내포 사용
# append 사용
li = [1, 2, 3]
num1 = []
for n in li:
    num1.append(n * 2) # n에 2를 곱한 후 num1 리스트에 추가
print('append 사용 : {}'.format(num1))

# 리스트 내포 사용
li = [1, 2, 3]
num2 = [n * 2 for n in li]
print('리스트 내포 사용 : {}'.format(num2))

###################################################
# 문제1) 1부터 100까지 수 중에서 5와 7의 공배수를 출력하여라
# 그 외의 숫자는 출력하지 말 것!
# [화면실행결과]
# 35 : 5와 7의 공배수
# 70 : 5와 7의 공배수

for i in range (1,101):
    if i % 5 == 0 and i % 7 == 0:
        print(f'{i} : 5와 7의 공배수')

# 문제2) for문을 이용하여 1부터 10까지의 합을 구하시오.
# [화면실행결과]
# 1부터 10까지의 합 : 55
# 힌트 : 합계를 담을 변수를 먼저 만들어서 초기화하고 진행하기

sum = 0 # 합계
for i in range(1,11):
    sum += i # sum = sum + i
print(f'1부터 10까지의 합 : {sum}')

# 문제3) for문을 이용하여 1부터 키보드로 입력한 값까지의 합을 구하시오.
# [화면실행결과]
# 값을 입력하시오 : 123
# 1부터 123까지의 합계 : 7626

num = int(input('값을 입력하시오'))
sum = 0
for i in range(1, num + 1):
    sum += i
print('1부터 {}까지의 합계 : {}'.format(num, sum))