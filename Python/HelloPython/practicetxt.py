def get_average(*numbers):
    average = sum(numbers) / len(numbers)
    print("평균:", average)

get_average(1, 2, 3, 4, 5)

def show_info(**keyword):
    for key, val in keyword.items():
        print(f"{key}:{val}")

show_info(name = "홍길동", age = 30, job = "해커")