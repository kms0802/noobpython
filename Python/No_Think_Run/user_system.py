class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.attempts = 0
        self.locked = False
    
    def check_password(self, input_pw):
        if self.locked:
            print("계정이 잠겼습니다.")
            return False
        if input_pw == self.__password:
            print(f"{self.name}님 로그인 성공!")
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            print(f"로그인 실패({self.attempts}/3)")
            if self.attempts >= 3:
                self.locked = True
                print("계정이 잠겼습니다.")
            return False
    
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.__password