'''
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''
# input_str = input("Введите строку: ")
# symbols = input_str.split()
# count_dict = {}

# output_str = ""

# for symbol in symbols:
#     if symbol in count_dict:
#         count_dict[symbol] += 1
#         symbol += "_" + str(count_dict[symbol] - 1)
#     else:
#         count_dict[symbol] = 1
#     output_str += symbol + " "

# print(output_str.strip())

'''
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
'''

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# # text = input("Введите текст: ")
# text_lower = text.lower()  
# words = text_lower.split()
# unique_words = []

# for word in words:
#     if word not in unique_words:
#         unique_words.append(word)

# print(len(unique_words))

# input_string = "aaabcaadcdd"
# char_count = {}
# output = []

# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#         output.append(f"{char}_{char_count[char]}")
#     else:
#         char_count[char] = 0
#         output.append(char)

# output_string = ' '.join(output)
# print(output_string)

#Моё 
# max_number = -1  # Инициализируем переменную максимального числа как -1
# while True:
#     n = int(input("Введите число (для окончания введите 0): "))
#     if n == 0:
#         break
#     if n > max_number:
#         max_number = n

# print("Наибольшее число:", max_number)

