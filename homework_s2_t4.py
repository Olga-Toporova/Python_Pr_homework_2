'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 15
'''

N = int(input("Введите количество элементов: "))
position_one = int(input("Введите позицию 1: "))
position_two = int(input("Введите позицию 2: "))
result = 1
numbers_list = list()
for n in range(-N, N+1):
    numbers_list.append(n)
    if n == position_one or n == position_two:
        result *= numbers_list[n-1]

print(f"{numbers_list} -> {result}")
