print("1. 리스트에서 인덱스로 값 꺼내기")
try:
    nums = [10, 20, 30]
    n = int(input("숫자를 입력하세요."))
    print(nums[n])
except ValueError:
    print("존재하지 않는 인덱스입니다.")

print("2. 나이를 입력받고 음수일 경우 예외 발생시키기")
try:
    age = int(input("나이를 입력하세요:"))
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다.")
except ValueError as e:
    print("오류: ", e)

print("3. 문자열을 숫자로 변환하기")
try:
    num = int(input("숫자를 입력하세요:"))
    print(num)
except NotReturnValue:
    print("숫자로 변환할 수 없습니다.")

print("4. 파일 열기 시도 후 종료 메시지 출력")
try:
    filename = input("파일 이름:")
    with open(filename, "r") as f:
        f.read()
except NotFileFoundError:
    print("파일 처리 시도 완료")

print("5. 특정 단어가 포함된 문장 검사")
try:
    connect2 = input("문장을 입력하세요:")
    if connect2.find("admin"):
        raise ValueError("관리자 키워드가 필요합니다.")
except ValueError as e:
    print("오류: " e)