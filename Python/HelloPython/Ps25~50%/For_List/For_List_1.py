#1. 리스트 + for문
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("과일:", fruit)

#2. 딕셔너리 + for문
users = {"admin": "1234", "neo": "matrix"}

for user, pw in users.items():
    print(user, "비밀번호:", pw)

#3. 튜플 리스트 + for문
logins = [("neo", "성공"), ("admin", "실패")]

for user, result in logins:
    print(f"{user} 로그인 {result}")

#4. 집합 + for문
unique_ips = {"192.168.0.1", "10.0.0.1", "192.168.0.1"}

for ip in unique_ips:
    print("접속 시도 IP:", ip)

#5.이중for문
activity = {
    "neo": ["login", "download"],
    "admin": ["login", "delete user"]
}

for user, actions in activity.items():
    for act in actions:
        print(f"{user} -> {act}")