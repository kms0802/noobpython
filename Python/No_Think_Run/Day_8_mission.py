class User:
    def __init__(self, name, pw):
        self.name = name
        self.__password = pw
        self.attempts = 0
        self.locked = False
    
    def login(self,pw):
        if self.locked:
            print("잠긴 계정입니다.")
            return False
        
        if self.__password == pw:
            print(f"{self.name}님 환영합니다.")
            self.attempts = 0
            return True
        else: #비밀번호 실패했을 경우
            if self.attempts <= 3:
                self.attempts += 1
                print(f"비밀번호가 틀렸습니다. 남은 횟수: {self.attempts}")
            else:
                self.locked = True
                print("비밀번호가 잠겼습니다.")
                return False

    def show_info(self):
        print(f"닉네임:{self.name}, 비밀번호: {self.__password}비밀번호 시도:{self.attempts}")
    
users = [
    User("neo", "1234"),
    User("Triple", "4321"),
    User("NameValues", "5678")
]

def find_user(name):
    for user in users:
        if user.name == name:
            return user
    
    return None

name = input("아이디 입력")
pw = input("비밀번호 입력")

user = find_user(name)
if user:
    success = user.login(pw)
    if success:
        user.show_info()
else:
    print("존재하지 않는 사용자입니다.")