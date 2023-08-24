import numpy as np


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MatrixMultiplier():
    matrix_a  = None
    matrix_b  = None

    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        if len(matrix_a) != len(matrix_b[0]) or len(matrix_a[0]) != len(matrix_b):
            raise MyCustomException("The shape of the matrices are not matched")


    def multiply(self, matrix_a, matrix_b):
        if matrix_a is None or matrix_b is None:
            return np.array([[0]])
        elif len(matrix_a)==0 or len(matrix_a[0])==0 or len(matrix_b)==0 or len(matrix_b[0])==0:
            return np.array([[0]])
        elif len(matrix_a)==1 and len(matrix_a[0])==1:
            return np.array([[matrix_a[0][0]*matrix_b[0][0]]])

        columns = len(matrix_a)
        rows = len(matrix_a)
        target_matrix = np.array([[0.0]*columns for i in range(rows)])

        columns=int(columns/2)
        rows=int(rows/2)


        target_matrix[:rows, :columns] = self.multiply(matrix_a[:rows, :columns], matrix_b[:columns, :rows])+self.multiply(matrix_a[:rows, columns:], matrix_b[columns:, :rows])
        target_matrix[:rows , columns:] =  self.multiply(matrix_a[:rows, :columns], matrix_b[:columns, rows:])+self.multiply(matrix_a[:rows, columns:], matrix_b[columns:, rows:])
        target_matrix[rows:, :columns] = self.multiply(matrix_a[rows:, :columns], matrix_b[:columns, :rows])+self.multiply(matrix_a[rows:, columns:], matrix_b[columns:, :rows])
        target_matrix[rows: , columns:] =  self.multiply(matrix_a[rows:, :columns], matrix_b[:columns, rows:])+self.multiply(matrix_a[rows:, columns:], matrix_b[columns:, rows:])

        return target_matrix

AA=np.random.rand(4,3)
BB=np.random.rand(3,4)
A=MatrixMultiplier(AA , BB)
print(A.multiply(AA, BB))
print(np.dot(AA,BB))