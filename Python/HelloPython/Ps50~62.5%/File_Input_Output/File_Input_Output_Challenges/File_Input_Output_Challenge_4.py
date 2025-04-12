print("1. 파일에 이름 저장하기")
with open("name.txt", "w") as f:
    f.write("내 이름은 홍길동입니다.")

print("2. 파일에서 이름 읽어오기")
with open("name.txt", "r") as f:
    content = f.read()
    print(content)

print("3. 사용자에게 동물 이름을 입력받고 저장하기")
animal = input("좋아하는 동물은?")
with open("animal.txt", "a") as f:
    f.write(animal + "\n")

print("저장 완료!")