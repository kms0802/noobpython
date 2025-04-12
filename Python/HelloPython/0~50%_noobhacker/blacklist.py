blacklist = {"192.168.0.10", "10.0.0.3", "172.16.5.8"}

ip = input("접속 시도한 IP 주소를 입력하세요: ")

if ip in blacklist:
    print("접속 차단: 블랙리스트에 등록된 IP입니다.")
else:
    print("접속 허용")