"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
2 2
4
"""
result = 0
def sum(a,b) :
    global result
    if a == 0 and b == 0 :
        return result
    else :
        result += 1
        if a == 0 and b != 0:
            sum(a,b-1)
        elif a != 0 and b == 0:
            sum(a-1,b)
        else :
            sum(a,b-1)
            
a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

sum(a,b)
print('Сумма чисел',a,'и',b,'равна:',result)
