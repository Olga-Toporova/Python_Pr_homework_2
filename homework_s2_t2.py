'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
- 4 -> [1, 2, 6, 24]
- 6 -> [1, 2, 6, 24, 120, 720]
'''
number = int(input("Введите число "))
result = 1
result_list = list()
for n in range(1, number + 1):
     result *= n
     result_list.append(result)    
print(result_list)