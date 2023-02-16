import random

def period_temp(month, temp_row, period):
    max_temp = 0
    day_max_temp = 1
    min_temp = 1000
    day_min_temp = 1

    for day in range(len(temp_row) - period + 1):
        temp_in_period = temp_row[day:day + period]
        sum_temp_in_period = sum(temp_in_period)        
        if sum_temp_in_period > max_temp:
            max_temp = sum_temp_in_period
            day_max_temp = day
        elif sum_temp_in_period < min_temp:
            min_temp = sum_temp_in_period
            day_min_temp = day
    print(f'{month}: {temp_row} | MAX t\' {round(max_temp/period)} с {day_max_temp} по {day_max_temp + period} ---- MIN t\' {round(min_temp/period)} с {day_min_temp} по {day_min_temp + period}')    

rows = 4

temp_table = [0] * rows

for i in range(rows):
    temp_table[i] = [random.randint(18, 32) for _ in range(30)]    
    period_temp(i+5, temp_table[i], 7)
