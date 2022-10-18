#Напишите программу, которая принимает на вход вещественное 
# или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.
try:
    number = float (input('Введите число (если дробь - не более 5 знаков после запятой) - '))
    sum = 0
    while number % 1 != 0:
        number = round (number, 5) * 10
    while number != 0:
        sum += int (number % 10)
        number = number // 10
    print (f'Сумма цифр числа равна {sum}')
except:
    print ('Ошибка - необходимо ввести число (если дробь - не более 5 знаков после запятой)')
