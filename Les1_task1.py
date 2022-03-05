a = int(input('Введите целое трехзначное число'))

if a < 0:
    a = -a
x = a % 10
y = (a // 10) % 10
z = (a // 100) % 10
if (z > 0) and (z < 10):
    print(x+y+z)
    print(x*y*z)
else:
    print('Введено не трехзначное число')
