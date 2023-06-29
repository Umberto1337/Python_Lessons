'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 
'''
# 1)
def power(base, exponent):
    if exponent == 0: return 1
    else: return base * power(base, exponent - 1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
result = power(a, b)
print("Результат:", result)

# 2) (без рекурсии)
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
result = a ** b
print("Результат:", result)


'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
Пример:
2 2 
4
'''
def sum(a, b):
    if b == 0: return a
    elif b > 0: return sum(a + 1, b - 1)
    else: return sum(a - 1, b + 1)

result = sum(2, 2)
print(result) 

