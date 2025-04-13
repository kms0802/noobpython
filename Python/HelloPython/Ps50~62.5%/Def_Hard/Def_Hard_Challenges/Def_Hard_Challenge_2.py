print("1. 기본값 매개변수 사용")
def greet(name = "익명"):
    print("Hello", name)

greet()
greet("홍길동")
print()

print("2. 키워드 인자 사용")
def showInfo(name, age):
    print(age, name)

showInfo(name = "홍길동", age = 20)
print()

print("3. 가변 인자를 사용하여 평균 구하기")
def get_average(*numbers):
    average = sum(numbers) / len(numbers)
    print("평균:", average)

get_average(1, 2, 3, 4, 5)
print()

print("4. 키워드 가변 인자를 사용하여 프로필 출력")
def show_profile(**keyword):
    for key, val in keyword.items():
        print(f"{key}:{val}")

show_profile(name = "홍길동", age = 30, job = "해커")
print()

print("5. 두 수를 더하고 빼는 함수를 만들고, 두 값을 한번에 반환하세요.")
def calc(x, y):
    return x + y, x - y

a, b = calc(10, 5)
print(a, b)
print()

print("6. 내부 함수 사용하기")
def outer():
    def inner():
        print("내부함수")
    inner()

outer()