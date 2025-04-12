#1. 변수 & 자료형
x = 10
name = "neo"
is_hacked = True

#2. 연산자
a = 5
b = 2
print(a ** b)

#3. 타입 변환
age = "20"
print(int(age) + 1)

#4. 문자열 다루기
text = " Hacker "
print(text.strip().upper())

#5. 조건문
score = 90
if score >= 90:
    print("A")

#6. 논리 연산자
if age >= 18 and is_hacked:
    print("접속 허용")

#7. 반복문
for i in range(1, 6):
    print(i)

#8. break / continue
for i in range(10):
    if i == 5:
        break

#9. 함수 정의와 호출
def greet(name):
    print("Hello", name)

greet("Neo")

#10. 리스트
items = ["admin", "user"]
items.append("guest")

#11. 튜플 & 집합
t = {"id", "pw"}
s= {"admin", "admin", "guest"}

#12. 딕셔너리
user = {"id": "neo", "pw": "1234"}
print(user["id"])

#13. 반복문 + 자료구조
for u, pw in {"neo":"123", "admin":"root"}.items():
    print(u, pw)

#14.리스트 내포
squares = [x**2 for x in range(1, 6)]