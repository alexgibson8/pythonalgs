x1 = int(input('Введите координату x1'))
y1 = int(input('Введите координату y1'))
x2 = int(input('Введите координату x2'))
y2 = int(input('Введите координату y2'))

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')
