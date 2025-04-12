corrent_pw = "admin123"

while True:
    pw = input("비밀번호를 입력하세요: ")

    if pw == corrent_pw:
        print("로그인 성공!")
        break
    else:
        print("비밀번호가 틀렸습니다. 다시 시도하세요.")