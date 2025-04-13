class User:
    def __init__(self, name, pw):
        self.name = name
        self._nickname = "닉네임"
        self.__password = pw
    
    def show_info(self):
        print(self.name)
        print(self._nickname)
        print(self.__password)
    
u = User("홍길동", "1234")
u.show_info()

print(u.name)
print(u._nickname)