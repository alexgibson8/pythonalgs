import collections

companys = collections.namedtuple('company', ['q1', 'q2', 'q3', 'q4'])
money = {}
total = 0
n = int(input('Введите количество предприятий: '))
for i in range(n):
    name = input('Предприятие ')
    q1_money = int(input(f'Прибыль за первый квартал '))
    q2_money = int(input(f'Прибыль за второй квартал '))
    q3_money = int(input(f'Прибыль за третий квартал '))
    q4_money = int(input(f'Прибыль за четвертый квартал '))
    total = total + q1_money + q2_money + q3_money + q4_money
    money[name] = companys(q1=q1_money, q2=q2_money, q3=q3_money, q4=q4_money,)

print('Средняя прибыль по всем предприятия: ', total/n)
print('Предприятия, чей доход выше среднего:')
for name, profit in money.items():
    if sum(profit) > total/n:
        print(f'{name}')
print('Предприятия, чей доход ниже среднего:')
for name, profit in money.items():
    if sum(profit) < total/n:
        print(f'{name} ')
