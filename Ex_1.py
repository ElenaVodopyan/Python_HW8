import random
group_count = 5 
marks = [0] * group_count

for i in range(group_count):
    marks[i] = [random.randint(2, 5) for _ in range(random.randint(20, 30))]


mark_max = 0
group_max = 0

for i in range(group_count):
    average_mark = 0
    students_count = len(marks[i])
    for j in range(len(marks[i])):
        average_mark += marks[i][j]
    average_mark /= students_count
    print(f'{marks[i]} средний балл: {round(average_mark, 2)}')
    if average_mark > mark_max:
        mark_max = average_mark
        group_max = i + 1

print(f'Максимальный средний балл у группы {group_max}')