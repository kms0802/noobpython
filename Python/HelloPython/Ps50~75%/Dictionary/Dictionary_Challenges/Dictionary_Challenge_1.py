#1. 딕셔너리 생성
user = {
    "id" : "admin",
    "password" : "1234",
    "level" : "root"
}

#2. 값 접근하기
print(user["id"])
print(user["level"])

#3. 값 수정과 추가
user["password"] = "5678"
#user.add("email", "admin@web.com")

#4. 값 삭제하기
#user.remove("password")

#5. 반복 출력하기
for key in user:
    print(key, ":", user)

#6. 사용자 인증 시물레이션
users = {
    "admin": "1234",
    "guest": "guest",
    "neo": "marix"
}

id = input("admin")
pw = input("1234")

for uss in users:
    if id == "admin"