# 1. 튜플 생성과 출력
info = ("홍길동", 20, "Korea")
print(info)

# 2. 튜플 인덱싱
fruits = ("apple", "banana", "cherry")
print(fruits[1])

# 3. 튜플은 불변임을 확인하기
# fruits[0] = "grade"

# 4. 중복 제거 집합 만들기
ip_list = {"192.168.0.1", "10.0.0.1", "192.168.0.1", "8.8.8.8"}
print(ip_list)

# 5. 집합에 요소 추가 & 제거
#arr = {}

#arr.add("admin")
#print(arr)

arr = set() # 빈 배열 생성
arr.add("admin")
arr.add("user")
arr.add("guest")
print(arr)

arr.remove("user")
print(arr)

# 6. 두 집합의 교집합 구하기
a = {"sql", "xss", "dos"}
b = {"brute", "sql", "xss"}

print(a & b)