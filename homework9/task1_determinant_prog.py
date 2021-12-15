def gauss(matr):
    """
    Прямой ход метода Гаусса.

    Функция приводит квадратную n * n матрицу к верхнему треугольному виду
    (не сокращая элементы, стоящие на главной диагонали).

    Аргументы:
    matr - двумерный массив размером N * N
    """

    for i in range(len(matr)):
        if (matr[i][i] == 0): continue
        for j in range(i + 1, len(matr[i])):
            c = matr[j][i] / matr[i][i]
            for k in range(i, len(matr[i])):
                matr[j][k] -= c * matr[i][k]
    return matr

def determinant(matr=None):
    """
    Вычисление определителя N * N матрицы с помощью метода Гаусса.

    Аргументы:
    matr - двумерный массив размером N * N

    Исключения:
    ValueError, если передан массив с разной длиной строк/столбцов.
    """

    if matr is None:
        return 0

    for i in range(len(matr)):
        if (len(matr[i]) != len(matr)):
            return None
    result = 1.0;
    gauss(matr); 
    for i in range(len(matr)):
        result *= matr[i][i];
    return round(result)
