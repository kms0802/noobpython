#1. 딕셔너리 기본 구조
user = {
    "id" : "admin",
    "password" : "1234",
    "level" : "super"
}

#2. 딕셔너리 값 접근
print(user["id"])
print(user.get("password"))

#3. 값 수정 & 추가
user["level"] = "root"
user["email"] = "admin@web.com"
print(user["level"])
print(user["email"])

#4. 값 삭제
del user["password"]
print(user)

#5. 딕셔너리 반복
for k, v in user.items():
    print(k, "=>", v)

