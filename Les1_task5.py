alp = 'abcdefghijklmnopqrstuvwxyz'
num1 = input('Введите первую букву ')
num2 = input('Введите вторую букву ')
a = alp.index(num1) + 1
b = alp.index(num2) + 1
c = b - a - 1

print(f'Первая буква: {num1} - находится на {a} позиции,\
      вторая буква {num2} - находится на {b} позиции.\
      Между ними {c} буквы')
