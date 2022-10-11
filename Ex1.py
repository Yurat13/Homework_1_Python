# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
day_of_week = int(input("Enter number of week's day\n"))
if day_of_week < 6:
    print ("no, it's weekday")
else:
    print ("yes, it's weekend")