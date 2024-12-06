def find_max(num):
    if not num:
        print ("Список не должен быть пустым")
    max = num[0]
    for n in num:
        if n > max:
            max = n
    return max
n = int(input("Введите количество чисел: "))
if n <= 0:
        print ("Количество чисел должно быть положительным")
nums = []
for i in range(n):
        number = float(input(f"Введите число {i + 1}: "))
        nums.append(number)
print("Максимум:", find_max(nums))
