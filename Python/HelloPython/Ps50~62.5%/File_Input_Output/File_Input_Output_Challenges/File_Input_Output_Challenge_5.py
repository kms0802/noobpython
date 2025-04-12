print("1. 좋아하는 음식 저장하기")
with open("food.txt", "w") as f:
    f.write("나는 김치찌개를 좋아합니다.")

print("2. 저장된 음식 정보 읽어서 출력하기")
with open("food.txt", "r") as f:
    text = f.read()
    print(text)

print("3. 사용자에게 오늘 기분을 입력받아 mood.txt에 추가로 저장하기")
mood = input("오늘 기분은 어떤가요?")
with open("mood.txt", "a") as f:
    f.write(mood + "\n")
print("저장 완료")