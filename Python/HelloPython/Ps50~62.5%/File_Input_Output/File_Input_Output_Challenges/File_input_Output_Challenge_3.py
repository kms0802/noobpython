print("1. message.txt에 Hello, Python 출력하기")
with open("message.txt", "w") as f:
    f.write("Hello, Python!")

print("2. message.txt읽어서 출력하기")
with open("message.txt", "r") as f:
    content = f.read()
    print(content)

print("3. 사용자 입력을 받아서 diary.txt에 추가로 저장하기")
line = input("오늘의 일기: ")

with open("diary.txt", "a") as f:
    f.write(line + "\n")

print("저장 완료!")