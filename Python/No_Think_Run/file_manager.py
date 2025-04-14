def save_user(user):
    with open("users.txt", "a") as f:
        f.write(f"{user.get_name()},{user.get_password()}")

def load_users():
    users = []
    try:
        with open("users.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                name, pw = line.strip().split(",")
                from user_system import User
                users.append(User(name, pw))
    except FileNotFoundError:
        print("사용자 파일이 아직 없습니다.")
    return users