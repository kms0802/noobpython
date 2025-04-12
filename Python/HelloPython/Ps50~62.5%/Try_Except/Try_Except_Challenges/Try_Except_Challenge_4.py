print("1. 리스트 나누기")
try:
    nums = [100, 50, 0, 25]
    n = int(input("입력: "))
    result = n / 100
    print(result)
except (ValueError, IndexError):
    print("잘못된 값이거나 인덱스에 없습니다.")

print("2. 입력받은 숫자2자리 이상 확인")
try:
    a = int(input("a값 입력:"))
    if a < 10:
        raise ValueError("두 자리 이상 숫자만 입력하세요.")
except ValueError as e:
    print("오류: ", e)

print("3. 파일을 읽되, 확장자 검사하기")
filename = input("파일 이름:")
f = open(filename, "w")
if f.last(".txt"):
    raise ValueError("텍스트 파일만 열 수 있습니다.")
