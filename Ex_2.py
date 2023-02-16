import random
rows = 4
numbers = [0] * rows

for i in range(rows):
    numbers[i] = [random.randint(1, 100) for _ in range(rows)]

diagonal_sum = 0
for i in range(rows):
    diagonal_sum += numbers[i][i]

print(f'Сумма элементов центральной диагонали равна {diagonal_sum}')

for index in range(len(numbers)):
    sum_in_row = sum(numbers[index])
    if sum_in_row > diagonal_sum:
        print(f'{numbers[index]} сумма: {sum_in_row} - сумма элементов строки больше')
    else:
        print(f'{numbers[index]} сумма: {sum_in_row}')
