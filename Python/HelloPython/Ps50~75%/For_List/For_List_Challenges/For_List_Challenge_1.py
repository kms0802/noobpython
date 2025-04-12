print("1. 리스트 출력하기")
ips = ["192.168.0.1", "10.0.0.1", "8.8.8.8"]
for ip in ips:
    print(ip)
print()

print("2. 딕셔너리 값 출력하기")
users = {
    "user1": "gold",
    "user2": "silver",
    "user3": "bronze"
}
for user, vip in users.items():
    print(user,"의 등급은", vip)
print()

print("3. 튜플 리스트 분석하기")
logins = [("neo", "성공"), ("admin", "실패")]
for user , val in logins:
    print(user ,":", val)
print()

print("4. 집합 중복 제거 출력")
ip_logs = {"192.168.0.1", "10.0.0.1", "192.168.0.1", "10.0.0.1", "8.8.8.8"}
for ip in ip_logs:
    print(ip)
print()

print("5. 딕셔너리 안의 리스트 출력")
activity = {
    "neo": ["login", "download"],
    "admin": ["login", "delete"]
}
for act , val in activity.items():
    print(act, "님의 활동 기록:")
    print()
    for va in val:
        print(va)
        print()