print("1. 입력한 내용을 memo.txt에 저장하기")
memo = input("메모를 입력하세요")
with open("memo.txt", "a") as f:
    f.write(memo + "\n")
print("메모가 저장되었습니다.")

print("2. 저장된 메모 내용 모두 출력하기")
print("저장된 메모 목록: ")

with open("memo.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")
print()

print("3. 특정 단어가 들어간 줄만 출력하기")
keyword = input("찾을 단어 입력: ")

with open("memo.txt", "r") as f:
    lines = f.readlines()

print(f"\n'{keyword}'가 포함된 줄:")
for line in lines:
    if keyword in line:
        print("- " + line.strip())