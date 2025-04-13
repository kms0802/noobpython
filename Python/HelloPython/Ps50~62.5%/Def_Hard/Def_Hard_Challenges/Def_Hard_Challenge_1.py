print("1. 기본값 매개변수")
def greet(name = "익명"):
    print("Hello", name)
greet()
greet("트리플")

print("2. 키워드 인자 사용")
def show_info(name, age):
    print(age, name)

show_info(name = "홍길동", age = 20)

print("3. 가변 인자")
def get_average(*numbers):
   print(*numbers / numbers)

#get_average(1,2,3,4,5)

print("4. 키워드 가변 인자")
def show_profile(**keyword):
    print(**keyword)

print("5. 다중 반환값")
def calc(x, y):
    return x + y, x - y

a, b = calc(20, 10)
print(a, b)

print("6. 내부 함수")
def outer():
    def inner():
        print("안쪽 함수 실행됨")
    inner()

outer()