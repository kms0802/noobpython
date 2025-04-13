print("1. 학생 클래스 만들기")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("안녕하세요. 저는 ", self.name, "이고, 나이는", self.age,"살입니다.")
    
s1 = Student("철수", 20)
s1.introduce()
print()

print("2. 자동차 클래스 만들기")
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def info(self):
        print("모델명: ", self.model, "연식: ", self.year)
    
c1 = Car("현대", 2000)
c1.info()
print()

print("3. 은행 계좌 클래스 만들기")
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def check_balance(self):
        print(self.balance)
print()

print("4. 사용자 클래스 만들기")
class User:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
    
    def login(self, input_id, input_pw):
        if input_id == "admin" and input_pw == "1234":
            print("로그인 성공")

u1 = User("admin", "1234")
u1.login("admin", "1234")
print()

print("5. 여러개의 객체를 리스트에 담고 반복 출력하기")
student1 = Student("철수", 20)
student2 = Student("홍길동", 21)
student3 = Student("김동희", 22)

students = [student1,student2,student3]

for st in students:
    st.introduce()