"""
Перемножение матриц
Напишите две функции, каждая из которых перемножает две квадратные матрицы:
одна без использования встроенных функций numpy, а другая --- с помощью numpy. 
На вход первой задаче подаются списки размера size по size элементов в каждом.
На вход второй задаче подаются объекты типа np.ndarray --- квадратные матрицы одинакового размера. 

Первая функция должна возвращать список списков, а вторая -- np.array.
"""
import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """

    #YOUR CODE: please do not use numpy
    result = []
    for i in range(len(first)):
        temp1 = []
        for j in range(len(second)):
            res = 0
            for k in range(len(second)):
                res += a[i][k] * b[k][j]
            temp1.append(res)
        result.append(temp1)
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    result = np.dot(first, second)
    return result