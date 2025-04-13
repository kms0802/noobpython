print("1. math 모듈 - 소수점 반올림")
import math

num = float(input("반올림 대상:"))
Ceil = math.ceil(num)
Floor = math.floor(num)
Round = round(num)
#round는 내장함수이므로 math. 없이 사용
print(Ceil)
print(Floor)
print(Round)

print("2. random 모듈-로또 번호 생성기")
import random

Rotto = ""
for _ in range(6):
    Rotto = Rotto + str(random.randint(1,45))
print(Rotto)

Rotto2 = "".join([str(random.randint(1,45)) for _ in range(6)])
print(Rotto2)

#lotto = random.sample(range(1,46), 6)
#print(lotto)

print("3. datetime 모듈 - 현재 시간 출력")
import datetime

today = datetime.date.today()
print("현재 시간 출력: " , today.strftime("%Y_%m_%d"))
# %H:%M:%S

print("4. os 모듈 - 파일 존재 여부 확인")
import os

cwd = os.getcwd()
print(cwd)
#print(os.path.exists("파일 이름"))

print("5. sys 모듈 - 종료 메시지 출력후 프로그램 종료")
import sys

sys.exit("시스템을 종료합니다.")