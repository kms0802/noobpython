id = input("아이디를 입력하세요:")

if id == "admin" or id == "guest":
    print("접속 허용")
else:
    print("접속 거부")