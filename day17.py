# 예외 처리
# 예외 종류
# SyntaxError : 잘못된 문법
#
#     print('test)
#     print('Hello'))

# NameError : 참조 변수 없음(변수 이름이 틀렸다)
#
#     a = 10
#     b = 15
#     print(c)
#
# ZeroDivisionError : 0 나누기 에러
#
#     print(10 / 0)
#
# IndexError : 인덱스 범위 오버
#
#     x = [1, 2, 3]
#     print(x[3])
#
# KeyError: 잘못된 키(key)
#
#     dic = {'name':'홍길동', 'age':20}
#     print(dic['hobby']) # 에러
#     print(dic.get('hobby')) # 에러 안나고 None을 반환
#
# ValueError : 참조 값이 없을 때
#
#     x = [1, 4, 10]
#     x.remove(100) # 값 100을 지워라 -> 오류

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
#
#    x = [1, 2] # 리스트
#    y = (1, 2) # 튜플
#    z = 'Hello' # 문자열
#    print(x + y + z) # 서로 다른 자료형이기 때문에 성립 안 됨

# 모든 예외를 처리하는 방식 (try ~ except)
# ex)
# try:
#     num = int(input('정수를 입력하세요: '))
#     print('원의 반지름: {}'.format(num))
#     print('원의 둘레: {}'.format(num * 3.14 * 2))
#     print('원의 넓이: {}'.format(num * num * 3.14))
# except: # 정수를 입력하지 않으면 에러가 뜨지 않고, 이 메세지가 출력
#     print('정수를 입력하지 않았습니다!')

# ex)
# try:
#     height = input('키를 입력하세요 >>> ') # 문자열 형태로 입력받음
#     height = round(height) # 반올림(예외 발생)
#     print('입력하신 키는 {}cm로 처리됩니다.'.format(height))
# except:
#     print('예외가 발생했습니다.')

# 특정 예외만 처리하는 방식
# ex)
# try:
#     a = int('제수를 입력하세요: ')
#     b = int('피제수를 입력하세요: ')
#     print('{} / {} = {}'.format(a, b, a / b))
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except ValueError:
#     print('정수만 이력할 수 있습니다.')
# except Exception:
#     print('알 수 없는 예외가 발생했습니다.')

# 예외 메시지 처리하기
# ex)
# a = [10, 20, 30, 40, 50]
#
# try:
#     print(a[10])
# except IndexError as e:
#     print(e) # 예외 메시지 출력

# else문과 finally문
#
#   else: 예외 발생하지 않고,정상적으로 처리될 때 실행되는 구문
#   finally: 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문
#            예외 발생 여부와 관계없이 무조건 실행해야 할 경우에 사용
#
#   try는 단독으로는 사용할 수 없으며, 반드시 except 또는 finally와 함께 사용해야 함
#   else는 반드시 except 뒤에 사용해야 함

# ex)
# try:
#     num = int(input('정수를 입력하세요: '))
# except:
#     print('정수를 입력하지 않았습니다.')
# else: # 예외가 발생하지 않았을 때 (정상적으로 작동)
#     print('원의 반지름 : {}'.format(num))
#     print('원의 둘레: {}'.format(num * 3.14 * 2))
#     print('원의 넓이: {}'.format(num * num * 3.14))
# finally: # 무조건 실행
#     print('프로그램이 종료되었습니다.')

# ex)
# try: # 예외가 발생할 가능성이 있는 코드
#     filename = input('열고자 하는 파일명을 입력하세요 >>> ')
#     file = open(filename,'rt') # 파일 열기
# except FileNotFoundError: # 예외가 발생했을 때 실행
#     print('{} 파일이 존재하지 않습니다.'.format(filename))
# else: # 예외가 발생하지 않았을 때 (정상적)
#     buffer = file.read()
#     print(buffer)
#     file.close() # 파일 닫기
# finally:
#     print('프로그램을 종료합니다!')

# 강제로 예외 발생시키기(raise)
#
#     예외를 강제로 발생시킴
#     1. 프로그램 개발 단계에서 아직 구현되지 않은 부분에 일부러
#        예외를 발생시켜 잊어버리지 않도록 하는 경우에 활용
#     2. 파이썬이 예외로 인식하지 못하지만 실제로 예외인 경우(ex. 나이)

# ex)
# num = int(input('정수를 입력하세요: '))
# if num > 0:
#     raise '아직 구현되지 않은 부분입니다!' # 임시
# else:
#     print('0 또는 음수입니다.')

# ex)
# try:
#     score = int(input('점수를 입력하세요 >>> '))
#     if score < 0 or score > 100: # 점수 범위를 벗어났다면
#         raise Exception('점수는 0~100사이 입니다.') # 강제로 예외 발생
#
# except Exception as e:
#     print(e) # 예외 메세지 출력
#
# else: # 정상적인 경우
#     if score >= 80:
#         print('{}점은 합격입니다.'.format(score))
#     else:
#         print('{}점은 불합격입니다.'.format(score))

# pass
#
#     예외 발생하면 바로 처리해야 하지만 크게 중요한 부분이 아닐 경우
#     프로그램의 강제 종료를 막는 목적으로 pass를 사용함
#
#     <형식>
#     try:
#         예외가 발생할 가능성이 있는 코드
#     except:
#         pass
#
# ex)
# li = ['52', '123', '29', '파이썬', '111']
# li_num = [] # 숫자만 담을 빈 리스트를 생성
#
# for i in li: # li에 있는 값들을 하나씩 꺼내어 반복
#     try:
#         result = int(i) # 정수형인 숫자로 변환
#         li_num.append(result) # 예외없이 통과한 값만 li_num에 추가
#     except:
#         pass # 예외 발생하면 그냥 넘어감
#
# print(li_num)

# 사용자 예외 클래스
# ex)
# class NameError(Exception): # Exception 클래스 상속받음
#     def __init__(self, message):
#         super().__init__(message)
#
# try:
#     name = input('이름을 입력하세요 >>> ')
#     if len(name) < 2 or len(name) > 6: # 강제로 예외 발생
#         raise NameError('이름은 2~6자 사이로 입력해 주세요.')
# except NameError as e:
#     print(e)
# else:
#     print('입력된 이름은 {}입니다.'.format(name))

############################################################################
# 예외처리 문제)
# 나이를 입력받아 정상적인 정수이면 나이를 출력하고, 그 외의 경우이면 예외처리를 하는 코드를 작성해 보자.
# try, except, else, finally 사용
# [화면실행결과1- 정상적]
# 나이를 입력하세요 : 20
# 입력하신 나이는 20살입니다.
# 프로그램을 종료합니다.

# [화면실행결과1- 비정상적(예외)]
# 나이를 입력하세요 : 스물
# 입력이 잘못되었습니다.
# 프로그램을 종료합니다.
#
# try:
#     age = int(input('나이를 입력하세요: '))
# except ValueError:
#     print('입력이 잘못되었습니다.')
# else:
#     print('입력하신 나이는 {}살 입니다.'.format(age))
# finally:
#     print('프로그램을 종료합니다.')
