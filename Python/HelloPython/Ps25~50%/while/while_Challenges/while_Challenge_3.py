passwd = input("비밀번호를 입력하세요.")

while passwd != "python123":
    passwd = input("비밀번호 입력:")
    if passwd == "python123":
        print("로그인 성공")
        break
