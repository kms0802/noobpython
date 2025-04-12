print("1. 숫자만 입력받기")
try:
    num = int(input("숫자 입력:"))
    print("결과:", num * 2)
except ValueError:
    print("숫자만 입력하세요!")

print("2. 0으로 나누기 예외 처리")
try:
    a = int(input("a값 입력:"))
    b = int(input("b값 입력:"))
    result = a / b
    print("나눗셈 결과:", result)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
except ValueError:
    print("숫자만 입력하세요!")

print("3. 파일 읽기 예외 처리")
filename = input("읽을 파일 이름: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    print("파일 작업이 끝났습니다.")

print("4. finally 사용")
try:
    num_4 = int(input("숫자 하나를 입력하세요:"))
except:
    print("숫자가 아닙니다.")
finally:
    print("프로그램 종료")

print("5. raise로 예외 발생시키기")
n = int(input("정수를 입력하세요:"))
try:
    x = int(input("정수를 입력하세요: "))
    if x < 0:
        raise ValueError("음수는 입력할 수 없습니다.")
    print("입력한 값:", x)
except ValueError as e:
    print("오류:", e)