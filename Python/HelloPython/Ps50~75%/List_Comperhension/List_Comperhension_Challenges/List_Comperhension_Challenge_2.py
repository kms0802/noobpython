print("1. 제곱수가 홀수인 것만 고르기")
nums = [x for x in range(1, 21) if x % 2 != 0]
print(nums)
print()

print("2. 'a'가 포함된 단어만 고르기")
words = ["apple", "banana", "kiwi", "grape", "melon"]
words_first = [word for word in words if word[0] == "a"]
print(words_first)
print()

print("3. 대문자로 변환된 문자열 리스트 만들기")
words_2 = ["login", "admin", "error", "user"]
words_2_big = [w.upper() for w in words_2]
print(words_2_big)
print()

print("4. 길이가 5 이상인 문자열의 길이만 출력")
data = ["root", "access", "permit", "id", "firewall"]
data_length = [dat for dat in data if len(dat) >= 5]
print(data_length)
print()

print("5. 1~50 중에서 3과 5의 공배수만 출력")
num = [x for x in range(1, 51) if x == (3 * 5)]
print(num)