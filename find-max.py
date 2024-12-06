def find_mix(num):
    if not num:
        print ("Список не должен быть пустым")
    min = num[0]
    for n in num:
        if n < min:
            min = n
    return min
n = int(input("Введите количество чисел: "))
if n <= 0:
        print ("Количество чисел должно быть положительным")
nums = []
for i in range(n):
        number = float(input(f"Введите число {i + 1}: "))
        nums.append(number)
print("Минимум:", find_min(nums))
