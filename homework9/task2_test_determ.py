import random
import math

import numpy

from task2_determinant_prog import determinant

class TestDeterm:
    def test_wrong_size(self):
        assert determinant([[3, 4, 0, 21, 3, 56, 7], [0, 89, 23, 45, 7, 12]]) is None
    
    def test_nothing(self):
        assert determinant() == 0

    def test_1by1_1(self):
        assert determinant([[1]]) == 1

    def test_2by2_1(self):
        assert determinant([[1,2], [2,1]]) == -3

    def test_2by2_2(self):
        assert determinant([[0,0], [0,0]]) == 0

    def test_3by3_1(self):
        assert determinant([[1,2,3],[3,2,1],[2,4,6]]) == 0

    def test_5by5_1(self):
        assert determinant([
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]) == 0

    def test_5by5_2(self):
        assert determinant([
            [11, 2, 0, 40, 5],
            [10, 24, 1, 80, 5],
            [14, 0, 0, 0, 85],
            [1, 51, 7, 81, 9],
            [18, 2, 0, 34, 1]
        ]) == -2964240

    def test_7by7_1(self):
        assert determinant([
            [7, 1, 13, 45, 1, 37, 2],
            [49, 26, 28, 48, 3, 38, 43],
            [17, 30, 9, 36, 32, 21, 5],
            [17, 19, 15, 1, 29, 40, 34],
            [37, 38, 49, 41, 44, 10, 7],
            [42, 10, 4, 28, 38, 45, 19],
            [45, 22, 1, 2, 30, 18, 43]
        ]) == -39103212636

    def test_7by7_2(self):
        assert determinant([
            [9, 11, 16, 22, 47, 42, 32],
            [19, 43, 46, 49, 28, 31, 2],
            [27, 1, 49, 46, 29, 12, 15], 
            [47, 5, 46, 39, 16, 16, 41], 
            [11, 24, 24, 15, 11, 10, 17], 
            [42, 34, 37, 24, 12, 14, 10],
            [22, 48, 48, 30, 22, 20, 34]
        ]) == 0

    def test_10by10_1(self):
        assert determinant([
            [1, 37, 49, 26, 36, 16, 7, 7, 14, 11],
            [9, 20, 2, 10, 1, 43, 20, 1, 8, 41],
            [25, 16, 20, 39, 31, 3, 25, 30, 22, 26],
            [42, 29, 7, 15, 9, 5, 15, 1, 46, 22],
            [13, 20, 41, 47, 45, 41, 15, 47, 22, 34],
            [1, 33, 14, 7, 48, 41, 31, 9, 22, 42],
            [30, 25, 4, 20, 2, 21, 43, 42, 35, 25],
            [32, 5, 32, 31, 27, 35, 5, 24, 2, 10],
            [44, 25, 46, 49, 3, 44, 16, 43, 10, 31],
            [5, 43, 11, 48, 9, 8, 38, 31, 4, 5]
        ]) == 2867175957118618

    def test_10by10_2(self):
        determinant([
            [36, 25, 50, 48, 10, 13, 29, 7, 41, 48, 35, 12, 1, 10, 7, 13, 7, 27, 15, 40],
            [26, 43, 44, 13, 27, 2, 4, 48, 35, 12, 6, 47, 38, 9, 5, 33, 48, 23, 7, 26],
            [7, 17, 17, 26, 46, 2, 31, 5, 38, 32, 28, 48, 41, 15, 20, 21, 22, 44, 38, 39],
            [33, 33, 29, 50, 43, 39, 44, 30, 46, 8, 24, 13, 1, 20, 46, 44, 20, 2, 31, 2],
            [35, 49, 25, 37, 10, 50, 48, 35, 6, 5, 26, 35, 16, 14, 29, 16, 11, 2, 2, 40],
            [38, 10, 12, 27, 20, 32, 16, 15, 27, 1, 40, 29, 44, 30, 29, 41, 12, 16, 16, 19],
            [20, 28, 44, 6, 44, 39, 3, 47, 45, 21, 49, 18, 3, 28, 4, 31, 26, 36, 14, 40],
            [11, 48, 45, 1, 33, 41, 27, 36, 12, 48, 24, 33, 20, 35, 33, 49, 32, 10, 48, 11],
            [9, 18, 39, 8, 13, 11, 39, 18, 7, 23, 13, 47, 17, 22, 48, 9, 26, 27, 10, 41],
            [40, 10, 24, 12, 46, 4, 43, 12, 8, 28, 24, 18, 17, 17, 22, 36, 10, 22, 6, 11],
            [29, 49, 22, 30, 30, 9, 3, 15, 5, 6, 2, 48, 18, 44, 6, 35, 11, 27, 17, 1],
            [13, 8, 18, 17, 2, 20, 17, 10, 4, 21, 39, 27, 32, 29, 48, 44, 40, 16, 32, 24],
            [3, 41, 46, 36, 33, 14, 30, 16, 28, 17, 45, 38, 31, 26, 42, 16, 19, 21, 11, 6],
            [38, 31, 34, 14, 50, 2, 31, 5, 49, 43, 5, 44, 43, 27, 40, 50, 17, 48, 25, 37],
            [26, 19, 14, 21, 22, 35, 9, 6, 48, 40, 18, 32, 12, 6, 39, 38, 49, 6, 29, 33],
            [5, 16, 36, 45, 1, 45, 31, 42, 19, 12, 5, 2, 28, 36, 41, 3, 5, 3, 26, 12],
            [33, 32, 11, 43, 13, 3, 19, 15, 19, 34, 18, 17, 44, 44, 32, 32, 22, 3, 37, 45],
            [31, 13, 14, 45, 38, 41, 13, 31, 39, 49, 34, 13, 32, 11, 41, 30, 1, 23, 30, 4],
            [8, 10, 50, 26, 13, 49, 44, 3, 13, 9, 5, 30, 48, 44, 7, 47, 43, 34, 6, 50],
            [26, 15, 47, 31, 49, 32, 12, 13, 45, 43, 7, 15, 49, 1, 18, 3, 16, 31, 42, 18]
        ]) == -10864880444578748611099584198868992

# Составление матриц большего размера - дело трудозатратное (в том числе и по месту),
# поэтому будем использовать случайные матрицы размером n * n. 
#
# Для утверждения того, что наш результат верный, дудем сравнивать его с результатом
# работы функции det из numpy.linalg (матрицы в функциях будут одинаковыми).
#
# Так как числа будут получаться крайне большими, для сравнения будет использовать метод
# isclose из модуля math.

    def test_50by50_random(self):
        matr = [[random.randint(1, 50) for x in range(50)] for y in range(50)]
        assert math.isclose(
            numpy.float64(determinant(matr)),
            numpy.linalg.det(matr)
        )

    def test_100by100_random(self):
        matr = [[random.randint(1, 50) for x in range(100)] for y in range(100)]
        assert math.isclose(
            numpy.float64(determinant(matr)),
            numpy.linalg.det(matr)
        )
        
    def test_150by150_random(self):
        matr = [[random.randint(1, 50) for x in range(150)] for y in range(150)]
        assert math.isclose(
            numpy.float64(determinant(matr)),
            numpy.linalg.det(matr)
        )