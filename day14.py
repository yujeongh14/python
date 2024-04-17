# csv 파일입출력
# csv 파일 읽기
# student_list = [] # 최종 결과를 담을 빈 리스트를 만든다
# with open('./Section14/학생명단.csv','rt') as file:
#     file.readline() # 제목 줄 (지워진다)
#     while True:
#         line = file.readline() # 한 줄씩 읽어 line 리스트에 담는다
#         if not line: # 더 이상 라인이 없을때까지 반복
#             break
#         student = line.split(',') # ,로 구분된 것을 분리해서 student에 저장
#         student_list.append(student) # 결과리스트에 분리한 student 저장
# print(student_list)

# 예제2)
# member_list = []
# with open('./Section14/회원명단.csv', 'rt') as file:
#     file.readline() # 제목 줄(삭제)
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         member = line.split(',') # ["강나라", 필라테스, 25일]
#         member[0] = member[0].strip('"') # 양쪽 큰 따옴표 제거 후 다시 담기
#         member_list.append(member)
#
# print(member_list)

# # csv 모듈로 csv 파일 생성하기
# import csv # csv 파일을 쉽게 관리하기 위한 모듈을 불러온다
#
# with open('./Section14/차량관리.csv','wt', newline='') as file:
#     csv_maker = csv.writer(file, delimiter=',' )
#     csv_maker.writerow([1,'08러1234', '2020-10-20, 14:00'])
#     csv_maker.writerow([2,'25다1234', '2020-10-20, 14:10'])
#     csv_maker.writerow([3,'28하1234', '2020-10-20, 14:20'])
#
# print('차량관리.csv 파일이 생성되었습니다.')

# csv 모듈로 csv 파일 읽기
# import csv
#
# with open('./Section14/차량관리.csv', 'rt', newline='') as file:
#     csv_reader = csv.reader(file, delimiter=',', quotechar='"')
#     for line in csv_reader:
#         print(line)
#
# print(csv_reader)

# json 파일입출력
# json 파일 쓰기 (생성)
# 예제)
# import json

# dict_list = [
#     {
#         'name':'james',
#         'age':20,
#         'spec':[175.5, 70.5]
#     },
#     {
#         'name':'alice',
#         'age':21,
#         'spec':[168.5, 60.5]

#     }
# ]
# json_string = json.dumps(dict_list) # json으로 변환(인코딩)

# with open('./Section14/dictList.json', 'wt') as file:
#    file.write(json_string) # json으로 인코딩한 내용을 json파일에 쓴다

# print('dictList.json 파일이 생성되었습니다.')

# json 파일 읽기
# import json
#
# with open('./Section14/dictList.json','rt') as file:
#     json_reader = file.read() # 파일 전체 읽어 json_reader에 저장
#     dict_list = json.loads(json_reader) # 파이썬으로 변환
#
# print(dict_list)
#
# for dic in dict_list:
#     print('이름 : {}'.format(dic['name']))
#     print('나이 : {}'.format(dic['age']))
#     print('키 : {}'.format(dic['spec'][0]))
#     print('몸무게 : {}'.format(dic['spec'][1]))
#     print('----------------')

# 응용예제 1) 파일을 복사하기. but txt확장자 외의 파일은 복사할 수 없는 파일이라고 오류 출력하기
# while True:
#     filename = input('복사할 파일명을 입력하세요 >>> ')
#     extname = filename[filename.rfind('.')+1:] # 확장자를 추출
#     if extname != 'txt':
#         print('복사할 수 없는 파일입니다.')
#     else:
#         break
#
# with open(filename, 'rt')as source: # 원본
#     with open('복사본-'+ filename, 'wt')as copy:
#         while True:
#             buffer = source.read(1) # 1바이트씩 읽어 buffer에 담는다
#             if not buffer:
#                 break
#             copy.write(buffer)
# print('복사본-'+filename+'파일이 생성되었습니다.')

# 응용예제 2) 총 cctv 개수 구하기
# import csv
#
# with open('./Section14/cctv.csv','rt') as csvfile:
#     buffer = csv.reader(csvfile,delimiter=',', quotechar='"')
#     totalcctv = 0 # cctv 개수
#     for i, line in enumerate(buffer):
#         if i != 0: # 제목 줄은 제외
#             totalcctv += int(line[6])
#
# print('대구광역시 달서구에 설치된 cctv는 총 {}입니다.'.format(totalcctv))

# 응용예제 3)
# import json
#
# with open('./Section14/cctv.json','rt', encoding='utf-8') as jsonfile:
#     buffer = jsonfile.read()
#     cctv_list = json.loads(buffer) # 파이썬으로 변환
#     cctv_purpose = set() # 결과를 담을 빈 세트를 생성 (중복 제외하기 위해)
#     for place in cctv_list:
#         cctv_purpose.add(place['설치목적구분']) # 세트에 추가
# print(cctv_purpose)