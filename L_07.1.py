"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        [print(self.lst[l]) for l in range(len(self.lst))]

    def __add__(self, other):
        result = []
        for l in range(len(self.lst)):
            result.append([x + y for x, y in zip(self.lst[l], other.lst[l])])
        return Matrix(result)


square1 = Matrix([[3,6,9], [2,3,0], [9,1,5]])
square2 = Matrix([[1,1,9], [9,1,0], [7,7,7]])

print('Матрица №1:')
square1.__str__()

print('Матрица №2:')
square2.__str__()

print('Результат сложения:')
square1.__add__(square2).__str__()