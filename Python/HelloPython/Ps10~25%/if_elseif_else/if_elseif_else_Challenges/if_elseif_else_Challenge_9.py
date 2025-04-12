email = input("이메일을 입력하세요:")

if "@" in email and "." in email:
    print("유효한 이메일")
else:
    print("잘못된 이메일")