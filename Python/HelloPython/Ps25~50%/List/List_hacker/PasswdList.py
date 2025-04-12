# 실제 정답 비밀번호
correct_password = "hunter2"

# 비밀번호 후보 리스트
password_list = ["1234", "qwerty", "letmein", "password", "hunter2", "admin"]

#시도
def try_passwords():
    for pw in password_list:
        print("시도 중:", pw)
        if pw == correct_password:
            print("비밀번호 찾음:", pw)
            break
    else:
        print("비밀번호를 찾지 못했습니다.")

try_passwords()