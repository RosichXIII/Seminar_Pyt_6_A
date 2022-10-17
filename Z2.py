# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import random
import string
from itertools import groupby

example_text = ''
for i in range(random.randint(5, 10)):
    example_text += (random.choice(string.ascii_letters) * random.randint(1, 9))    
print(f'Текст: {example_text}')

encoded_text = ''.join([(str(len(list(j))) + i) for i,j in groupby(example_text)])
print(f'Сжатый текст: {encoded_text}')

decoded_text = ''
for i in range(len(encoded_text)):
    if encoded_text[i].isdigit():
        continue
    else:
        decoded_text += (encoded_text[i] * int(encoded_text[i-1]))        
print(f'Восстановленный текст: {decoded_text}')