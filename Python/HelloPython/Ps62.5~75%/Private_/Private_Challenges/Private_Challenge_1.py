print("1. private 변수 만들기")
class User:
    def __init__(self, name, pw):
        self.name = name
        self._nickname = "닉네임"
        self.__password = pw

    def show_info(self):
        print("이름", self.name)
        print("닉네임:", self._nickname)
        print("비밀번호:", self.__password)

    def get_password(self):
        return self.__password
    
    def set_password(self, new_pw):
        self.__password = new_pw
    
us = User("홍길동", "1234")
us.show_info()

print("2. getter 사용하기")
print(us.get_password())