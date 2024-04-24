# 클래스와 객체2
# 생성자 (constructor)
#
#     객체에서 초깃값을 설정해야 할 필요가 있을 때 사용
#     ex) set_info()
#     객체가 생성될 때 자동으로 호출해주는 메서드
#     __init__ 사용
#     스페셜메서드(매직메서드) : 파이썬에서 자동으로 호출되는 메서드
#                             앞뒤로 __가 붙은 메서드
#     <형식>
#     class 클래스이름:
#         def__init__(self): # 생성자 (인스턴스 메서드)
#             self.속성 = 값 # 인스턴스 변수

# ex) 생성자를 사용하지 않은 경우
# class Candy: # 클래스 정의
#     def set_info(self, shape, color): # 인스턴스 메서드 정의
#         self.shape = shape # 인스턴스 변수
#         self.color = color
#
#     def pring_info(self): # 인스턴스 메서드 정의
#         print(self.shape)
#         print(self.color)
#
# satang = Candy() # 인스턴스(객체) 생성
# satang.set_info('circle', 'brown') # 인스턴스 메서드 호출
# satang.pring_info() # 인스턴스 메서드 호출

# ex) 생성자를 사용한 예제
# class Candy2:
#     def __init__(self, shape, color): # 생성자
#         self.shape = shape
#         self.color = color
#
#     def print_info(self):
#         print(self.shape)
#         print(self.color)
#
# satang2 = Candy2('circle', 'red') # 객체 생성과 동시에 생성자를 호출
# satang2.print_info() # 인스턴스 메서드 호출
#
# satang3 = Candy2('oval', 'pink')
# satang3.print_info()

# ex)
# class USB: # 클래스 정의
#     def __init__(self, capacity): # 생성자
#         self.capacity = capacity # 인스턴스 변수
#
#     def info(self): # 인스턴스 메서드 정의
#         print('{}GB'.format(self.capacity))
#
# usb = USB(64) # 인스턴스(객체) 생성
# usb.info() # 인스턴스 메서드 호출
#
# usb2 = USB(128)
# usb2.info()

# ex) 소멸자 (파이썬은 메모리 관리 알아서 해주기 때문에 굳이 사용할 일 없음)
# class Service:
#     def __init__(self, sefvice): # 생성자
#         self.sevice = sefvice # 인스턴스 변수
#         print('{} Service 가 시작되었습니다.'.format(self.sevice))
#     def __del__(self): # 소멸자
#         print('{} Service가 종료되었습니다.'.format(self.sevice))
#
# s = Service('길 안내') # 인스턴스(객체) 생성
# del s                 # 인스턴스(객체) 삭제

# 클래스 변수
#     클래스 안에서 공간이 할당된 변수
#     여러 인스턴스(객체)가 클래스 변수 공간을 함께 사용

# ex)
# class Car: # 클래스 정의
#     count = 0 #  클래스 변수 정의(0으로 초깃값을 줬다)
#
#     def __init__(self, name, speed): # 생성자
#         self.name = name # 인스턴스 변수
#         self.speed = speed # 인스턴스 변수
#         Car.count += 1 # 클래스 변수를 1 증가시킨다
#
#     def info(self): # 인스턴스 메서드 정의
#         print(f'{self.name}의 현재 속도 : {self.speed}km')
#         print(f'생산된 자동차 수 : {Car.count}대')
#         print('--------------------------------')
#
# car1 = Car('붕붕카', 0) # 인스턴스(객체) 생성(생성자도 호출)
# car1.info() # 인스턴스 메서드 호출
#
# car2 = Car('빵빵카', 30) # 인스턴스(객체) 생성
# car2.info()
#
# car3 = Car('띠띠카', 60) # 인스턴스(객체) 생성
# car3.info()
#
# car4 = Car('드릉카', 90) # 인스턴스(객체) 생성
# car4.info()

# 클래스 메서드
#     인스턴스 또는 클래스로 호출
#     생성된 인스턴스가 없어도 호출 가능
#     @classmethod 데코레이터를 표시하고 작성
#     매개변수 self 사용하지 않고 cls를 사용

