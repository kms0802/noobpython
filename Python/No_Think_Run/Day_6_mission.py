class User:
    def __init__(self, name):
        self.name = name
        self.__password = ""
    
    def get_password(self):
        return self.__password
    
    def set_password(self, pw):
        if len(pw) >= 4:
            self.__password = pw
        else:
            print("4자리 이상 입력하세요.")

    def show_info(self, name):
        print(name, "님의 비밀번호:", self.__password)

u = User("홍길동")
u.set_password("1234")
print(u.get_password())
u.show_info("홍길동")