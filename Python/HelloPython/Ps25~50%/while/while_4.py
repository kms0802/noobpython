from ast import Continue


num = 0

while num < 5:
    num = num + 1
    if num == 3:
        continue
    print(num)