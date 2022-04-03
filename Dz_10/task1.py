class Matrix:

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in i) for i in self.__value)

    def __add__(self, other):
        return Matrix(map(lambda list_1, list_2: map(lambda x, y: x + y, list_1, list_2), self.__value, other.__value))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 6], [5, 6]])

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
