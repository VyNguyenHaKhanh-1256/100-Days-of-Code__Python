def is_perfect_number(n):
    if n <= 1:
        return False

    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    total = sum(divisors)
    print(f"Các ước số của {n} là: {divisors}")
    print(f"Tổng các ước số: {total}")

    return total == n

number = int(input("Nhập một số nguyên dương: "))
if is_perfect_number(number):
    print(f"=> {number} là số hoàn hảo!")
else:
    print(f"=> {number} không phải là số hoàn hảo.")

