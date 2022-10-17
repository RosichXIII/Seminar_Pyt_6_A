# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
real_numbers = []
def fill_list(real_numbers):
    for i in range(random.randrange(3, 9)):
        real_numbers.append(round(random.random()*100, 2))
    print('Список:', real_numbers)
def max_min_fractions_difference(real_numbers):
    real_numbers = [round(i % 1, 2) for i in real_numbers]
    print(f'Ответ: {round((max(real_numbers) - min(real_numbers)), 2)}')

fill_list(real_numbers)
max_min_fractions_difference(real_numbers)