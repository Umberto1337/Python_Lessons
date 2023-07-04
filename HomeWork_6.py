'''Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите колличество колличество элементв: "))

progression = [a1 + i * d for i in range(n)]
print(progression)


'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random

def find_indexes(array, minimum, maximum):
    return [i for i in range(len(array)) if minimum <= array[i] <= maximum]

print(my_array := [random.randint(-10, 10) for _ in range(int(input("Введите размер массива(списка): ")))])
min_value = int(input("Введите минимальный диапозон: "))
max_value = int(input("Введите максимальный диапозон: "))

result = find_indexes(my_array, min_value, max_value)
print(result)