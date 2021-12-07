import math;
def discriminant(coefs):
    """ Дискриминант квадратного уравнения.
    
    Аргументы: 
    coeffs - список/кортеж значений коэффициентов квадратного уравнения
    """
    
    return float(coefs[1]) ** 2  - 4 * float(coefs[0]) * float(coefs[2])

coeffs = [float(x) for x in input("Введите коэффициенты квадратного уравнения (через пробел): ").split(" ")];

if (coeffs[0] == 0 or len(coeffs) != 3):
    print("Уравнение не является квадратным")
    exit()

print(f'Дискриминант равен {discriminant(coeffs)}\nКорни уравнения: ')
if (discriminant(coeffs) >= 0):
    # x1,2 == (-b +- sqrt(discriminant())) / (2 * a)
    x1 = (-coeffs[1] + math.sqrt(discriminant(coeffs))) / (2 * coeffs[0])
    print(f'Корни уравнения: x1 == {x1}', end='');
    if (discriminant(coeffs) > 0):
        x2 = (-coeffs[1] - math.sqrt(discriminant(coeffs))) / (2 * coeffs[0])
        print(f', x2 == {x2}')
else:
    x1_complex = complex(-coeffs[1], math.sqrt(abs(discriminant(coeffs)))) / (2 * coeffs[0])
    x2_complex = complex(-coeffs[1], math.sqrt(abs(discriminant(coeffs))) * (-1.0)) / (2 * coeffs[0])
    print(f'x1 == {x1_complex}, x2 == {x2_complex}')
