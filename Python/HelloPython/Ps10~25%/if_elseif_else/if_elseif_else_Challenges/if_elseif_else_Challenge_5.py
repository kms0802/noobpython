id = input("아이디를 입력하세요:")

if id == "admin":
    print("관리자 로그인")
elif id == "guest":
    print("손님 로그인")
else:
    print("알 수 없는 사용자")
