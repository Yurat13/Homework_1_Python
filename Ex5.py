# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
print('Enter coordinates of point A')
x1 = int(input('x = '))
y1 = int(input('y = '))
print('Enter coordinates of point B')
x2 = int(input('x = '))
y2 = int(input('y = '))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)
