"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_n = -1000000000000
min_n = 1000000000000
idx_min = -1
idx_max = -1
for i in range(len(array)):
    if array[i] > max_n:
        max_n = array[i]
        idx_max = i
    elif array[i] < min_n:
        min_n = array[i]
        idx_min = i
print(max_n, min_n)
t = array[idx_max]
array[idx_max] = array[idx_min]
array[idx_min] = t
print(array)
