# 내장 함수
# 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수가 내장되어있다
# 문자열 내장 함수
# 모든 문자는 자신만의 코드 값을 가지고 있다.
# 이를 문자 코드라고 하는데 미국 표준 코드인 아스키코드나 국제 표준 코드인 유니코드 등이 있다.
# chr()함수는 특정 문자의 유니코드 값을 전달하면 해당 유니코드 값을 가진 문자를 반환하는 함수입니다.

# chr() : 유니코드를 문자로 변환
# print(chr(48))
# print(chr(49))
# print(chr(65))
# print(chr(66))
# print(chr(97))
# print(chr(98))
#
# # ord() : 문자를 유니코드로 변환
# print(ord('0'))
# print(ord('1'))
# print(ord('A'))
# print(ord('B'))
# print(ord('a'))
# print(ord('b'))
#
# # eval() : 문자열로 된 값을 계산
# print('100 + 200')
# print(eval('100 + 200'))
# print(eval('min(1, 2, 3)')) # min(): 최소값
#
# # 예제) 문자열로 입력받은 계산식을 연산하기
# expr = input('계산식을 입력하세요 >>> ')
# result = eval(expr)
# print(result)
# print(type(result))
# print(expr + '=' + str(result))
#
# # 숫자 내장 함수
# abs() : 절대값
# print(abs(10))
# print(abs(-10))


#
# # divmod() : 몫과 나머지
# print(divmod(10, 3)) # 결과는 튜플형식
# d, m = divmod(10, 3)
# print(d)
# print(m)
#
# # max() : 최댓값
# print(max(1, 2))
# li = [10, 8, 4, 6, 2]
# print(max(li))
#
# # min() : 최솟값
# print(min(1, 10))
# print(min(li))
#
# # pow() : 거듭제곱 ( ** 연산자 )
# print(pow(10, 2)) # 10을 두 번 곱하다
# print(pow(10, 3)) # 10을 세 번 곱하다
# print(pow(10, -2)) # 10을 두 번 곱하다
#
# # round() : 반올림
# print(round(1.5)) # 일의 자리까지
# print(round(1.4))
# print(round(1.55, 1)) # 소수 첫 째자리 까지
#
# # sum() : 합계
# li = [1, 2, 3, 4, 5]
# print(sum(li))
#
# # 예제) divmod를 사용해서 빵을 몇 개 샀고 얼마가 남았는지 확인하기
# money = 10000
# price = 3000 # 빵 1개의 가격
# result = divmod(money, price)
# print(result)
# print('빵을 {}개 사고 {}원이 남았습니다.'.format(result[0], result[1]))
#
# # 시퀀스 내장 함수
# # enumerate()
#
#     # <형식>
#     # for 인덱스번호, 값 in enumerate(리스트명):
#     #     수행할 코드
#
# # 예제)
# li = [10, 20, 30]
# for i in li:
#     print(i) # 리스트의 값(요소)만 출력
#
# for item in enumerate(li):
#     print(item) # 튜플로 묶어져서 나온다
# for index, value in enumerate(li):
#     print(f'{index}번째 : {value}')
#
# print()
#
# for i, v in enumerate(li, start=1): # 인덱스 시작번호를 1로 정함
#     print(f'{i}번째 : {v}')
#
# # len() : 길이(항목 수)
# li = ['a', 'b', 'c', 'd']
# print(len(li))
#
# ch = 'Hello'
# print(len(ch))
#
# d = {'a':'apple', 'b':'banana'}
# print(len(d))
#
# print(len(range(10))) # 0~9 : 10개
# print(len(range(1, 10))) # 1~9 : 9개
#
# # 예제) 총점과 평균 구하기
# score = [70, 60, 55, 75, 95] # 학생 점수 리스트
# total = 0 # 총점을 0으로 초기화
#
# for i, v in enumerate(score, start=1):
#    print(f'{i}번째 학생 점수 : {v}')
#    total += v
#
# print(f'총점 : {total}')
# avg = total / len(score) # 리스트 개수로 나누어 평균 구한다
# print(f'평균 : {avg}')
#
# # sorted() : 정렬
# my_list = [6, 3, 1, 2, 5, 4]
# sorted_list = sorted(my_list)
# reverse_list = sorted(my_list, reverse=True)
# print(f'원본 : {my_list}')
# print(f'정렬 후 (오름차순) : {sorted_list}')
# print(f'정렬 후 (내림차순) : {reverse_list}')
#
# # zip() : 튜플로 묶기
# names = ['james', 'emily', 'amanda']
# scores = [60, 70, 80]
# for student in zip(names, scores):
#     print(student)
#
# for name, score in zip(names, scores):
#     print(f'{name}의 점수는 {score}점입니다.')
#
# # 예제) 1~12월까지 해당 달에 몇일 까지 있는지 표현해보기
# months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# for month, day in enumerate(months):
#    print('{}월={}일'.format(month+1, day))
#
# #######################################################
# # 문제1) 시작값과 끝값, 증값값까지 사용자에게 정수를 입력받아
# # 시작값과 끝값까지의 합계 구하기 (for, range()이용)
# # [화면실행결과]
# # 시작값을 입력하시오 : 3
# # 끝값을 입력하시오 : 300
# # 증감값을 입력하시오 : 3
# # 3에서 300까지 3씩 증가시킨 값의 합계 : 15150
#
# start = int(input('시작값을 입력하시오 : '))
# end = int(input('끝값을 입력하시오 : '))
# increase = int(input('증감값을 입력하시오 : '))
# total = 0
#
# for i in range(start, end+1, increase):
#     total += i
# print(f'{start}에서 {end}까지 증가시킨 값의 합계 : {total}')

print('123'.isdigit()) # True
print('python123'.isdigit()) # False