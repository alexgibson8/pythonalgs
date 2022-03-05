a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
if b < min:
    min = b
if c < min:
    c = min
if ((max == a) and (min == c)) or ((max == c) and (min == a)):
    print(b)
elif ((max == a) and (min == b)) or ((max == b) and (min == a)):
    print(c)
else: print (a)
