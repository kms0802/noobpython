#1. 사용자 계정 딕셔너리 만들기
infos = {
    "username" : "hacker007",
    "rank" : "elite",
    "attempts" : 3
}
print(infos)

#2. 로그인 시도 횟수 증가시키기
infos["attempts"] += 1
print(infos)

#3. 새로운 정보 추가
infos["banned"] = False
print(infos)

#4. 존재하지 않는 키 접근 방지 (get)사용
print(infos.get("email"))
print(infos.get("email", "N/A"))

#5. 딕셔너리 반복 출력
for key, val in infos.items():
    print(key, ":", val)

#6. 악성 코드 감지 결과 출력기
malware = {
    "trojan": "detected",
    "worm": "not found",
    "backdoor": "detected",
    "ransomware": "not found"
}

for key, value in malware.items():
    print(f"{key}: {value}")