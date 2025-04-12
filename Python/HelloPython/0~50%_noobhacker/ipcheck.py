blacklist = {"192.168.0.10", "10.0.0.3", "172.16.5.8"}
access_list = {"192.168.0.1", "10.0.0.3", "8.8.8.8", "172.16.5.8"}

for ip in access_list:
    if ip in blacklist:
        print(ip, "-> 차단됨")
    else:
        print(ip, "-> 허용됨")