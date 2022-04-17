import sys
import random

"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
У меня стоит 64 разрядная Windows 10. Python 3.10.
"""


def first_solve(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    max_n = array[0]
    min_n = array[0]
    idx_min = -1
    idx_max = -1
    for i in range(len(array)):
        if array[i] > max_n:
            max_n = array[i]
            idx_max = i
        elif array[i] < min_n:
            min_n = array[i]
            idx_min = i
    t = array[idx_max]
    array[idx_max] = array[idx_min]
    array[idx_min] = t
    memory = sys.getsizeof(n) + sys.getsizeof(size) + sys.getsizeof(min_item) + sys.getsizeof(max_item) + \
             sys.getsizeof(idx_max) + sys.getsizeof(idx_min) + sys.getsizeof(array) + sys.getsizeof(t)
    return array, f'Были поменяны {array[idx_min]} и {array[idx_max]}, выделено памяти: {memory}'


def second_solve(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    array_sort = sorted(array)
    max_n = array_sort[-1]
    min_n = array_sort[0]
    idx_min = array.index(min_n)
    idx_max = array.index(max_n)
    t = array[idx_max]
    array[idx_max] = array[idx_min]
    array[idx_min] = t
    memory = sys.getsizeof(n) + sys.getsizeof(size) + sys.getsizeof(min_item) + sys.getsizeof(max_item) + \
             sys.getsizeof(idx_max) + sys.getsizeof(idx_min) + sys.getsizeof(array) + sys.getsizeof(t)
    return array, f'Были поменяны {array[idx_min]} и {array[idx_max]}, выделено памяти: {memory}'


def third_solve(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    array_1 = [{min(array): max(array), max(array): min(array)}.get(x, x) for x in array]
    memory = sys.getsizeof(n) + sys.getsizeof(size) + sys.getsizeof(min_item) + sys.getsizeof(max_item) + \
             sys.getsizeof(array)
    return array_1, f'Былo выделено памяти: {memory}'


print(first_solve(20))  # 440
print(second_solve(20))  # 440, иногда 436
print(third_solve(20))  # 356

"""
Вывод: Если я правильно понял, как нужно было эту память считать, то из приведенных выше решений следует, что первые два
решения идентичны по памяти, не смотря на разницу во времениработы. Там задействовано одинаковое количество переменных, 
хотя иногда, второе решение задействует на 4 байта меньше. Я не уверен, с чем конкретно это связано. Третье решение же
использует меньше переменных, используя только синтаксис и встроенные функции, поэтому занимает меньше ОП.
"""
