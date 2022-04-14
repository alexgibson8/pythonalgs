from collections import deque

nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
        'D': 13, 'E': 14, 'F': 15, 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: "A", 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
summa = deque()
f_summand = list(input('Введите первое число: '))
s_summand = list(input('Введите второе число: '))
decade = 0
if f_summand < s_summand:
    f_summand, s_summand = deque(s_summand), deque(f_summand)
else:
    f_summand, s_summand = deque(f_summand), deque(s_summand)
while f_summand:
    if s_summand:
        result = nums[f_summand.pop()] + nums[s_summand.pop()] + decade
    else:
        result = nums[f_summand.pop()] + decade
    decade = 0
    if result < 16:
        summa.appendleft(nums[result])
    else:
        summa.appendleft(nums[result - 16])
        decade = 1
    if decade:
        result.appendleft('1')
print(summa)
