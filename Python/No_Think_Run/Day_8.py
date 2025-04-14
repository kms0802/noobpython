class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.attempts = 0
        self.locked = False
    
    def login(self, input_pw):
        if self.locked:
            print("계정이 잠겼습니다.")
            return False
        
        if input_pw == self.__password:
            print(f"{self.name}님 로그인 성공")
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            print(f"로그인 실패 ({self.attempts}/3)")
            if self.attempts >= 3:
                self.locked = True
                print("계정이 잠겼습니다.")
            return False
    
    def show_info(self):
        print(f"사용자: {self.name}, 로그인 시도:{self.attempts}, 잠김:{self.locked}")

users = [
    User("neo", "1234"),
    User("admin", "abcd"),
    User("guest", "guest")
]

def find_user(name):
    for user in users:
        if user.name == name:
            return user
    
    return None

name = input("아이디 입력:")
pw = input("비밀번호 입력:")

user = find_user(name)

if user:
    success = user.login(pw)
    if success:
        user.show_info()
else:
    print("존재하지 않는 사용자입니다.")