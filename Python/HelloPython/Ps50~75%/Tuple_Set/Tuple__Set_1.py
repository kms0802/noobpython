
# 튜플(Tuple)
info = ("Alice", 20, "Korea")
print(info[0])

# info[1] = 30 -> 오류! 수정 불가


# 집합(set)
ips = {"192.168.0.1", "10.0.0.1", "192.168.0.1"}
print(ips)

ips.add("8.8.8.8")
ips.remove("10.0.0.1")

print(ips)

# 집합 연산
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
