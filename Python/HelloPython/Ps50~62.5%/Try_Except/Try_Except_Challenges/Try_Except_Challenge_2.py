print("1. 정수 입력 받고 10 더하기")
try:
    num1 = int(input("정수를 입력하세요"))
    print(num1 + 10)
except ValueError:
    print("정수만 입력하세요!")

print("2. 나누기 계산기")
try:
    num3 = int(input("숫자 입력:"))
    num4 = int(input("숫자 입력:"))
    result = num3 / num4
    print(result)
except ValueError:
    print("숫자만 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

print("3. 파일 쓰기 시 에러 처리")
filename = input("파일 이름을 입력하세요: ")
content = input("저장할 내용을 입력하세요: ")

try:
    with open(filename, "w") as f:
        f.write(content)
        print("저장 완료!")
except Exception:
    print("파일을 저장할 수 없습니다.")

print("4. finally로 정리 메시지 출력")
try:
    age = int(input("나이 입력: "))
except ValueError:
    print("숫자만 입력하세요!")
finally:
    print("입력 시도 완료")

print("5. raise로 사용자 정의 예외 발생")
try:
    num6 = int(input("정수를 입력하세요."))
    if num6 > 100:
        raise ValueError("100보다 큰 수를 입력할 수 없습니다.")
except ValueError as e:
    print("오류:", e)