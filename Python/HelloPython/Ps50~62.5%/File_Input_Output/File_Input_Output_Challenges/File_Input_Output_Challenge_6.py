print("1. 사용자 이름 저장하기")
with open("myname.txt", "w") as f:
    f.write("이름: 철수")

print("2. 나이 정보 파일에서 읽기인데 그냥 myname.txt 파일 읽어버리기")
with open("myname.txt", "r") as f:
    text = f.read()
print(text)

print("3. 좋아하는 동물 입력받아 저장하기")
animal = input("가장 좋아하는 동물은?")
with open("zoo.txt", "w") as f:
    f.write(animal + "\n")