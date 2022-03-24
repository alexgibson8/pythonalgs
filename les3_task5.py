"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_neg_n = -1000000000000
max_neg_idx = -1
for i in range(len(array)):
    if (array[i] < 0) and (array[i] > max_neg_n):
        max_neg_n = array[i]
        max_neg_idx = i
if max_neg_n != -1000000000000:
    print(f'Максимальное отрицательное число: {max_neg_n}, его позиция: {max_neg_idx}')
else:
    print('Нет отрицательных элементов!')
