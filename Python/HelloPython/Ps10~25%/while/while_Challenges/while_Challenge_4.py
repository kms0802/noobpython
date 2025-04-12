cmd = "notexit"

while cmd != "exit":
    cmd = input("명령을 입력하세요:")
    if cmd == "exit":
        break
print("입력된 명령어: " + cmd)   