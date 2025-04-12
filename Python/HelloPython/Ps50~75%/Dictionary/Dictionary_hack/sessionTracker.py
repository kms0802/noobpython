import time

# 사용자 세션 상태 저장용 딕셔너리
sessions = {}

# 사용자 로그인 함수
def login(user_id):
    sessions[user_id] = {
        "active": True,
        "login_time": time.strftime("%H:%M:%S"),
        "last_action": "login"
    }
    print(f"{user_id} 로그인됨")

# 사용자 활동 기록 함수
def update_action(user_id, action):
    if user_id in sessions and sessions[user_id]["active"]:
        sessions[user_id]["last_action"] = action
        print(f"{user_id} 활동 기록: {action}")
    else:
        print(f"{user_id}는 현재 로그인 상태가 아님.")

# 사용자 로그아웃 함수
def logout(user_id):
    if user_id in sessions:
        sessions[user_id]["active"] = False
        sessions[user_id]["last_action"] = "logout"
        print(f"{user_id} 로그아웃됨")

# 텍스트 흐름
login("neo")
time.sleep(1)
update_action("neo", "access /home")
time.sleep(1)
update_action("neo", "download file")
time.sleep(1)
logout("neo")

print("\n=== 현재 세션 정보 ===")
for uid, info in sessions.items():
    print(uid, ":", info)