# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
quarter = int(input(('Enter number of quarter = ')))
if quarter == 1: print(f'x = {range(1, 10**10)} y = {range(1, 10**10)}')
elif quarter == 2: print(f'x = {range(-10**10, 0)} y = {range(1, 10**10)}')
elif quarter == 3: print(f'x = {range(-10**10, 0)} y = {range(-10**10, 0)}')
elif quarter == 4: print(f'x = {range(1, 10**10)} y = {range(-10**10, 0)}')