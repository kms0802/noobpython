print("리스트 내포 기본 문법들")
nums = [x for x in range(5)]
print(nums)
print()

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

print("1. 제곱 리스트 만들기")
squares = [x**2 for x in range(1, 6)]
print(squares)
print()

print("2. 문자열 길이 리스트 만들기")
words = ["hackers", "admin", "root"]
lengths = [len(word) for word in words]
print(lengths)
print()

print("3. IP에서 10.x.x.x 대역만 걸러내기")
ips = ["192.168.0.1", "10.0.0.2", "8.8.8.8", "10.1.2.3"]
ten_ips = [ip for ip in ips if ip.startswith("10.")]
print(ten_ips)
print()

print("4. 중복 없는 숫자 리스트 만들기")
nums = [1, 2, 2, 3, 3, 3]
unique = list({x for x in nums})
print(unique)