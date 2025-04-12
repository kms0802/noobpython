print("1. 메모 추가 프로그램 만들기")
memo = input("메모 입력: ")

with open("note.txt", "a") as f:
    f.write(memo + "\n")

print("메모가 저장되었습니다.")
print()

print("2. 메모 목록 출력")
print("메모 목록: ")

with open("note.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

print("3. 특정 단어가 들어간 줄만 출력")
keyword = input("찾을 단어 입력: ")

with open("note.txt", "r") as f:
    lines = f.readlines()

print(f"\n'{keyword}'가 포함된 줄:")
for line in lines:
    if keyword in line:
        print("- " + line.strip())