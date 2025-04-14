class User:
    def __init__(self, name, pw):
        self.name = name
        self.__password = pw
        self.attempts = 0
    
    def login(self, input_pw):
        if self.attempts >= 4:
            print("계정이 잠겼습니다.")
            return

        if input_pw == self.__password:
            print("로그인 성공")
            self.attempts = 0
        elif input_pw != self.__password:
            if self.attempts <= 3:
                print("로그인 실패")
                self.attempts += 1
            elif self.attempts > 3:
                print("계정이 잠겼습니다.")
                return
    
    def set_password(self,new_pw):
        if len(new_pw) >= 4:
            self.__password = new_pw
        else:
            print("비밀번호는 4자리 이상만 가능합니다.")
    
    def show_info(self):
        print(self.name, "님의 정보:", self.__password)

triple = User("트리플", "1234")
triple.login("4321")
triple.login("1234")
triple.set_password("1111")
triple.show_info()