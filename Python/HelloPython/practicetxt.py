class User:
    next_id = 0
    def __inif(self, name):
        self.name = name
        self.user_id = User.next_id
        User.next_id += 1
    
    def show(self):
        print(f"{self.name} , {self.user_id}")

u1 = User("홍길동")
u2 = User("철수")
u1.show()
u2.show()