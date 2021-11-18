#Простенькая программка, считающая определитель квадратной матрицы со следующими параметрами:
#> размер матрицы - целое число, введённое пользователем
#> элементы матрицы - случайные числа из диапазона от 1 до 10
import random

def gauss(matr):
    for i in range(len(matr)):
        if (matr[i][i] == 0): continue
        for j in range(i+1, len(matr[i])):
            c = matr[j][i] / matr[i][i]
            for k in range(i, len(matr[i])):
                matr[j][k] -= c * matr[i][k]
    return matr

def determinant(matr):
    result = 1.0; gauss(matr); 
    for i in range(len(matr)):
        result *= matr[i][i];
    return round(result)

size = int(input()); 
if (size < 1):
    size = random.randint(1,10);
mas = [[0] * size for i in range(size)];
for i in range(len(mas)):
    for j in range(len(mas[i])):
        mas[i][j] = random.randint(1,10);
print("Matrix:", mas)
print("Determinant is", determinant(mas))
