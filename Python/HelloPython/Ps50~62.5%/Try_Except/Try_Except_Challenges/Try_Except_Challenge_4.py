print("1. 숫자 입력하고 출력하기")
try:
    num = int(input("숫자 입력:"))
    print(num)
except ValueError:
    print("숫자만 입력해 주세요.")

print("2. 0으로 나눌 때 에러 처리하기")
try:
    a = int(input("입력값:"))
    result = 10 / a
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 입력하세요")

print("3. 파일 열기")
try:
    with open("data.txt", "r") as f:
        connect = f.read()

except FileNotFoundError:
    print("파일이 없습니다.")

print("4. 문자열을 정수로 변환하기")
try:
    str_num = "123"
    num_4 = int(str_num)
except ValueError:
    print("정수로 변환할 수 없습니다.")

print("5. finally 사용하기")
try:
    nu = int(input("입력하세요:"))
except ValueError:
    print("잘못된")
finally:
    print("입력 시도 완료")