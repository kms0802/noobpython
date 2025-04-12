print("1. 변수와 자료형")
name_1 = "neo"
age_1 = 25
height_1 = 180.5
is_hacker_1 = True
print()

print("2. 연산자")
a_2 = 15
b_2 = 4
print()

print(a_2 + b_2)
print(a_2 - b_2)
print(a_2 * b_2)
print(a_2 / b_2)
print(a_2 // b_2)
print(a_2 % b_2)
print(a_2 ** b_2)

print("3. 문자열 다루기")
str_3 = " hello python "
print(str_3.strip())
print()

print("4. 조건문")
age_4 = int(input("나이를 입력하세요."))
if age_4 >= 20:
    print("성인")
elif age_4 >= 13 and age_4 <= 19:
    print("청소년")
else:
    print("어린이")
print()

print("5. 논리 연산자")
age_5 = int(input("나이를 입력하세요."))
account_5 = input("아이디를 입력하세요.")
if age_5 >= 18 and account_5 == "admin":
    print("접속 허용")
else:
    print("접속 거부")
print()

print("6. while 반복문")
while True:
    user_said_6 = input("명령어를 입력하세요.")
    if user_said_6 == "exit":
        break
    else:
        print("명령어를 다시 입력하세요 예) exit")
print()

print("7. for 반복문")
list_7 = ["admin", "neo", "guest"]
for user_7 in list_7:
    print(user_7)
print()

print("8. 함수 정의와 호출")
def greet(name):
    print("Hello", name, "!")
greet("홍길동")

print("9. 리스트")
users_9 = ["admin", "guest"]
users_9.append("user")
users_9.remove("admin")
print(users_9)

print("10. 튜플 & 집합")
list_10 = ("neo", "admin", "guest")
print(list_10[1])
ips = {"192.168.0.1", "10.0.0.1", "192.168.0.1"}
print(ips)

print("11. 딕셔너리")
users_11 = {
    "admin":"1234",
    "neo":"matrix",
}
print(users_11["admin"])

print("12. 리스트 내포")
list_12 = [x for x in range(1,21) if x % 3 == 0]
print(list_12)