"""
4. Определить, какое число в массиве встречается чаще всего
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = 0
max_frq = 1
for i in range(len(array)):
    frq = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]
if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз(-а)')
else:
    print('Нет повторяющихся элементов')
