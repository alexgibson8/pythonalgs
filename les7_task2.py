"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы. Долго мучался с этой задачей, пришлось прибегнуть к
помощи сторонних источников)))
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def merge_sort(data):
    if len(data) <= 1:
        return data
    left = merge_sort(data[:len(data) // 2])
    right = merge_sort(data[len(data) // 2:])
    cross = [0] * (len(left)+len(right))
    l = r = i = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            cross[i] = right[r]
            r += 1
        else:
            cross[i] = left[l]
            l += 1
        i += 1
    while l < len(left):
        cross[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        cross[i] = right[r]
        r += 1
        i += 1
    for j in range(len(data)):
        data[j] = cross[j]
    return data

print('Sorted array:', merge_sort(array))