"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
домашнего задания первых трех уроков.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
import timeit
import cProfile


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
    return array, f'Были поменяны {array[idx_min]} и {array[idx_max]}'


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
    return array, f'Были поменяны {array[idx_min]} и {array[idx_max]}'


def third_solve(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    array_1 = [{min(array): max(array), max(array): min(array)}.get(x, x) for x in array]
    return array_1


print(timeit.timeit('first_solve(5)', number=100, globals=globals()))  # 0.0006902999593876302
print(timeit.timeit('first_solve(10)', number=100, globals=globals()))  # 0.0011787000112235546
print(timeit.timeit('first_solve(20)', number=100, globals=globals()))  # 0.002192899992223829
print(timeit.timeit('first_solve(40)', number=100, globals=globals()))  # 0.004455900052562356
print(timeit.timeit('first_solve(80)', number=100, globals=globals()))  # 0.0073488999623805285
print(timeit.timeit('first_solve(160)', number=100, globals=globals()))  # 0.014416199992410839
print(timeit.timeit('first_solve(320)', number=100, globals=globals()))  # 0.025119600002653897
print(timeit.timeit('first_solve(640)', number=100, globals=globals()))  # 0.058232099981978536
print(timeit.timeit('first_solve(1280)', number=100, globals=globals()))  # 0.13551309995818883
print(timeit.timeit('first_solve(2560)', number=100, globals=globals()))  # 0.24020240001846105
cProfile.run('first_solve(5120)')
"""
42268 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.000    0.000    0.016    0.016 les4_task1.py:34(second_solve)
        1    0.001    0.001    0.015    0.015 les4_task1.py:38(<listcomp>)
     5120    0.003    0.000    0.004    0.000 random.py:239(_randbelow_with_getrandbits)
     5120    0.006    0.000    0.012    0.000 random.py:292(randrange)
     5120    0.002    0.000    0.014    0.000 random.py:366(randint)
    15360    0.001    0.000    0.001    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sorted}
     5120    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     6420    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
print(' ')
print(timeit.timeit('second_solve(5)', number=100, globals=globals()))  # 0.0006902999593876302
print(timeit.timeit('second_solve(10)', number=100, globals=globals()))  # 0.0011787000112235546
print(timeit.timeit('second_solve(20)', number=100, globals=globals()))  # 0.002192899992223829
print(timeit.timeit('second_solve(40)', number=100, globals=globals()))  # 0.004455900052562356
print(timeit.timeit('second_solve(80)', number=100, globals=globals()))  # 0.0073488999623805285
print(timeit.timeit('second_solve(160)', number=100, globals=globals()))  # 0.014416199992410839
print(timeit.timeit('second_solve(320)', number=100, globals=globals()))  # 0.025119600002653897
print(timeit.timeit('second_solve(640)', number=100, globals=globals()))  # 0.058232099981978536
print(timeit.timeit('second_solve(1280)', number=100, globals=globals()))  # 0.13551309995818883
print(timeit.timeit('second_solve(2560)', number=100, globals=globals()))  # 0.24020240001846105
cProfile.run('second_solve(5120)')
"""
42268 function calls in 0.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        1    0.000    0.000    0.016    0.016 les4_task1.py:34(second_solve)
        1    0.001    0.001    0.015    0.015 les4_task1.py:38(<listcomp>)
     5120    0.003    0.000    0.004    0.000 random.py:239(_randbelow_with_getrandbits)
     5120    0.006    0.000    0.012    0.000 random.py:292(randrange)
     5120    0.002    0.000    0.014    0.000 random.py:366(randint)
    15360    0.001    0.000    0.001    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sorted}
     5120    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     6420    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""
print(' ')
print(timeit.timeit('third_solve(5)', number=100, globals=globals()))  # 0.0010127000277861953
print(timeit.timeit('third_solve(10)', number=100, globals=globals()))  # 0.0023566000163555145
print(timeit.timeit('third_solve(20)', number=100, globals=globals()))  # 0.005401599977631122
print(timeit.timeit('third_solve(40)', number=100, globals=globals()))  # 0.016434199991635978
print(timeit.timeit('third_solve(80)', number=100, globals=globals()))  # 0.03972200001589954
print(timeit.timeit('third_solve(160)', number=100, globals=globals()))  # 0.15052820002892986
print(timeit.timeit('third_solve(320)', number=100, globals=globals()))  # 0.5565210999920964
print(timeit.timeit('third_solve(640)', number=100, globals=globals()))  # 2.1726844999939203
print(timeit.timeit('third_solve(1280)', number=100, globals=globals()))  # 8.330135099997278
print(timeit.timeit('third_solve(2560)', number=100, globals=globals()))  # 33.190211999986786
cProfile.run('third_solve(5120)')
"""
67969 function calls in 1.228 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.228    1.228 <string>:1(<module>)
        1    0.000    0.000    1.228    1.228 les4_task1.py:50(third_solve)
        1    0.002    0.002    0.016    0.016 les4_task1.py:54(<listcomp>)
        1    0.006    0.006    1.212    1.212 les4_task1.py:55(<listcomp>)
     5120    0.003    0.000    0.005    0.000 random.py:239(_randbelow_with_getrandbits)
     5120    0.006    0.000    0.012    0.000 random.py:292(randrange)
     5120    0.002    0.000    0.014    0.000 random.py:366(randint)
    15360    0.002    0.000    0.002    0.000 {built-in method _operator.index}
        1    0.000    0.000    1.228    1.228 {built-in method builtins.exec}
    10240    0.643    0.000    0.643    0.000 {built-in method builtins.max}
    10240    0.562    0.000    0.562    0.000 {built-in method builtins.min}
     5120    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     5120    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     6523    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
"""
Вывод: мы можем заметить, что в первых двух решениях время работы увеличивается пропоционально увеличению
количества данных (в 2 раза), соответственно тут сложность O(n), а в третьем решении примерно в 4 раза 
Первое и второе решение лучше, чем третье!
"""