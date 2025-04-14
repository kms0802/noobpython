class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.attempts = 0
    
    def login(self, input_pw):
        if self.attempts >= 3:
            print("로그인 시도 횟수 초과! 계정 잠김 ")
            return
        
        if input_pw == self.__password:
            print(f"{self.username}님 로그인 성공")
            self.attempts = 0
        else:
            self.attempts += 1
            print(f"비밀번호 틀림! {self.attempts}/3")

user1 = User("neo", "matrix")

user1.login("test")
user1.login("1234")
user1.login("matrix")
user1.login("wrong")