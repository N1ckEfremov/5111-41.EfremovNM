import numpy as np
import math as mt
first_matrix = np.array([[1,3,4],[2,3,4],[4,5,6]])
second_matrix = np.array([[0,9,8],[8,7,6],[7,6,5]])
def arr_valid(first_matrix, second_matrix):
    return (first_matrix.shape[0] == second_matrix.shape[1]) and (first_matrix.shape[1] == second_matrix.shape[0])
def mat_mult(first_matrix, second_matrix):
    res = np.array((first_matrix.shape[0],second_matrix.shape[1]))
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            for k in range(first_matrix.shape[0]):
                res[i, j] += first_matrix[i,k] * second_matrix[k,i]
    return res
print(mat_mult(first_matrix, second_matrix))
