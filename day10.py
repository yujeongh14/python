# 메소드 : 특정 개체가 가지고 있는 함수를 의미
#   문자열 메소드 : format() 메소드
#   .count() : 특정 문자열의 개수
s = '내가 그린 기린 그림은 목 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
print(s.count('기린'))

a = 'best of best'
print(a.count('best'))
print(a.count('best', 5)) # 5번 인덱스부터 시작
print(a.count('best', -7))

# .find(), .index() : 특정 문자열의 위치 반환
b = 'apple'
print(b.find('p')) # 해당 인덱스 번호
print(b.rfind('p')) # 오른쪽에서부터 제일 먼저 나오는 p의 인덱스 번호
print(b.find('z')) # 없는 경우 -1이 출력

print(a.find('best'))
print(a.find('best', 5)) # 지정한 인덱스부터 검색

print(b.index('p'))
# print(b.index('z')) # 없는 경우 에러 발생

# 대소문자 변환 메소드
s = 'BEST of best'
print(s.upper()) # 대문자로 변환
print(s.lower()) # 소문자로 변환
print(s.capitalize()) # 첫 글자만 대문자

# .join() : 합치기
a= '-'.join('python')
print(a)

b = '+'.join(['a', 'b', 'c'])
print(b)

c = ''.join(['x', 'y', 'z'])
print(c)

d = ''.join({'a':'apple', 'b':'banana'})
print(d) # key만 사용

# .split() : 나누기 (리스트 형식으로 결과가 나옴)
a = 'Life is too short'
print(a.split()) # 공백을 기준으로 분리

b = '010-1234-5678'
print(b.split('-')) # -을 기준으로 분리

c = '제임스, 25, 남, 서울'
print(c.split(','))

# .replace() : 바꾸기
print(a.replace('Life', 'Time'))

print(b.replace('-', ''))

# .strip() : 불필요한 문자열 제거
a1 = '     apple'
print(a1)
print(len(a1))

b1 = a1.lstrip() # 왼쪽 공백 제거, rstrip : 오른쪽 공백 제거
print(b1)
print(len(b1))

c1 = '<head<'
print(c1.strip('<')) # 양쪽 < 문자 제거

# 예제) 사용자가 입력한 주민번호 확인
while True:
    p = input('하이픈을 포함하여 전체 주민등록번호를 입력하세요 >>>')
    if p.find('-') != 6: # 하이픈의 위치가 6이 아니라면
        print('하이픈의 위치가 잘못되었습니다.')
        continue
    birthday = p.split('-')[0] # -을 기준으로 분리, 0번 인덱스 값(생년월일)
    print('생년월일은 {}입니다.'.format(birthday))
    break

# 리스트 메소드
# .extend() : 확장
my_list = ['apple', 'banana']
my_list.extend(['cherry', 'mango'])
print(my_list)

# .remove() : 특정 값을 제거
my_list.remove('mango')
print(my_list)
my_list.remove('banana')
print(my_list)

# .clear() : 모든 값을 제거
my_list.clear()
print(my_list)

# 예제)
a_list = ['above', 'cookie','app','about','admin','bisket','aplle','april']
for i, item in enumerate(a_list):
    if item.find('a') == -1: # a가 없는 값은 -1로 반환되므로
        print('{} 제거됩니다.'.format(a_list.pop(i))) # i번째 값을 삭제

print(a_list)

# 세트 메소드 : 집합을 연산할 때 사용
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print('세트 s1 :', s1)
print('세트 s2 :', s2)

# 교집합
print('교집합 :', s1 & s2)
print('교집합 :', s1.intersection(s2))

# 합집합
print('합집합 :', s1 | s2)
print('합집합 :', s1.union(s2))

# 차집합
print('차집합 :', s1 - s2)
print('차집합 :', s2 - s1)
print('차집합 :', s1.difference(s2))
print('차집합 :', s2.difference(s1))

# 사용자 함수

# 함수 용어 정리
#   입력 값 : 인수, 인자, 매개변수, 파라미터
#   출력 값 : 결과값, 반환값, return, 돌려주는 값

# 사용자 함수를 4가지로 나누어서 살펴보자!
# 1. 매개변수(입력 값), 반환 값(출력 값)이 없는 가장 간단한 함수
#    <형식>
#    def 함수이름(): # 함수 정의
#       수행할 코드
#
#    함수이름 () # 함수 호출

# 예제)
def hello():    # 함수 정의
    print('Hello, World!')

hello() # 함수 호출
hello() # 함수 호출
hello() # 함수 호출
# 이거 출력 값 아님? NO! -> 반환값은 저장이 되어야 하는데 이건 저장되는거 아님.잠시 보여주는거임.

# 2. 매개변수(입력값)만 있는 함수
#    <형식>
#    def 함수이름(매개변수, 매개변수2): # 함수 정의
#       수행할 코드
#
#    함수이름 (인수1, 인수2) # 함수 호출

# 예제)
def add(a, b):  # 함수 정의
    print(a + b)

add(1, 2) # 함수 호출
add(10, 20)

x = 6
y = 3
add(x, y)

n1 = int(input('첫 번째 수를 입력하세요 :'))
n2 = int(input('두 번째 수를 입력하세요 :'))
add(n1, n2)

# 3. 반환값(출력값)만 있는 함수
#    <형식>
#    def 함수이름(): # 함수 정의
#       수행할 코드 # 생략 가능
#       return 반환값(출력값)

#   결과변수 = 함수이름() # 함수 호출

# 예제)
def Greetings(): # 함수 정의
    return 'Hello~'

x = Greetings() # 함수 호출 (변수에 담아서 쓰면 여러번 사용 가능)
print(x)

print(Greetings) # 1회성

# 4. 매개변수(입력값), 반환값(출력값)이 1개인 함수
#    <형식>
#    def 함수이름(매개변수, 매개변수2): # 함수 정의
#       수행할 코드 # 생략 가능
#       return 반환값(출력값)

#   결과변수 = 함수이름(인수1, 인수2) # 함수 호출

# 예제)
def plus(a, b): # 함수 정의
    return a + b
n1 = plus(1, 2) # 함수 호출 후 결과값을 n1변수에 담았다
print(n1)       # 실제 담겼는지 print문으로 확인해 본다

n2 = plus(10, 20)
print(n2)

print(plus(100, 200)) # 함수 호출 후 바로 결과를 본다



