print("1. 기본값 매개변수")
def greet(name="익명"):
    print("Hello", name)

greet()
greet("철수")

print("2. 키워드 인자")
def show_info(name, age):
    print(name, ":", age)

show_info(age=20, name="영희")

print("3. 가변 인자")
def total(*numbers):
    print("합계:", sum(numbers))

total(1, 2, 3)
total(10, 20, 30, 40)

print("4. 키워드 가변 인자")
def show_profile(**info):
    for key, value in info.items():
        print(key, ":", value)

show_profile(name="neo", age=30, job="해커")

print("5. 다중 반환값")
def calc(x, y):
    return x + y, x - y

a, b = calc(10, 5)
print("합:", a, "차:", b)

print("6. 함수 안에 함수")
def outer():
    def inner():
        print("안쪽 함수 실행됨")
    inner()

outer()