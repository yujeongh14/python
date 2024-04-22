# 클래스와 객체 1
# 객체 지향 프로그래밍 (Object-Oriented Programming, OOP)
#
#     문제를 작게 나누에 객체(object)를 만들고 객체를 조합해서 문제를 해결하는 방식
#     복잡한 문제를 처리하는데 유용하며, 기능을 개선하고 발전시킬 때도 해당 클래스만 수정하면 되므로, 유지보수에 효율적

#     클래스(class) : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도
#                    과자틀, 붕어빵 틀에 비유
#     객체(object) : 붕어빵 틀에서 만들어낸 붕어빵에 비유
#                    각각의 개체마다 고유의 특성을 가진다
#                    파이썬에서는 문자, 정수, 실수, 함수 등 모두 객체이다
#
#     인스턴스(instance) : 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때 사용
#                         클래스와 연관지어 객체를 말할 때 인스턴스라고 한다
#
#     메서드(method) : 클래스 안에서 구현된 함수
#
#     <형식>
#     class 클래스이름: # 파이썬에서는 클래스이름을 주로 대문자로 시작
#       def 메서드이름(self, 매개변수):
#           # self -> 메서드를 호출한 객체가 자동으로 전달되는 매개변수
#           self.속성 = 값 # 인스턴스 변수
#
#     인스턴스이름 = 클래스이름() # 인스턴스(객체) 생성 -> 붕어빵 굽는 행위
#     인스턴스이름.메서드이름() # 메서드 (함수) 호출

# ex)
# class Person: # 클래스 정의
#     def who_am_i(self, name, age, tel, address): # 인스턴스 메서드
#         self.name = name # 인스턴스 변수
#         self.age = age
#         self.tel = tel
#         self.address = address
#
# boy = Person() # boy 인스턴스(객체) 생성
# boy.who_am_i('john', 15, '123-1234', 'toronto') # 메서드(함수) 호출
# print(boy)
# print(boy.name)
# print(boy.age)
# print(boy.tel)
# print(boy.address)
#
# boy2 = Person() # boy2 인스턴스(객체) 생성 -> 붕어빵 구움
# boy2.who_am_i('ryan', 20, '111-1111', 'Daegu') # 인스턴스 메서드(함수) 호출
# print(boy2)
# print(boy2.name)
# print(boy2.age)
# print(boy2.tel)
# print(boy2.address)

# 예제)
# class Computer: # 클래스 정의
#     def set_spec(self, cpu, ram, vga, ssd): # 인스턴스 메서드 정의
#         self.cpu = cpu # 인스턴스 변수
#         self.ram = ram
#         self.vga = vga
#         self.ssd = ssd
#
#     def hardware_info(self): # 인스턴스 메서드 정의
#         print('CPU = {}'.format(self.cpu))
#         print('RAM = {}'.format(self.ram))
#         print('VGA = {}'.format(self.vga))
#         print('SSD = {}'.format(self.ssd))
#         print('-------------------')
#
# desktop = Computer() # 인스턴스(객체) 생성 -> 붕어빵 구움
# desktop.set_spec('i7', '16GB', 'GTX1060', '512GB') # 인스턴스 메서드 호출
# desktop.hardware_info() # 인스턴스 메서드 호출
# print(desktop)
#
# notebook = Computer() # 인스턴스(객체) 생성 -> 붕어빵 구움
# notebook.set_spec('i5', '8GB', 'MX300', '256GB') # 인스턴스 메서드 호출
# notebook.hardware_info() # 인스턴스 메서드 호출
# print(notebook)

# 예제)
# class Calculator: # 클래스 정의
#     def input_expr(self): # 인스턴스 메서드 정의
#         expr = input('수식을 입력하세요 >>> ') # 지역변수
#         self.expr = expr # 인스턴스 변수로 다시 저장
#
#     def calculate(self): # 인스턴스 메서드 정의
#         return eval(self.expr) # eval(): 문자열로 된 수식을 계산해주는 함수
#
# calc = Calculator() # 인스턴스(객체) 생성 -> 붕어빵 구움
# calc.input_expr() # 인스턴스 메서드 호출
# print('수식 결과는 {}입니다.'.format(calc.calculate())) # 인스턴스 메서드 호출

