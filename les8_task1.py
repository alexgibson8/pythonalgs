"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib


def my_func(data):
    input_string = str(data).lower()
    res_set = set()
    couples = []
    for i in range(len(input_string) + 1):
        for j in range(i + 1, len(input_string) + 1):
            str_hash = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            couples.append(input_string[i:j])
            res_set.add(str_hash)
    res_set.remove(hashlib.sha1(input_string.encode('utf-8')).hexdigest())
    return len(res_set)


print(my_func(input('Input your string: ')))
