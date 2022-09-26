'''
5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
'''
import random
import copy

min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
origin_list = list(range(min,max+1))

shuffle_list = copy.copy(origin_list)
i=0
while i < len(origin_list):
    sub_i = random.randrange(0, len(origin_list))
    shuffle_list[i], shuffle_list[sub_i] = shuffle_list[sub_i], shuffle_list[i]
    i+=1

print(origin_list, "-> ", shuffle_list)
