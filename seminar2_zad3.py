#Напишите программу, в которой пользователь будет задавать две строки, 
#а программа - определять количество вхождений одной строки в другой. 
#COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.

def convert_string (s):
    array = []
    end = 0
    s = s + (' ')
    start = 0
    for i in range (len(s)):
        if s[i] == (' ') or s[i] == (','):
            end = i
            array.append (s[start:end])
            start = end+1
    return array



list_one = convert_string (input ('Введите строку 1'))
print (list_one)
list_two = convert_string (input ('Введите строку 2'))
sum = 0
for i in range (len(list_one)):
    for j in range (len(list_two)):
        if list_one[i] == list_two [j] != (' '):
            sum+=1
if sum == 0:
    print ('Совпадений не найдено')
else:
    print (f'Количестов вхождений строки 1 в строку 2 - {sum}')