ip_logs = [
    "192.168.0.1", "10.0.0.1", "192.168.0.1",
    "10.0.0.2", "10.0.0.1", "8.8.8.8"
]

unipue_ips = set(ip_logs)

print("중복 제거된 IP 목록:")
for ip in unipue_ips:
    print(ip)