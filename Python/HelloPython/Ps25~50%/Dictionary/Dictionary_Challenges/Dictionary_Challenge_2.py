#1. 서버 정보 딕셔너리 만들기
server = {
    "ip": "192.168.0.1",
    "port": "8080",
    "status": "active"
}
print(server)

#2. 딕셔너리에서 특정 값 출력
print(server["ip"])
print(server["status"])

#3. 서버 상태 변경
server["status"] = "inactive"
print(server)

#4. 새 키 추가
server["location"] = "Seoul"
print(server)

#5. 딕셔너리 반복 출력
for ser in server:
    print(ser)

#6. 딕셔너리를 활용한 포트 스캔 결과 표시
ports = {
    22: "open",
    80: "open",
    443: "closed",
    3306: "closed"
}

for port in ports:
    if port == "open":
        print(port)