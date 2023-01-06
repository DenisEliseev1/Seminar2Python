import math


def input_cord (n):
    array = []
    for i in range (n):
        array.append (float (input (f'Введите координату {i+1} - ')))
    return array

def dist_2_point (a, b):
    sum = 0
    for i in range (n):
        sum = sum + (a[i]-b[i])**2
    sum = math.sqrt (sum)
    return sum

try:
    n = int (input ('Введите мерность пространства N='))
    print ('Введите координаты точки 1:')
    point1 = input_cord (n)
    print ('Введите координаты точки 2:')
    point2 = input_cord (n)
    print (f'расстоние от точки 1 до точки 2 - {dist_2_point (point1, point2)}')
except:
    print ('Не корректные значения: N - целое положительное число, координаты точек - любое число')