a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a < b and a < c:
    print("Наименьшее число:", a)
elif b < a and b < c:
    print("Наименьшее число:", b)
else:
    print("Наименьшее число:", c)

if a == b == c:
    print("3")
elif a == b or a == c or b == c:
    print("2")
else:
    print("0")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for num in numbers:
    sum += num

print("Сумма чисел:", sum)

n = int(input("Введите количество чисел в массиве: "))
numbers = []

for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

count = 0

for num in numbers:
    if num == 0:
        count += 1

print("Количество чисел равных нулю:", count)

n = int(input("Введите натуральное число (<=9): "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
