'''
3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''
n = int(input("Введите число: "))
num_list = list()
result = 0
i = 0
while i < n:
    formule = round((1 + 1/n)**n)
    num_list.append(formule)
    result += formule
    i += 1

print(f" {num_list} -> {result}")
