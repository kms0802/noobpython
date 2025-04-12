print("1. 텍스트 파일 쓰기")
f = open("log.txt", "w")
f.write("첫 번째 로그입니다.\n")
f.write("두 번째 줄입니다. \n")
f.close()
print()

print("2. 텍스트 파일 읽기")
f = open("log.txt", "r")
data = f.read()
print(data)
f.close()

print("3. 한 줄씩 읽기")
f = open("log.txt", "r")

# 한 줄씩 읽기
line = f.readline()
print("첫 줄:", line)

# 모든 줄 리스트로 읽기
f.seek(0) # 처음으로 되감기
lines = f.readlines()
print("모든 줄:", lines)

f.close()

print("4. 자동으로 닫기(with 문 사용)")
with open("log.txt", "a") as f:
    f.write("세 번째 줄 추가!\n")
