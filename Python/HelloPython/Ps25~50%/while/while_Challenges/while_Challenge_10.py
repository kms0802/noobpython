passwd = ""

while passwd != "hack123":
    passwd = input("비밀번호를 입력하세요.")
    if passwd == "hack123":
        print("접속 성공")
        break