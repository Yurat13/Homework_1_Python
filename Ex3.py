# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
x = int(input('x = '))
y = int(input('y = '))
if x > 0 and y > 0:
    print('1st quarter')
elif x < 0 and y > 0:
    print('2nd quarter')
elif x < 0 and y < 0:
    print('3rd quarter')
elif x > 0 and y < 0:
    print('4th quarter')