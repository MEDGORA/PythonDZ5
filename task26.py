"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""
result = 1

def exponent(a,b) :
    global result
    if b == 0 :
        return result
    else :
        result = result * a
        exponent(a,b-1)

a = int(input('Введите число А: '))
b = int(input('Введите число B: '))

exponent(a,b)
print('Число',a,'в степени',b,'равно:',result)

