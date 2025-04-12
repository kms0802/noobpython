print("1. Squares of even numbers(1-10)")
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)
print()

print("2. Filter short words")
words = ["root", "admin", "user", "guest", "test"]
words_for = [word for word in words if len(word) <= 4]
print(words_for)

print("3. Numbers divisible by 3 (1-30)")
nums = [x for x in range(1, 31) if x % 3 == 0]
print(nums)

print("4. First letters of words")
names = ["Neo", "Trinity", "Morpheus", "Smith"]
names_text = [name[0] for name in names]
print(names_text)

print("5. 192.168 대역 IP만 필터링")
ips = ["192.168.0.1", "10.0.0.1", "192.168.1.1", "8.8.8.8"]
ips_filter = [ip for ip in ips if ip.startswith("192.168")]
print(ips_filter)

print("6. 빈 문자열 제외하고 길이만 출력")
texts = ["hello", "", "world", "", "python"]
texts_length = [text for text in texts if text != ""]
print(texts_length)