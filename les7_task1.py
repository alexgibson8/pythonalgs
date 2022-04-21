"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array_slow = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_fast = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_slow, array_fast, sep='\n')


def slow_bubble(data):
    n = 1
    while n < len(data):
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    return data


def fast_bubble(data):
    n = 1
    while n < len(data):
        for i in range(len(data) - n):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    return data


print('Sorted array:', slow_bubble(array_slow))
print('Sorted array:', fast_bubble(array_fast))


"""
Суть учучшения: при прогоне программы пошагово, я заметил, что последние итерации не делают ничего, так как за то время,
пока мы сортируем ~ первую половину массива, второй уже тоже отсортирован. Поэтому количество итераций можно сократить
до len(data) - n.
"""