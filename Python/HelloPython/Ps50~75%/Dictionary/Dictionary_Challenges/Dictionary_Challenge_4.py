#1. 로그인 사용자 정보 저장
session = {
    "user_id": "neo",
    "login_time" : "10:30",
    "is_active" : True
}

print(session)

#2. 로그인 시간 변경
session["login_time"] = "11:00"
print(session)

#3. 세션 만료 처리
session["is_active"] = False
if session["is_active"] == False:
    print("세션 종료")

#4. 키 존재 여부 확인
print(session.get("last_action"))
print(session.get("last_action", "활동 기록 없음"))

#5. 딕셔너리 안에 리스트 저장
session["pages"] = ["/home", "/profile", "/logout"]
print(session)

#6. 사용자 목록 딕셔너리 반복 출력
users = {
    "user1": "1234",
    "admin": "admin123",
    "guest": "guest"
}

for key, val in users.items():
    print(key, ":", val)