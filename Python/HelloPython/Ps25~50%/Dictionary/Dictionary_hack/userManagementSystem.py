import time

# 사용자 DB와 상태 추적용 딕셔너리
users = {}
login_attempts = {}
activity_logs = {}
MAX_TRIES = 3

# 사용자 등록
def register_user(user_id, pw):
    if user_id in users:
        print("이미 등록된 아이디입니다.")
    else:
        users[user_id] = pw
        login_attempts[user_id] = 0
        activity_logs[user_id] = []
        print(f"{user_id} 등록 완료.")

# 사용자 로그인
def login_user(user_id, pw):
    if user_id not in users:
        print("존재하지 않는 사용자입니다.")
        return False
    
    if login_attempts[user_id] >= MAX_TRIES:
        print("로그인 시도 초과. 계정이 잠겼습니다.")
        return False
    
    if pw == users[user_id]:
        print("로그인 성공!")
        login_attempts[user_id] = 0
        log_activity(user_id, "login")
        return True
    else:
        login_attempts[user_id] = 0
        log_activity(user_id, "login")
        return True

# 활동 기록 함수
def log_activity(user_id, action):
    timestamp = time.strftime("%H:%M:%S")
    log = f"[{timestamp}] {action}"
    activity_logs[user_id].append(log)

# 로그 확인 함수
def show_user_logs(user_id):
    if user_id not in activity_logs:
        print("존재하지 않는 사용자입니다.")
        return
    print(f"\n[{user_id} 활동 로그]")
    for log in activity_logs[user_id]:
        print(" -", log)

#전체 사용자 출력 (관리자 전용)
def show_all_users():
    print("\n=== 전체 사용자 목록 ===")
    for uid in users:
        print("-", uid)

# 테스트 흐름
register_user("neo", "matrix")
register_user("admin", "root")
login_user("neo", "wrong")
login_user("neo", "wrong")
login_user("neo", "matrix")
log_activity("neo", "visit /home")
log_activity("neo", "download confidential.txt")
login_user("admin", "root")
log_activity("admin", "delete user")

show_user_logs("neo")
show_user_logs("admin")
show_all_users()