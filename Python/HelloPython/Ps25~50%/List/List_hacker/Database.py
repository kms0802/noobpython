# 사용자 정보 데이터베이스 (리스트 안에 딕셔너리)
users = [
    {"id": "admin", "password": "1234"},
    {"id": "user1", "password": "abcd"},
    {"id": "neo", "password": "matrix"}
]

# 로그인 함수
def login(user_id, pw):
    for user in users:
        if user["id"] == user_id and user["password"] == pw:
            return True
    return False

# 사용자 입력
uid = input("아이디: ")
pwd = input("비밀번호: ")

#결과
if login(uid, pwd):
    print("로그인 성공!")
else:
    print("로그인 실패...")