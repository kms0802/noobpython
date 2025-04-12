#1. 딕셔너리 생성
user = {
    "id" : "admin",
    "password" : "1234",
    "level" : "root"
}
print(user)

#2. 값 접근하기
print("ID", user["id"])
print("Level", user["level"])

#3. 값 수정과 추가
user["password"] = "5678"
user["email"] = "admin@web.com"
print(user)

#4. 값 삭제하기
del user["password"]
print(user)

#5. 반복 출력하기
for key in user:
    print(key, ":", user)

#6. 사용자 인증 시물레이션
users = {
    "admin": "1234",
    "guest": "guest",
    "neo": "marix"
}

user_input = input("아이디를 입력하세요: ")

if user_input in users:
    print("접속 허용")
else:
    print("접속 거부")