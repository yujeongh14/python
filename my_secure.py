def secure_name(name):
    return name[0] + '**'

def secure_no(no):
    return no[0:8] + '******'

def securte_phone(phone):
    return phone.replace(phone[4:8], '****')

print(__name__)

# 이 파일을 실행할 때만 출력됨
if __name__ == '__main__':
    print(secure_no('김철수'))