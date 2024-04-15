# 파일 입출력
# 파일 생성하고 문자열 쓰기
#
#     <형식> (기본 문법)
#     파일객체명 = open('파일 이름', 'w') # 파일 열기(텍스트일 경우 w뒤에 오는 t는 생략가능)
#     파일객체명.write('문자열')
#     파일객체명.write(str(숫자)) # write함수는 문자열 형식만 가능
#     파일객체명.close() # 파일 닫기
#
#     <형식> (리스트 문법)
#     리스트명 = [값1, 값2, 값3,...]
#     파일객체명 = open('파일 이름', 'w')
#     파일객체명.writelines(리스트명)
#     파일객체명.close()

# ex)
# file = open('Hello.txt','w') # 파일 열기(쓰기 모드로)
# file.write('Hello, world!')
# file.close() # 파일 닫기

# ex) for문을 이용해서 파일에 문자열 쓰기
# file = open('Hello.txt', 'w')
# 상대 경로 : 현재 폴더를 기준으로 ./(현재 폴더),  ../(상위폴더)
# 절대 경로 : 'C:\python\python'
# 예를 들어 c드라이브 안 a라는 폴더에 hello.txt를 생성(절대 경로)
# 'c:/a/hello.txt'
# 'c:\\a\\hello.txt' --> /, \ 둘 다 사용 가능

# for i in range(1, 11):
#     data = f'{i}번째 줄입니다.\n' # \n : 엔터
#     file.write(data) # write 함수는 엔터기능이 없다.
#
# file.close()  # 파일 닫기
#
# # ex) for문을 이용하여 파일에 새로운 내용을 추가하기
# file = open('Hello.txt','a') # 파일 열기(추가 모드로)
#
# for i in range(11, 21):
#     data = f'{i}번째 줄입니다~~~~~~~~!!\n'
#     file.write(data)
#
# file.close()

# 파일에서 문자열 읽기
#
#     <형식>
#     파일객체명 = open('파일 이름', 'r')
#     변수명 = 파일객체명.read()
#     파일객체명.close()
#
#     print(변수명) # 화면으로 보고싶을 때 사용

# ex)
# file = open('Hello.txt','r') # 파일 열기 (읽기 모드로)
# temp = file.read() # 읽을 내용을 temp 변수에 담았다
# file.close() # 파일 닫기
#
# print(temp)

# 파일에서 여러 줄을 리스트로 각각 읽기
#
#     <형식>
#     파일객체명 = open('파일 이름', 'r')
#     리스트명 = 파일객체명.readlines()
#     파일객체명.close()
#
#     print(리스트명) # 화면에서 보고 싶을 때 사용

# ex)
# file = open('Hello.txt','r')
# lines = file.readlines() # 파일에서 읽은 내용을 리스트형식으로 저장
# file.close()
#
# print(lines)
# print(lines[3])
#
# for i in lines:
#     print(i, end='') # print 함수에 있는 엔터 기능을 없앤다

# with문과 함께 파일 입출력 하기
#
#     파일을 열면 항상 close 해주어야 하는 불편함을 덜어주는 기능
#
#     <형식>
#     with open('파일 이름', '파일 열기 모드') as 파일객체명:
#         수행할 코드

# ex)
# li = ['hell0~\n', 'world!\n', 'hi\n', 'python!!\n']
# with open('file.txt','w') as f: # 파일 열기(쓰기 모드로)
#     f.writelines(li) # 리스트를 파일에 쓸 때
#     f.write('ㅋㅋㅋㅋㅋ\n')
#     f.write('파이썬 재미있어!\n')
#
# with open('file.txt','r') as f: # 파일 열기(읽기 모드로)
#     temp = f.read() # 파일에 내용을 모두 읽어 temp 변수에 담았다
#
# print(temp)

# 예제)
# import time
#
# file = open(time.strftime('%Y-%m-%d') + '.txt', 'at') # 날짜의 형식 지정(파일명)
# while True:
#     schedule = input('오늘의 스케쥴을 입력하세요 >>> ')
#     if not schedule: # 스케쥴이 없다면(아무것도 입력 안되었다면)
#         break # 반복문을 종료한다
#     file.write(schedule + '\n') # 스케쥴 뒤에 엔터 삽입
# file.close() # 파일 닫기

# 예제) 파일을 읽어서 '꿀'이란 글자가 몇 개인지 세아려 보자
# file = open('엄마돼지아기돼지.txt','r') # 파일 열기(읽기모드)
#
# line_list = file.readlines() # 전체 글을 저장할 리스트
#
# count = 0 # 꿀의 개수
#
# for line in line_list: # 전체 글 중 하나의 라인을 문자열 line 변수에 저장
#     for ch in line: # line에 담긴 모둔 문자들을 하나씩 ch변수에 저장
#         if ch == '꿀': # 꿀과 같다면
#             count += 1 # 개수 증가
#
# file.close() # 파일 닫기
# print('꿀은 전체 {}번 나타납니다.'.format(count))

# 파일 입출력의 활용
# 파일 복사
# 예제)
# buffer_size = 1024 # 한번에 읽어들이는 데이터의 크기(1kb == 1024byte)
# with open('./Section14/code.mp4', 'rb') as source : # 동영상을 바이너리 모드로 읽는다 # 텍스트는 t 생략해도 되지만 바이너리는 꼭 b추가
#     with open('./Section14/code2.mp4','wb') as copy: # 동영상을 바이너리 모드로 쓴다
#         while True:
#             buffer = source.read(buffer_size) # buffer_size만큼 읽어 변수에 담는다
#             if not buffer:  # 버퍼 변수의 내용이 없다면 중지
#                 break
#             copy.write(buffer) # 버펴 변수의 내용을 복사할 파일에 기록
#
# print('code2.mp4 파일이 복사되었습니다!!')

#############################################################
# 파일 입출력 문제 1)
# 새로운 텍스트 파일 text.txt를 만들고 1부터 10까지의 수가 저장되도록 하여라.
# [text.txt 파일 실행결과]
# 12345678910
#
# 방법1)
# file = open('text.txt','w')
# for i in range(1, 11):
#     file.write(str(i))
# file.close()
#
# 방법2)
# with open('text.txt','w') as f:
#     for i in range(1, 11):
#         f.write(str(i))

# 파일 입출력 문제 2)
# 새로운 텍스트파일 loop.txt를 생성하되, 파일 열기 모드를 추가모드로 한다.
# 1부터 100까지 한 칸씩만 띄우고 모두 한 줄에 저장한다.
# [loop.txt를 열어서 본 결과]
# 숫자 1 숫자 2 숫자 3...숫자 99 숫자 100
#
# 방법1)
# f = open('loop.txt','a')
# for i in range(1, 101):
#     data = f'숫자 {i}'
#     f.write(data)
# f.close()
#
# 방법2)
# with open('loop.txt','a') as f:
#     for i in range(1,101):
#         data = f'숫자 {i}'
#         f.write(data)