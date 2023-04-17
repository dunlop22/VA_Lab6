import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math
import getch


##Расчет значений функции в точках
def y_Count(x_):
    y_2 = []
    for i in range(len(x_)):
        x = x_[i]
        y_2.append(eval(func))
    return y_2



def simpson_(x_, y_, h):

    if len(x_) % 2 == 0: ##нечетное число отрезков, т.к. четное число значений
        ##изменить количество отрезков
        h_old = h
        h = (b - a) / (((b - a) / h_old) + 1)
        x_ = np.arange(a, b + h, h)
        print ("\nНовый шаг (т.к. число отрезков изначально нечетное): ", h)
        ##добавить до четного значения отрезков
        y_ = y_Count(x_)
    
    rez = y_[0] + y_[len(x_) - 1]

    for i in range (1, len(x_), 2): ##подсчет по нечетным 
        rez = rez + (y_[i] * 4)
    
    for i in range (2, len(x_) - 1, 2): ##подсчет по четным 
        rez = rez + (y_[i] * 2)

    rez = rez * h / 3
    return 

def Monte_Carlo(func, a, b ,n):
    x_ = np.arange(a, b + 0.001, 0.001)
    y_ = y_Count(x_)
    M = max(y_)
    
    K = 0

    for i in range(n):
        x = a + rand.random() * (b - a)
        y = M * rand.random()

        if y < eval(func):
            K += 1
            plt.plot(x, y, 'mo')
        else:
            plt.plot(x, y, 'yo')

    plt.plot(x_, y_, 'r')
    plt.grid(True)

    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$y$', fontsize=14)

    plt.show()

    result = M * (b - a) * K / n
    return result

print("Y = ", end = '')
func = input();

print("\nЛевая граница участка: ", end = '')
a = float(input())

print("\nПравая граница участка: ", end = '')
b = float(input())

print("\nШаг (h): ", end = '')
h = float(input())

print("\nКоличество точек (Монте-Карло): ", end = '');
n = int(input())


x_ = np.arange(a, b + h, h)
y_ = y_Count(x_)

print('\nМетод Симпсона: ', simpson_(x_, y_, h), end='')

print('\n\nМетод Монте-Карло: ', Monte_Carlo(func, a, b, n))
