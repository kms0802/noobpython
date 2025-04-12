print("1. 파일에 쓰기")
f = open("test.txt", "w")
f.write("첫 번째 줄입니다.\n")
f.write("두 번째 줄입니다.\n")
f.close()
print()

print("2. 파일 읽기")
f = open("test.txt", "r")
data = f.read()
print(data)
f.close()
print()

print("3. 한줄씩 읽기")
f = open("test.txt", "r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()
print()

print("4. 모든 줄을 리스트로 읽기")
f = open("test.txt", "r")
lines = f.readline()
for line in lines:
    print(line.strip())
f.close()
print()

print("5. with.open()으로 자동닫기")
with open("test.txt", "a") as f:
    f.write("추가된 줄입니다.\n")
print()

print("6. 다시 읽기 위해 처음으로 이동 seek()")
f = open("test.txt", "r")
print(f.readline())
f.seek(0)
print(f.readline())
f.close()

