passwd = ""

while passwd != "admin123":
    passwd = input("패스워드 입력:")
    if passwd == "admin123":
        print("관리자 로그인")
        break