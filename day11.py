# 매개변수(입력값), 반환값(출력값)이 2개 이상인 함수 (반환값은 원래 무조건 1개, 근데 튜플로 묶어서 여러 개 나오기에 값이 여러 개 나온다고 표현)
#
#     <형식>
#     def 함수이름 (매개변수1, 매개변수2): # 함수 정의
#         수행할 코드 - 있으면
#         return 반환값1, 반환값2
#
#     결과변수1, 결과변수2 = 함수이름(인수1, 인수2) #함수 호출

# 예제)
def add_sub(a, b):  # 함수 정의
    return a + b, a - b

x, y = add_sub(1, 2) # 함수 호출
print(x)    # 첫 번째 결과값을 x변수에
print(y)    # 두 번째 결과값을 y변수에 담았다

print(add_sub(10, 20))

# 디폴트 매개변수 (매개변수에 초깃값)
# 예제)
def info(name, age, address='비공개'): # 함수 정의
    print('이름 : {}'.format(name))
    print('나이 : {}'.format(age))
    print('주소 : {}'.format(address))
    print('---------------------')

info('네오',25) # 함수 호출
info('라이언', 20, '대구')

# 키워드 인수 : 각각의 매개변수가 어떤 용도인지 알기 어려울 때 사용
# 예제)
def info(name, age, address): # 함수 정의
   print('이름 : {}'.format(name))
   print('나이 : {}'.format(age))
   print('주소 : {}'.format(address))
   print('---------------------')

info('라이언', 20, '대구') # 일반적인 호출 방식
info(name ='어피치', age = 30, address = '부산') # 키워드 인수
info(age = 40, address = '서울', name = '춘식이') # 순서를 다르게 지정해도 된다 (근데 이렇게 쓰진 말기!)

# 가변 매개변수 : 매개변수 (입력값)의 개수를 정확히 모를 때 사용
#
#     <형식>
#     def 함수이름(*매개변수명): # 함수 정의
#         수행할 코드
#
#     함수 이름(필요한 인수만큼 입력) # 함수 호출

# 예제)
def adder(*args): # 함수 정의
    print('{}의 합은 {}입니다.'.format(args, sum(args)))

adder(1, 2) # 함수 호출
adder(1, 2, 3)
adder(1, 3, 5, 7, 9)

# 예제)
def add_mul(choice, *args): # 함수 정의(가변 매개변수를 맨 뒤로)
    if choice == 'add':
        answer = 0 # 합계를 담을 변수 초깃값을 0으로 한다.
        for i in args: # 가변매개변수 args의 개수만큼 반복
            answer += i # answer = answer + i
    elif choice == 'mul':
        answer = 1 # 초깃값을 1로 한다 (곱하기 할 때 초깃값을 0으로 하면 0이 됨)
        for i in args:
            answer *= i # answer = answer * i

    return answer # 결과로 나온 answer를 반환한다

a = add_mul('add', 1, 2, 3) # 1+2+3
print(a)

b = add_mul('mul', 4, 5, 6, 7) # 4*5*6*7
print(b)

# 예제) 자판기 만들기
def coffee_machine(money, pick): # 함수 정의
    print('{}원의 {}를 선택하셨습니다.'.format(money, pick))
    menu = {
        '아메리카노': 1000,
        '카페라떼' : 1500,
        '카푸치노' : 2000
    }
    if pick not in menu: # 메뉴에 없는 음료라면
        print('{}는 판매하지 않습니다.'.format(pick))
        return money, '없는 메뉴' # 돈을 다시 돌려준다. 없는 메뉴라는 글자 반환
    elif menu[pick] > money: # 해당 음료의 금액이 부족한 경우
        print('{}는 {}입니다.'.format(pick, menu[menu]))
        return money, '금액 부족'
    else: # 정상적인 경우
        return money-menu[pick], pick # 음료값을 제외한 잔돈과 음료 이름 반환

pick = input('커피를 선택하세요(아메리카노, 카페라떼, 카푸치노) >>> ')
money = int(input('얼마를 내시나요? >>> '))

money, pick = coffee_machine(money, pick) # 반환 값이 2개이므로 결과 변수 2개
print('잔돈 {}원, 선택한 메뉴는 {}입니다.'.format(money, pick))

# 지역 변수 / 전역 변수

#    지역 변수 : 한정된 지역(함수 안)에서 사용
#    전역 변수 : 프로그램 전체에서 사용, 예약어 globals()

# 예제)
a = 100 # 전역 변수

def func1(): # 함수 정의
    a = 10 # 지역 변수( 이 함수 안에서만 사용)
    print('func1에서의 a의 값 : {}'.format(a))

def func2(): # 함수 정의
    print('func2에서의 a의 값 : {}'.format(a))

func1() # 함수 호출
func2() # 함수 호출

# 예제) 전역 변수의 값을 변경해야 하는 경우
b = 0 # 전역 변수

def f(): # 함수 정의
    global b # 전역 변수 b를 가리킨다
    b = 10 # 전역 변수 b의 값을 10으로 변경한다

print('함수 호출 전 : {}'.format(b))
f() # 함수 호출
print('함수 호출 후 : {}'.format(b))

########################################################################
# 사용자함수 문제 1)
# 매개변수를 통해서 두 개의 정수를 전달받는다.
# 이 둘의 평균값을 계산해서 화면에 출력하는 함수를 만들어보자.
# 예를 들어 3과 4가 전달되면 이 두 수의 평균값 3.5가 출력되어야 한다.
# 함수 이름은 average로 하고, 매개변수명은 각각 num1, num2로 한다.
# 반환값은 return은 없다.
# 함수 호출은 한번만 한다.
# [화면실행결과]
# 3.5

def average(num1, num2): # 함수 정의
    print((num1 + num2)/2) #

average(3, 4)

# 사용자함수 문제 2)
# 하나의 정수를 매개변수에 전달받아서 부호가 반대인 정수를 반환하는 함수를 정의해 보자.
# 함수 이름은 하고 싶은대로 하고, 매개변수명도 자유롭게 한다.
# 반환값 return이 있도록 한다.
# 호출할 때 반환값은 따로 결과변수에 담도록 하고, 그 변수값을 출력해 본다.
# 함수 호출은 한번만 한다.
# [화면실행결과] (호출할 때 인수를 12로 넣었을 경우)
# -12

def number(num): # 함수 정의
    return num * -1

result = number(12) # 함수 호출
print(result)



