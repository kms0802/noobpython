fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

print(fruits[0])
print(fruits[-1])

print(fruits[0:2])
print(numbers[1:])

fruits.append("orange")
fruits.insert(1, "grade")

print(fruits)

fruits.remove("banana")
fruits.pop()

print(fruits)

print(len(fruits))

for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("apple이 리스트에 있어요!")