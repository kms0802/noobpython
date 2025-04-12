def check_password(password):
    
    while True:
        password = input("비밀번호를 입력하세요.")
        if len(password) < 8:
            print("비밀번호가 너무 짧습니다. 최소 8자 이상이어야 합니다.")
        elif "@" not in password and "!" not in password:
            print("특수문자(@ 또는 !)가 포함되어야 합니다.")
        else:
            print("사용 가능한 비밀번호입니다.")
            break


check_password(12345678)