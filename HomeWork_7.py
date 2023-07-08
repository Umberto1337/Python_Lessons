'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке.
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-да
Вывод:
Парам пам-пам
'''
def check_rhythm(poetry):
    lines = poetry.split()  
    syllables_counts = list(map(lambda line: sum(map(count_syllables, line.split('-'))), lines))
    if len(set(syllables_counts)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'
    
def count_syllables(word):
    vowels = 'аеёиоуыэюя' 

    syllables = len(list(filter(lambda char: char in vowels, word)))  # Подсчет гласных букв

    return syllables

poetry = input("Введите стихотворение Винни-Пуха: ").lower()
result = check_rhythm(poetry)
print(result)


'''Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.'''

# # Решение через цикл "for"
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row_values = [operation(i, j) for j in range(1, num_columns + 1)]
        row_str = ' '.join(str(value) for value in row_values)
        print(row_str)

print_operation_table(lambda x, y: x * y)

# # Решение через встроенную функцию "map"
def print_operation_table(operation, num_rows=6, num_columns=6):
    rows = range(1, num_rows + 1)
    columns = range(1, num_columns + 1)
    table = map(lambda x: ' '.join(map(str, map(lambda y: operation(x, y), columns))), rows)
    for row in table:
        print(row)

print_operation_table(lambda x, y: x * y)
