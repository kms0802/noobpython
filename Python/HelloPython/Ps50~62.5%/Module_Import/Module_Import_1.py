import math
import random
import datetime
import os
import sys

num = float(input("제곱근:"))
root = math.sqrt(num)
print(root)

password = ""
for _ in range(4):
    password = password + str(random.randint(0,9))
print(password)

password2 = "".join([str(random.randint(0,9)) for _ in range(4)])
print(password2)

today = datetime.date.today()
print(today.strftime("%Y_%m_%d"))

cwd = os.getcwd()
print(cwd)

print(sys.argv)