class User:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

class Admin(User):
    def __init__(self,id, pw, level):
        super().__init__(id, pw)
        self.level = level

ad = Admin("admin", "1234", 2)

print(ad.id)
print(ad.pw)
print(ad.level)