print("1. 기본 구조")
try:
    x = int(input("숫자를 입력하세요: "))
    print("입력한 숫자:", x)
except ValueError:
    print("숫자가 아닌 값을 입력했어요!")

print("2. 여러 종류의 예외 다루기")
try:
    num = int(input("숫자 입력: "))
    print(10 / num)
except ValueError:
    print("숫자가 아닙니다!")
except ZeroDivisionError:
    print("0으로는 나눌 수 없어요!")

print("3. 무조건 실행되는 블록")
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    print("파일 작업 끝!")

print("4. 예외가 없을때만 실행")
try:
    age = int(input("나이 입력:"))
except:
    print("숫자가 아님!")
else:
    print("입력한 나이:", age)

print("5. 예외를 직접 발생시키기")
#x = -1
#if x < 0:
   # raise ValueError("음수는 허용되지않아요")