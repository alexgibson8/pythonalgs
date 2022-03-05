num1 = int(input('Введите длину одной стороны '))
num2 = int(input('Введите длину второй стороны '))
num3 = int(input('Введите длину третьей стороны '))
if (num1 < 0) or (num2 < 0) or (num3 < 0):
    print('Данные введены неверно')
else:
    if (num1 < num2 + num3) and (num2 < num1 + num3) and (num3 < num1 + num2):
        print('Треугольник существует!')
        if (num1 == num2) and (num1 == num3):
             print('Это равносторонний треугольник!')
        else:
            if (num1 == num2) or (num2 == num3) or (num1 == num3):
                print('Это равнобедренный треугольник!')
            else:
                print('Это разносторонний треугольник!')

    else:
        print('Треугольник не существует!')
