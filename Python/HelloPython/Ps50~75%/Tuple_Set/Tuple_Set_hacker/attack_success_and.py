all_attempts = {"192.168.0.1", "10.0.0.1", "8.8.8.8"}
successful = {"10.0.0.1", "8.8.8.8"}

failed = all_attempts - successful
print("공격 실패 IP:", failed)