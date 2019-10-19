"""
Напишите функцию, которая находит сумму четных элементов на главной диагонали квадратной матрицы 
(именно чётных элементов, а не элементов на чётных позициях!).
Если чётных элементов нет, то вывести 0. Используйте библиотеку numpy.
Входные данные -- квадратный np.ndarray.
"""

import numpy as np
def diag_2k(a):
    #YOUR CODE
    diag = np.diag(a)
    result = 0
    for el in diag:
        if el % 2 == 0:
            result += el
    return result