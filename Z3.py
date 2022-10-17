# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from enum import unique
import random
example_numbers = []

def fill_numbers(example_numbers):
    for i in range(random.randint(5, 25)):
        example_numbers.append(random.randint(1, 20))
    print(f'Последовательность чисел: {example_numbers}')

fill_numbers(example_numbers)
unique_numbers = set(example_numbers)
print(f'Уникальные числа: {unique_numbers}')
