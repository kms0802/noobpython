def analyze_text(text):
    length = len(text)
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0

    for ch in text:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
        elif ch.isdigit():
            digit_count += 1
        elif ch.isspace():
            space_count += 1

    print("문자열 길이:", length)
    print("대문자 수:", upper_count)
    print("소문자 수:", lower_count)
    print("숫자 수:", digit_count)
    print("공백 수:", space_count)

msg = input("분석할 문자열을 입력하세요:")
analyze_text(msg)
