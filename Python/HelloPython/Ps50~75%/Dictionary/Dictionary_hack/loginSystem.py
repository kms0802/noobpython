# 사용자 데이터데이스
users = {
    "admin": "1234",
    "neo": "matrix",
    "guest": "guest"
}

# 로그인 시도 횟수 기록
attempts = {
    "admin": 0,
    "neo": 0,
    "guest": 0
}

MAX_TRIES = 3

while True:
    user_id = input("아이디 입력: ")
    
    if user_id not in users:
        print("존재하지 않는 사용자입니다.")
        continue

    # 로그인 시도 3회 초과 시 차단
    if attempts[user_id] >= MAX_TRIES:
        print(f"{user_id} 계정은 로그인 시도 초과로 잠겼습니다.")
        continue
    
    password = input("비밀번호 입력: ")

    if password == users[user_id]:
        print(f"{user_id}님, 로그인 성공!")
        break
    else:
        attempts[user_id] += 1
        print("비밀번호가 틀렸습니다.")
        print(f"현재 시도 횟수: {attempts[user_id]}회")