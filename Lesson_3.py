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


# scores_eng = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# scores_rus = {
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#     'Й': 4, 'Ы': 4,
#     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#     'Ш': 8, 'Э': 8, 'Ю': 8,
#     'Ф': 10, 'Щ': 10, 'Ъ': 10
# }

# k = input("Введите слово: ").upper()

# score = 0

# if all(letter in scores_eng for letter in k):
#     scores = scores_eng
# elif all(letter in scores_rus for letter in k):
#     scores = scores_rus
# else:
#     print("Ошибка: введено слово с неизвестными символами")
#     exit()

# for letter in k:
#     score += scores[letter]

# print(score)


# k = 'lizard'

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)
