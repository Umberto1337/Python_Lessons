# import random

# numbers_list = [random.randint(0, 9) for _ in range(10)]

# unique_numbers = set(numbers_list)

# count = len(unique_numbers)

# print("Сгенерированный список чисел:", numbers_list)
# print("Количество различных чисел:", count)


'''
Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
'''

# sequence = [random.randint(0, 9) for _ in range(10)]
# k = 2
# n = len(sequence)
# k = k % n 

# shifted_sequence = sequence[-k:] + sequence[:-k]
# print(sequence)
# print(shifted_sequence)


# import random

# print(my_list := [random.randint(0, 5) for _ in range(int(input('Введите размер списка: ')))])

# shift = int(input('Введите сдвиг: '))

# for i in range(100):
#     print(my_list[i % len(my_list)], end=' ')

# print('\n' + str(my_list[-shift:] + my_list[:-shift]))

# for _ in range(shift):
#     my_list.insert(0, my_list.pop())
# print(my_list)


'''Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
'''
# import random

# array = [random.randint(0, 9) for _ in range(10)]
# count = 0

# for i in range(1, len(array)):
#     if array[i] > array[i-1]:
#         count += 1
# print(array)
# print(count)

'''Напишите программу для печати всех уникальных значений в словаре.
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]'''

# list_1 = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005"},
#     {"V": "S009"},
#     {"VIII": "S007"}
# ]

# unique_values = set()

# for dictionary in list_1:
#     for value in dictionary.values():
#         unique_values.add(value)

# for value in unique_values:
#     print(value)
