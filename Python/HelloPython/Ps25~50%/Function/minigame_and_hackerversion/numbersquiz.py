import random

def number_game():
    secret = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("숫자를 맞춰보세요 (1~10): "))
        attempts = attempts + 1

        if guess == secret:
            print(f"정답입니다! 시도 횟수: {attempts}번")
            break
        elif guess < secret:
            print("더 큰 수입니다.")
        else:
            print("더 작은 수입니다.")

number_game()