# ex)
# class Korean: # 클래스 정의
#     country = '한국' # 클래스 변수('한국'으로 초기화)
#
#     @classmethod
#     def trip(cls, country): # 클래스 메서드 정의
#         if cls.country == country:
#             print('국내여행입니다.')
#         else:
#             print('해외여행입니다.')
#
# Korean.trip('한국')  # 객체없이 호출 가능(클래스 메서드의 특징)
# Korean.trip('미국')

# ex)
# class Bag: # 클래스 정의
#     count = 0 # 가방 개수 (클래스 변수)
#
#     def __init__(self): # 생성자 (객체가 생성될 때 자동으로 호출되는 함수)
#         Bag.count += 1 # 생성자 호출될 때마다 1씩 증가(객체 생성시 1씩 증가)
#
#     @classmethod
#     def sell(cls): # 클래스 메서드 정의
#         cls.count -= 1 # 호출될 때 1씩 감소 (가방 팔릴때마다 1씩 감소)
#
#     @classmethod
#     def remain_bag(cls): # 클래스 메서드 정의
#         return cls.count # 가방 개수를 알려줌(반환함)
#
# print('현재 가방 : {}개'.format(Bag.remain_bag()))
# bag1 = Bag() # 인스턴스(객체) 생성
# bag2 = Bag()
# bag3 = Bag()
# print('현재 가방 : {}개'.format(Bag.remain_bag()))
# bag1.sell() # Bag.sell()
# bag2.sell()
# print('현재 가방 : {}개'.format(Bag.remain_bag()))

# 클래스 상속
# ex)
# class Person: # 슈퍼 클래스(부모 클래스)
#     def __init__(self, name): # 생성자
#         self.name = name
#
#     def eat(self, food): # 인스턴스 메서드 정의
#         print(f'{self.name}가 {food}를 먹습니다.')
#
# class Student(Person): # 서브 클래스(자식 클래스)
#     def __init__(self, name, school): # 생성자
#         super().__init__(name) # 슈퍼(부모) 클래스의 생성자를 호출
#         self.school = school
#
#     def study(self): # 인스턴스 메서드 정의
#         print('f{self.name}는 {self.school}에서 공부를 합니다.')
#
# potter = Student('해리포터', '호그와트')
# potter.eat('젤리') # 상속받은 메서드 호출
# potter.study() # 인스턴스 메서드 호출

# ex)
# class Coffee: # 슈퍼 클래스(부모 클래스)
#     def __init__(self, bean): # 생성자
#         self.bean = bean
#
#     def coffee_info(self): # 인스턴스 메서드 정의
#         print('원두 : {}'.format(self.bean))
#
# class Espresso(Coffee): # 서브 클래스(자식 클래스)
#     def __init__(self, bean, water): # 생성자
#         super().__init__(bean) # 부모의 생성자를 호출
#         self.water = water
#
#     def espresso_info(self): # 인스턴스 메서드 정의
#         super().coffee_info() # 부모 클래스의 메서드를 호출
#         print('물: {}ml'.format(self.water))
#
# coffee = Espresso('콜롬비아', 30) # 인스턴스(객체) 생성
# coffee.espresso_info() # 인스턴스 메서드 호출
#
# coffee2 = Espresso('예가체프', 50)
# coffee2.espresso_info()

#########################################################
# 클래스 문제)
# 친구의 이름과 전화번호 정보를 담을 수 있는 클래스 Friend를 만들자
# 생성자, show_info() 인스턴스 메서드를 포함한다
# show_info()는 print를 하는 역할을 한다
# 인스턴스 변수 이름은 자유롭게 한다
# [화면실행결과]
# 이름 : 라이언
# 전화번호 : 010-1234-5678
# -----------------------
# 이름 : 춘식이
# 전화번호 : 010-1111-2222
# -----------------------
#
# class Friend:
#     def __init__(self, name, tel):
#         self.name = name
#         self.tel = tel
#
#     def show_info(self):
#         print('이름: {}'.format(self.name))
#         print('전화번호: {}'.format(self.tel))
#         print('-----------------------')
#
# friend1 = Friend('라이언', '010-1234-5678')
# friend2 = Friend('춘식이', '010-1111-2222')
# friend1.show_info()
# friend2.show_info()