# 예제)
# class Book:
#     def set_info(self, title, author):
#         self.title = title      # 책 제목
#         self.author = author    # 저자 정보
#
#     def print_info(self):
#         print('책 제목: {}'.format(self.title))
#         print('책 저자: {}'.format(self.author))
#         print('-----------------')
#
# 인스턴스(객체) 생성 -> 책 생성
# book1 = Book()
# book2 = Book()
# book3 = Book()
# book4 = Book()
# print(book1, book2, book3, book4, sep='\n')
#
# 제목과 저자 정보를 저장
# book1.set_info('파이썬', '민경태')
# book2.set_info('어린왕자', '생택쥐페리')
# book3.set_info('오늘부터 개발자', '김병욱')
# book4.set_info('트렌드코리아2024', '김난도')
#
# book_list = [book1, book2, book3, book4]
# for book in book_list:
#     book.print_info() # 출력 메서드 호출

##########################################
# 응용 문제)
# class Watch:
#     def set_time(self): # 인스턴스 메서드 정의
#         now = input('시간을 입력하세요 >>> ') # ex) 12:00:00
#         hms = now.split(':') # : (콜론)으로 분리 ex)['12', '00', '00']
#         self.hour = int(hms[0]) # 인스턴스 변수
#         self.minute = int(hms[1]) # 인스턴스 변수
#         self.second = int(hms[2]) # 인스턴스 변수
#
#     def add_hour(self, hour):
#         if hour <= 0:
#             return # 함수 종료
#         self.hour += hour
#         self.hour %= 24
#
#     def add_minute(self, minute):
#         if minute <= 0:
#             return
#         self.minute += minute
#         self.add_hour(self.minute // 60)
#         self.minute %= 60
#
#     def add_second(self, second):
#         if second <= 0:
#             return
#         self.second += second
#         self.add_minute(self.second // 60)
#         self.second %= 60
#
#     def see(self): # 출력 메서드
#         print('계산된 시간은 {}시 {}분 {}초입니다.'.format(self.hour, self.minute, self.second))
#
# watch = Watch() # 인스턴스(객체) 생성
# watch.set_time() # 인스턴스 메서드 호출
# watch.add_hour(int(input('계산할 시간을 입력하세요 >>> ')))
# watch.add_minute(int(input('계산할 분을 입력하세요 >>> ')))
# watch.add_second(int(input('계산할 초를 입력하세요 >>> ')))
# watch.see() # 출력 메서드 호출(인스턴스 메서드 호출)
##########################################
# 문제)
# 친구의 이름과 전화번호 정보를 담을 수 있는 클래스 Friend를 만들어보자
# set_info(), show_info() 인스턴스 메서드를 포함한다
# 인스턴스 변수 : 이름, 전화번호 (변수명은 마음대로)
# [화면실행결과]
# 이름 : 라이언
# 전화번호 : 010-1234-5678
# ------------------------
# 이름 : 춘식이
# 전화번호 : 010-1111-2222

# class Friend():
#     def set_info(self, name, tel):
#         self.name = name
#         self.tel = tel
#
#     def show_info(self):
#         print('이름 : {}'.format(self.name))
#         print('전화번호 : {}'.format(self.tel))
#         print('-------------------')
#
# 객체(인스턴스)생성 -> 붕어빵 구움 -> 친구 생성
# friend1 = Friend()
# friend2 = Friend()
#
# 인스턴스 메서드 호출(데이터를 저장하는 역할을 하는 메서드 호출)
# friend1.set_info('라이언', '010-1234-5678')
# friend2.set_info('춘식이', '010-1111-2222')
#
# 인스턴스 메서드 호출(출력해주는 메서드 호출)
# friend1.show_info()
# friend2.show_info()