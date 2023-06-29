'''Последовательностью Фибоначчи называется
последовательность чисел a0
, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи'''

# 1.0
# n = int(input("Введите номер числа Фибоначчи: "))
# a = [0,1]


# def fibonacci(n):
#     for i in range(2, n+1):
#         a.append(a[i-2] + a[i-1])
#     return n


# result = fibonacci(n)
# print(f"N-е число Фибоначчи: {result}")

# 1.2
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# n = int(input("Введите номер числа Фибоначчи: "))
# result = fibonacci(n)
# print(f"N-е число Фибоначчи: {result}")


'''Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
'''
# import random

# def replace_grades(grades):
#     for i in range(len(grades)):
#         if grades[i] >= 4:
#             grades[i] = random.randint(1, 2)

#     return grades

# n = int(input("Введите количество оценок: "))
# grades = [random.randint(3, 5) for _ in range(n)]
# print("Оригинальные оценки: ", end="")
# for grade in grades:
#     print(grade, end=" ")

# result = replace_grades(grades)

# print("\nИзмененные оценки: ", end="")
# for grade in result:
#     print(grade, end=" ")
   
    
'''Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)'''   


# def is_number(number):
#     if number < 2:
#         return False

#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False

#     return True

# number = int(input("Введите число: "))
# if is_number(number):
#     print("yes")
# else:
#     print("no")


'''Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.

Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).'''

def reverse_print(n):
    if n > 0:
        element = input("Введите элемент: ")
        reverse_print(n-1)
        print(element, end=" ")

n = int(input("Введите количество элементов: "))
reverse_print(n)









