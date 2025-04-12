import time

# 사용자별 활동 로그 저장소 (딕셔너리 안에 리스트)
activity_logs = {}

# 사용자 활동 기록 함수
def log_activity(user_id, action):
    timestamp = time.strftime("%H:%M:%S")
    log = f"[{timestamp}] {action}"

    # 해당 사용자의 로그 리스트가 없으면 만들기
    if user_id not in activity_logs:
        activity_logs[user_id] = []

    # 활동 로그 추가
    activity_logs[user_id].append(log)
    print(f"{user_id} 활동 기록됨: {log}")

# 전체 로그 출력 함수
def show_logs():
    print("\n=== 사용자별 활동 로그 ===")
    for user_id, logs in activity_logs.items():
        print(f"{user_id}의 로그:")
        for log in logs:
            print("  -", log)
        print()

# 테스트 시나리오
log_activity("neo", "login")
time.sleep(1)
log_activity("neo", "visit /home")
time.sleep(1)
log_activity("neo", "download secret.zip")
time.sleep(1)
log_activity("neo", "logout")

log_activity("admin", "login")
log_activity("admin", "delete user")

show_logs()