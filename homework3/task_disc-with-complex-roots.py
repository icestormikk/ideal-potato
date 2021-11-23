import math;
def discriminant(coefs):
    #coef[0] == a, coef[1] == b, coef[2] = c
    return float(coefs[1]) ** 2  - 4 * float(coefs[0]) * float(coefs[2])

coeffs = [float(x) for x in input("Введите коэффициенты квадратного уравнения (через пробел): ").split(" ")];

if (coeffs[0] == 0 or len(coeffs) != 3):
    print("Уравнение не является квадратным")
    exit()

print(f'Дискриминант равен {discriminant(coeffs)}\nКорни уравнения: ')
if (discriminant(coeffs) >= 0):
    print(f'x1 == {(-coeffs[1] + math.sqrt(discriminant(coeffs))) / (2 * coeffs[0])}', end='');
    if (discriminant(coeffs) > 0):
        print(f', x2 == {(-coeffs[1] - math.sqrt(discriminant(coeffs))) / (2 * coeffs[0])}')
else:
    print(f'x1 == {complex(-coeffs[1], math.sqrt(abs(discriminant(coeffs)))) / (2 * coeffs[0])}, x2 == {complex(-coeffs[1], math.sqrt(abs(discriminant(coeffs))) * (-1.0)) / (2 * coeffs[0])}')
