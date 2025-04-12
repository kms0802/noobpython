passwd = input("비밀번호를 입력하세요:")

if len(passwd) >= 8:
    print("사용 가능한 비밀번호입니다.")
else:
    print("비밀번호가 너무 짧습니다.")