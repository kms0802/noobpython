score = int(input("점수를 입력하세요:"))
id = input("아이디 입력")
if score >= 50 or id == "admin":
    print("통과")
else:
    print("불합격")