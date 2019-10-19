"""
Вам подаются на вход два вектора a и b в трехмерном пространстве. 
Реализуйте их скалярное произведение с помощью numpy и без. 
Первой функции на вход подаются два стандартных python-списка размера size, второй функции -- одномерные np.array.
"""
import numpy as np

def no_numpy_scalar(v1, v2):
    #YOUR CODE: please do not use numpy
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def numpy_scalar (v1, v2):
    #YOUR CODE
    result = np.matmul(v1, v2)
    return result