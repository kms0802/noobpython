def calculate_attack_points(attack_type, critical, success):
    points = 0

    if attack_type == "sql_injection":
        points += 30
    elif attack_type == "xss":
        points += 20
    elif attack_type == "dos":
        points += 25
    else:
        points += 10
    
    if critical:
        points *=2

    if not success:
        points = 0

    return points

atk = input("공격 종류 (sql_injection / xss / dos / 기타): ")
crit = input("치명타 여부 (y/n): ") == "y"
succ = input("공격 성공 여부 (y/n): ") == "y"

score = calculate_attack_points(atk, crit, succ)
print("공격 포인트:", score)