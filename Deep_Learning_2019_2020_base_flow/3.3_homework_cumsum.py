"""
На вход дан двумерный массив X. Напишите функцию, которая для каждой строчки x=(x1,x2,…,xn) массива X строит строчку s=(s1,s2,…,sn), 
где sk=x1+...+xk, а затем выдаёт массив из построенных строчек.
Используйте библиотеку numpy (вам поможет функция cumsum). 
Выходом функции должен быть двумерный массив той же формы, что и X.
"""

import numpy as np

def cumsum(A):
    #YOUR CODE
    mas = np.array(A)
    list_el = np.cumsum(mas, axis=1)
    result = list_el.reshape(np.shape(A)).tolist()
    return result