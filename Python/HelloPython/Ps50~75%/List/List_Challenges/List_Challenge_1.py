#1 리스트 생성하고 출력하기
fruits = ["apple", "banana", "cherry"]
print(fruits)

#2 리스트에서 첫 번째와 마지막 값 출력하기
print(fruits[0])
print(fruits[2])

#3 리스트에 "orange" 추가하기
fruits.append("orange")
print(fruits)

#4 "banana" 제거하기
fruits.remove("banana")
print(fruits)

#5 리스트 길이 출력하기
print(len(fruits))

#6 리스트 반복 출력
for fruit in fruits:
    print(fruit)