"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import timeit
import cProfile


def sieve(n):
    prime = []
    nums = []
    i = 10
    k = 0
    while len(prime) < n:
        f = 2
        for j in range(k, i):
            nums.append(j)
        nums[1] = 0
        while f <= i - 1:
            if nums[f] != 0:
                j = f + f
                while j <= i - 1:
                    nums[j] = 0
                    j = j + f
            f += 1
        for j in range(k, i):
            if (nums[j] != 0) and (len(prime) < n):
                prime.append(nums[j])
        i += 10
        k += 10
    return prime[-1]


def prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        flag = 1
        for j in range(3, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            primes.append(i)
        i += 2
    return primes[-1]


print(sieve(1024))
print(prime(1024))
print(timeit.timeit('sieve(2)', number=100, globals=globals()))  # 0.00028740009292960167
print(timeit.timeit('sieve(4)', number=100, globals=globals()))  # 0.00028789998032152653
print(timeit.timeit('sieve(8)', number=100, globals=globals()))  # 0.0007330999942496419
print(timeit.timeit('sieve(16)', number=100, globals=globals()))  # 0.005462900036945939
print(timeit.timeit('sieve(32)', number=100, globals=globals()))  # 0.02286699996329844
print(timeit.timeit('sieve(64)', number=100, globals=globals()))  # 0.1189037999138236
print(timeit.timeit('sieve(128)', number=100, globals=globals()))  # 0.6574289000127465
print(timeit.timeit('sieve(256)', number=100, globals=globals()))  # 3.495303999981843
print(timeit.timeit('sieve(512)', number=100, globals=globals()))  # 18.54006190004293
cProfile.run('sieve(1024)')
"""
11041 function calls in 1.074 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.074    1.074 <string>:1(<module>)
        1    1.073    1.073    1.074    1.074 les4_task2.py:5(sieve)
        1    0.000    0.000    1.074    1.074 {built-in method builtins.exec}
     1843    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     9194    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
print(' ')
print(timeit.timeit('prime(2)', number=100, globals=globals()))  # 8.230004459619522e-05
print(timeit.timeit('prime(4)', number=100, globals=globals()))  # 0.00017049990128725767
print(timeit.timeit('prime(8)', number=100, globals=globals()))  # 0.0005114000523462892
print(timeit.timeit('prime(16)', number=100, globals=globals()))  # 0.0014405000256374478
print(timeit.timeit('prime(32)', number=100, globals=globals()))  # 0.004009700031019747
print(timeit.timeit('prime(64)', number=100, globals=globals()))  # 0.009741900023072958
print(timeit.timeit('prime(128)', number=100, globals=globals()))  # 0.02591159997973591
print(timeit.timeit('prime(256)', number=100, globals=globals()))  # 0.06814160000067204
print(timeit.timeit('prime(512)', number=100, globals=globals()))  # 0.1921844999305904
cProfile.run('prime(1024)')
"""
5108 function calls in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.006    0.006    0.007    0.007 les4_task2.py:30(prime)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
     4081    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1023    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
"""
Вывод: из-за вложенных циклов и большого количества превращения чисел в 0, решето Эратосфена работает значительно
медленнее,чем второе решение без него. По факту, большее влияние имеет именно превращение составных чисел в 0
"""